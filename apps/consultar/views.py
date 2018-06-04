
from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from apps.configurarSimulacion.models import Simulacion,Configuracion,Siembra,FaseCultivo,Usuario
#from apps.configurarSimulacion.forms import ConfigurarForm
 
# Create your views here.
def simulacionlist(request):
	if not request.user.is_active:
			return redirect('/')
	us=request.user
	usua=Usuario.objects.get(nombre_usuario=us)
	simulacion = Simulacion.objects.filter(estado=1).filter(usuario=usua).order_by('-id')
	contexto = {'simulaciones':simulacion }
	return render(request, 'Simulacion/consultar.html', contexto)

@csrf_protect
def simulacionEditar(request,idSimulacion):
	if not request.user.is_active:
			return redirect('/')

	us=request.user
	usuario_id=Usuario.objects.get(nombre_usuario=us)
	simulacion = get_object_or_404(Simulacion,pk=idSimulacion)
	configura = get_object_or_404(Configuracion,pk=idSimulacion)
	
	siembras = Siembra.objects.get(id=1)
	#usuario_id =usua.id
	if request.method == 'POST':
		simulaElimina = Simulacion.objects.get(id=idSimulacion)
		simulaElimina.delete()
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

		

		return redirect('consulta:consultar')
	else:
		contexto = {'simula':simulacion,'confi':configura,'siembras':siembras}
		#contexto.update(csrf(request))
		return render(request,'Simulacion/editarSimulacion.html',contexto)

def simulacionEliminar(request,idSimulacion):
	if not request.user.is_active:
			return redirect('/')

	simulacion = get_object_or_404(Simulacion,pk=idSimulacion)
	configura = get_object_or_404(Configuracion,pk=idSimulacion)
	simula2 = Simulacion.objects.get(id=idSimulacion)
	simula2 = Simulacion.objects.get(id=idSimulacion)
	nombre=simulacion.nombre
	if request.method == 'POST':
		simula2.delete()
		return redirect('consulta:consultar')
	else:
		return render(request,'Simulacion/simulaciondelete.html',context={'nombre':nombre})
