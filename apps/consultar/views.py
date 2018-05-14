
from django.shortcuts import render


from apps.configurarSimulacion.models import Simulacion
# Create your views here.
def simulacionlist(request):
	 simulacion = Simulacion.objects.all()
	 contexto = {'simulaciones':simulacion }
	 return render(request, 'Simulacion/consultar.html', contexto)
# Create your views here.from django.shortcuts import renderfrom django.shortcuts import render

# Create your views here.
