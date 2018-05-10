from django.shortcuts import render,redirect
from apps.configurarSimulacion.models import Configuracion
from django.http import HttpResponse
from apps.configurarSimulacion.forms import *

# Create your views here.
def index(request):
	return render(request,'Simulacion/index.html')

def nuevo(request):
	return render(request,'Simulacion/nuevo.html')

def configuracion(request):
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

	   #form = configurarForms(request.POST)

"""def configuracion(request):
	if request.method == 'POST':
		form = ConfiguraForms(request.POST)
		if form.is_valid():
			form.save()
		return redirect('configurar:nuevo')
	else:
		form = ConfiguraForms()
	return render(request,'Simulacion/configuracion.html',{'formulario':form})"""