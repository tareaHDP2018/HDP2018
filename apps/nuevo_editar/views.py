from django.shortcuts import render,redirect
from apps.nuevo_editar.forms import SimulacionForm, ConfigurarForm
from apps.configurarSimulacion.models import Simulacion,Configuracion,Siembra,FaseCultivo,Usuario
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView,CreateView,DeleteView,UpdateView,View

# Create your views here.
def index(request):
	return render(request,'Simulacion/index.html')

def simulacionCrear(request):
	siembras = Siembra.objects.get(id=1)
	usuario_id = Usuario.objects.get(id=1)
	forms = SimulacionForm
	if request.method == 'POST':
		simula = Simulacion()
		confi = Configuracion()
		fase = FaseCultivo()
		fase.germinacion=True if request.POST.get('germinacion') else False
		fase.mergencia=True if request.POST.get('mergencia') else False
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
	simula = Simulacion.objects.filter(usuario_id=1).latest('id')
	contexto = {'simula':simula}
	return render(request,'Simulacion/simular.html',contexto)


def grafico(request,idSimulacion):
	simula = Simulacion.objects.get(id=idSimulacion)


	return render(request,'Simulacion/grafico.html')