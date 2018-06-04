from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from apps.nuevo_editar.forms import SimulacionForm, ConfigurarForm
from apps.configurarSimulacion.models import Simulacion,Configuracion,Siembra,FaseCultivo,Usuario
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.urlresolvers import reverse_lazy
from decimal import *
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,View,TemplateView
import json as simplejson
import json
from django.forms.models import model_to_dict
from django.core import serializers



# Create your views here.
def index(request):
	if not request.user.is_active:
			return redirect('/')
	return render(request,'Simulacion/index.html')

def somos(request):
	if not request.user.is_active:
			return redirect('/')

	return render_to_response('Simulacion/quienSomos.html')
 
def simulacionCrear(request):
	if not request.user.is_active:
			return redirect('/')
	us=request.user
	siembras = Siembra.objects.get(id=1)
	usuario_id = Usuario.objects.get(nombre_usuario=us)
	forms = SimulacionForm
	if request.method == 'POST':
		simula = Simulacion()
		confi = Configuracion()
		fase = FaseCultivo()
		fase.germinacion=True if request.POST.get('germinacion') else False
		fase.mergencia=True if request.POST.get('emergencia') else False
		fase.hojaPrimaria=True if request.POST.get('hojaPrimaria') else False
		fase.primeraHoja=True if request.POST.get('primeraHoja') else False
		fase.terceraHoja=True if request.POST.get('terceraHoja') else False
		fase.prefloracion=True if request.POST.get('prefloracion') else False
		fase.floracion=True if request.POST.get('floracion') else False
		fase.save()
		fase_id = FaseCultivo.objects.latest('id')
		
		confi.temperaturaMax = request.POST['temperaturaMax']
		confi.temperaturaMin = request.POST['temperaturaMin']
		confi.humedad = request.POST['humedad']
		confi.altitud = request.POST['altitud']
		confi.luminosidad = request.POST['luminosidad']
		confi.distanciaLinea = request.POST['distanciaL']
		confi.save()
		confi_id = Configuracion.objects.latest('id')

		simula.nombre = request.POST['simulacion']
		simula.lineaSiembra = request.POST['linea']
		simula.estado = 1
		simula.siembra = siembras
		simula.usuario = usuario_id
		simula.configuracion=confi_id
		simula.faseCultivo = fase_id
		simula.save()
		return redirect('nuevo:simula')
	contexto = {'siembras':siembras}
	return render(request,'Simulacion/nuevo.html',contexto)


def simular(request):
	if not request.user.is_active:
			return redirect('/')
	simula = Simulacion.objects.filter(usuario_id=1).latest('id')

	contexto = {'simula':simula}
	return render(request,'Simulacion/simular.html',contexto)

def simularVer(request,idSimulacion):
	if not request.user.is_active:
			return redirect('/')
	simula = Simulacion.objects.get(id=idSimulacion)
	contexto={'simula':simula}
	return render(request,'Simulacion/simular.html',contexto)


"""def grafico(request,idSimulacion):
	e = 2.718281828
	simula = Simulacion.objects.get(id=idSimulacion)
	altura = simula.configuracion.altitud
	tMaxima = simula.configuracion.temperaturaMax
	tMinima = simula.configuracion.temperaturaMin
	humedad = simula.configuracion.humedad
	if tMinima < 8:
		rT = 0
	elif tMaxima <= 12:
		rT = 0.55
	elif tMaxima <= 29:
		rT = 0.75
	elif tMaxima <= 35:
		rT = 1
	elif tMaxima <= 45:
		rT=1
	elif tMaxima <= 50:
		rt=0

	tiempo = tiempoDia(simula)
	hFase = hidricoFase(simula)
	contador = len(tiempo)
	validar2 = validar(simula)
	tiempo2=[]
	for a in tiempo:
		tiempo2.append(float(a))

	rm = Decimal((altura))*Decimal((0.021))
	N=[]
	for t in tiempo2:
		if t == 0:
			N.append(0)
		else:
			getcontext().prec = 2
			N.append(float(Decimal(e)**(Decimal(rm)*Decimal(float(t)))*Decimal(rT)))

	numero = len(N)
	
	nodos2 = simplejson.dumps(N)
	jsonParametros(nodos2)

	return render_to_response('Simulacion/grafico.html',{'nodos':nodos2,'simula':simula,'tiempo':tiempo2,'hidrico':hFase,'humedad':humedad,'numero':numero,'validar':validar2})"""

"""def jsonParametros(nodo,hidrico,humedad,validar):
	data = {"nodos":nodo,"hidrico":hidrico,"humedad":humedad,"validar":validar}
	return JsonResponse(data)"""

