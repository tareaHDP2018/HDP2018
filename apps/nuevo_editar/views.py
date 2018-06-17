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
import math



# Create your views here.
#FUNCION QUE ENVIA AL INICIO DE LA APLICACION 
def index(request):
	if not request.user.is_active:
			return redirect('/')
	return render(request,'Simulacion/index.html')

#ENVIAR AL INICIO DE SESION, CUANDO EL USUARIO NO SE A LOGUEADO
def somos(request):
	if not request.user.is_active:
			return redirect('/')

	return render_to_response('Simulacion/quienSomos.html')
 
#FUNCION PARA CREAR UNA NUEVA SIMULACION, SE OCUPAN LAS CLASES CORRESPONDIENTES
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
		#VALIDO LA ENTRADA, PARA CONOCER SI ES TRUE O FALSE
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


#FUNCION QUE PERMITE MOSTRAR LA SIMULACION A GRAFICAR, INTRODUCIDA POR EL USUARIO
def simular(request):
	if not request.user.is_active:
			return redirect('/')
	us=request.user
	usua=Usuario.objects.get(nombre_usuario=us)
	simula = Simulacion.objects.filter(usuario=usua).latest('id')

	contexto = {'simula':simula}
	return render(request,'Simulacion/simular.html',contexto)

#FUNCION PARA PODER VER LAS SIMULACIONES HECHAS ANTERIORMENTE EN EL LISTADO
def simularVer(request,idSimulacion):
	if not request.user.is_active:
			return redirect('/')
	us=request.user
	usua=Usuario.objects.get(nombre_usuario=us)
	simula = Simulacion.objects.filter(usuario=usua).get(id=idSimulacion)
	contexto={'simula':simula}
	return render(request,'Simulacion/simular.html',contexto)

#FUNCION QUE NOS RETORNA MEDIANTE JSON LOS DATOS CALCULADOS PARA SER USADOS EN LOS GRAFICOS 
def jsonParametros(request):
	e = 2.71
	idSimulacion = request.GET.get('grafico')
	simula = Simulacion.objects.get(id=idSimulacion)
	altitud = float(simula.configuracion.altitud)
	valida = validar(simula)
	humedad = float(simula.configuracion.humedad)
	tMaxima = float(simula.configuracion.temperaturaMax)
	tMinima = float(simula.configuracion.temperaturaMin)
	lumi = float(simula.configuracion.luminosidad)
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

	rm = (altitud)*(0.021)
	NodoTotal=[]
	for t in tiempo2:
		if t == 0:
			NodoTotal.append(0)
		else:
			potencia = (rm*t*rT)/1000
			N=math.pow(e,potencia)
			Econver = humedad*(0.70)
			crecimiento = Econver*((lumi*tMinima)-(0.0693*(tMaxima-25)))*(N*(0.85))
			crecimiento2 = crecimiento/1000
			crecimiento3 = round(crecimiento2,2)
			NodoTotal.append(crecimiento3)
	nodos = NodoTotal
	divHumedad = humedad/10
	if divHumedad < hidrico[3]:
		mns = "Hidricos por debajo del nivel"
	elif divHumedad > hidrico[2]*2:
		mns = " Mucha humedad al cultivo"
	else:
		mns = "Hidricos aceptables para el cultivo"

	#CONTEXTO ENVIADO CON TODOS LOS DATOS
	contexto = {'altitud':altitud,'humedad':humedad,'nodos':nodos,'valida':valida,'hidrico':hidrico,'fase':faseC,'mensaje':mns}
	return HttpResponse(json.dumps(contexto),content_type='application/json') 

def simula_serializer(simula):
	return {'altitud':simula.configuracion.altitud}

#
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

#SELECCIONANDO HIDRICOS SEGUN FASE DE CULTIVO SELECCIONADA
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

#VALIDAR SEGUN FASE DE CULTIVO SELECCIONADA
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



