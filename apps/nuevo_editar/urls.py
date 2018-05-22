from django.conf.urls import url,include
from apps.nuevo_editar.views import simulacionCrear,index,grafico,simular,simulacionEditar

urlpatterns=[
url(r'^inicio$',index,name='inicio'),
url(r'^simulacion$',simulacionCrear,name='nuevaSimulacion'),
url(r'^grafico/(?P<idSimulacion>\d+)/$',grafico,name='graficos'),
url(r'^simular$',simular,name='simula'),
url(r'^editarSimulacion/(?P<idSimulacion>\d+)/$',simulacionEditar,name='editar'),
#url(r'^consultaGrafico$',consultaGrafico,name='ajaxConsulta'),


]