from django.shortcuts import render,redirect
from apps.configurarSimulacion.models import Configuracion
from django.http import HttpResponse, HttpResponseRedirect
from apps.configurarSimulacion.forms import *

# Create your views here.
def index(request):
	if not request.user.is_active:
			return redirect('/')
	return render(request,'Simulacion/index.html')

def nuevo(request):
	 
	if not request.user.is_active:
			return redirect('/')
	return render(request,'Simulacion/nuevo.html')

def configuracion(request):
	if not request.user.is_active:
			return HttpResponseRedirect('/')
	if request.method == 'POST':
	   configurar = Configuracion()
	   configurar.temperaturaMax = request.POST['temperaturaMax']
	   configurar.temperaturaMin = request.POST['temperaturaMin']
	   configurar.humedad = request.POST['humedad']
	   configurar.altitud = request.POST['altitud']
	   configurar.luminosidad = request.POST['luminosidad']
	   configurar.distanciaLinea = request.POST['distanciaL']
	   configurar.save()
	   return redirect('configurar:nuevo')
	return render(request,'Simulacion/configuracion.html')
 