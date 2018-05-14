from django.shortcuts import render,redirect
from apps.nuevo_editar.forms import SimulacionForm, ConfigurarForm
#from apps.configurarSimulacion.forms import ConfigurarForm
from apps.configurarSimulacion.models import Simulacion,Configuracion,Siembra,FaseCultivo
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView,CreateView,DeleteView,UpdateView,View

# Create your views here.
def index(request):
	return render(request,'Simulacion/index.html')

def simulacionCrear(request):
	siembras = Siembra.objects.get(id=1)
	fase = FaseCultivo.objects.all().order_by('id')
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
		#simula.usuario = 1
		simula.configuracion=confi_id
		simula.faseCultivo = fase_id
		simula.save()
		#variable = request.POST['temperaturaMax']
		
		return redirect('consulta:consultar')
	contexto = {'siembras':siembras,'fase':fase,'forms':forms}
	return render(request,'Simulacion/nuevo.html',contexto)
"""
class simulacionCrear(CreateView):
	model = Simulacion
	template_name = 'Simulacion/nuevo.html'
	form_class = SimulacionForm
	second_form_class = ConfigurarForm
	success_url = reverse_lazy('nuevo:graficos')


	def get_context_data(self,**kwargs):
		context = super(simulacionCrear,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2']=self.second_form_class(self.request.GET)
		return context

	def post(self,request,*args,**kwargs):
		siembras = Siembra.objects.get(id=1)
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			simula = form.save(commit=False)
			#simula.faseCultivo = request.POST["faseCultivo"]
			simula.estado = 1
			simula.siembra = siembras
			simula.configuracion = form2.save()
			#simula.usuario = 1
			simula.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form,form2=form2))"""

def grafico(request):
	return render(request,'Simulacion/grafico.html')