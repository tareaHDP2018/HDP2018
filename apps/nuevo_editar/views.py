from django.shortcuts import render,redirect
from apps.nuevo_editar.forms import SimulacionForm
from apps.configurarSimulacion.models import Simulacion,Configuracion,Siembra,FaseCultivo
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
	return render(request,'Simulacion/index.html')

def simulacionCrear(request):
	siembras = Siembra.objects.get(id=1)
	fase = FaseCultivo.objects.all().order_by('id')
	if request.method == 'POST':
		simula = Simulacion()
		confi = Configuracion()
		
		confi.temperaturaMax = request.POST['temperaturaMax']
		confi.temperaturaMin = request.POST['temperaturaMin']
		confi.humedad = request.POST['humedad']
		confi.altitud = request.POST['altitud']
		confi.luminosidad = request.POST['luminosidad']
		confi.distanciaLinea = request.POST['distanciaL']
		confi.save()

		simula.nombre = request.POST['simulacion']
		simula.lineaSiembra = request.POST['linea']
		simula.estado = 1
		simula.siembra = request.POST['siembra']
		simula.usuario = 1
		simula.faseCultivo = request.POST['fase']
		simula.configuracion=confi.objects.get('id')
		simula.save()
		
		return redirect('nuevo:graficos')
	contexto = {'siembras':siembras,'fase':fase}
	return render(request,'Simulacion/nuevo.html',contexto)

def grafico(request):
	return render(request,'Simulacion/grafico.html')