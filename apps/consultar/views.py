
from django.shortcuts import render,redirect


from apps.configurarSimulacion.models import Simulacion
from apps.configurarSimulacion.forms import ConfigurarForm
# Create your views here.
def simulacionlist(request):
	 simulacion = Simulacion.objects.all()
	 contexto = {'simulaciones':simulacion }
	 return render(request, 'Simulacion/consultar.html', contexto)
# Create your views here.from django.shortcuts import renderfrom django.shortcuts import render

def simulacion_editar(request,id_simulacion):
	simulacion = Simulacion.objects.get(id=id_simulacion)
	if request.method== 'GET':
		form = ConfigurarForm(instance=simulacion)

	else:
		form = ConfigurarForm(request.POST, instance=simulacion)
		if form.is_valid():
			form.save()

		return redirect('consulta:editar')

	return render(request,'Simulacion/nuevo.html',{'form':form})
# Create your views here.

def simulacion_eliminar(request):
	simulacion = Simulacion.objects.get()
	if request.method== 'POST':
		simulacion.delete()

		return redirect('consulta:editar')


	return render(request,'Simulacion/simulaciondelete.html',{'simulacion':simulacion})
# Create your views here.