def jsonParametros(request):
	e = 2.718281828
	idSimulacion = request.GET.get('grafico')
	simula = Simulacion.objects.get(id=idSimulacion)
	altitud = float(simula.configuracion.altitud)
	valida = validar(simula)
	humedad = float(simula.configuracion.humedad)
	tMaxima = float(simula.configuracion.temperaturaMax)
	tMinima = float(simula.configuracion.temperaturaMin)
	hidrico = hidricoFase(simula)
	faseC = fase(simula) 

	if tMinima < 8:
		rT = 0
	elif tMaxima <= 12:
		rT = 0.55
	elif tMaxima <= 29:
		rT = 0.75
	elif tMaxima <= 35:
		rT = 1
	elif tMaxima <= 45:
		rT=1
	elif tMaxima <= 50:
		rT=0
	tiempo = tiempoDia(simula)
	tiempo2=[]
	for a in tiempo:
		tiempo2.append(float(a))

	rm = Decimal((altitud))*Decimal((0.021))
	N=[]
	for t in tiempo2:
		if t == 0:
			N.append(0)
		else:
			getcontext().prec = 4
			N.append(float(Decimal(e)**(Decimal(rm)*Decimal(float(t)))*Decimal(rT)))
	
	#nodos = [1,2,3,4,5,6,7]
	nodos = N
	contexto = {'altitud':altitud,'humedad':humedad,'nodos':nodos,'valida':valida,'hidrico':hidrico,'fase':faseC}
	return HttpResponse(json.dumps(contexto),content_type='application/json') 

def simula_serializer(simula):
	return {'altitud':simula.configuracion.altitud}


def tiempoDia(simulacion2):
	t =[]
	if simulacion2.faseCultivo.germinacion:
		t.append("5")
	else:
		t.append("0")
	if simulacion2.faseCultivo.mergencia:
		t.append("2")
	else:
		t.append("0")
	if simulacion2.faseCultivo.hojaPrimaria:
		t.append("4")
	else:
		t.append("0")
	if simulacion2.faseCultivo.primeraHoja:
		t.append("5")
	else:
		t.append("0")
	if simulacion2.faseCultivo.terceraHoja:
		t.append("7")
	else:
		t.append("0")
	if simulacion2.faseCultivo.prefloracion:
		t.append("9")
	else:
		t.append("0")
	if simulacion2.faseCultivo.floracion:
		t.append("4")
	else:
		t.append("0")
	return t 

def hidricoFase(simulacion):
	t =[]
	if simulacion.faseCultivo.germinacion:
		t.append(float(19.35))
	else:
		t.append(0)
	if simulacion.faseCultivo.mergencia:
		t.append(float(19.35))
	else:
		t.append(0)
	if simulacion.faseCultivo.hojaPrimaria:
		t.append(float(19.35))
	else:
		t.append(0)
	if simulacion.faseCultivo.primeraHoja:
		t.append(float(37.57))
	else:
		t.append(0)
	if simulacion.faseCultivo.terceraHoja:
		t.append(float(37.57))
	else:
		t.append(0)
	if simulacion.faseCultivo.prefloracion:
		t.append(float(48.1))
	else:
		t.append(0)
	if simulacion.faseCultivo.floracion:
		t.append(float(43.65))
	else:
		t.append(0)
	return t

def validar(simulacion2):
	t =[]
	if simulacion2.faseCultivo.germinacion:
		t.append(1)
	else:
		t.append(0)
	if simulacion2.faseCultivo.mergencia:
		t.append(1)
	else:
		t.append(0)
	if simulacion2.faseCultivo.hojaPrimaria:
		t.append(1)
	else:
		t.append(0)
	if simulacion2.faseCultivo.primeraHoja:
		t.append(1)
	else:
		t.append(0)
	if simulacion2.faseCultivo.terceraHoja:
		t.append(1)
	else:
		t.append(0)
	if simulacion2.faseCultivo.prefloracion:
		t.append(1)
	else:
		t.append(0)
	if simulacion2.faseCultivo.floracion:
		t.append(1)
	else:
		t.append(0)
	return t 

def fase(simulacion2):
	t =[]
	if simulacion2.faseCultivo.germinacion:
		t.append('Germinacion')
	if simulacion2.faseCultivo.mergencia:
		t.append('Emergencia')
	if simulacion2.faseCultivo.hojaPrimaria:
		t.append('Hoja primaria')
	if simulacion2.faseCultivo.primeraHoja:
		t.append('Primera hoja')
	if simulacion2.faseCultivo.terceraHoja:
		t.append('Tercera hoja')
	if simulacion2.faseCultivo.prefloracion:
		t.append('Prefloracion')
	if simulacion2.faseCultivo.floracion:
		t.append('Floracion')
	return t



