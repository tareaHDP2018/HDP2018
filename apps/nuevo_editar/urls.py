from django.conf.urls import url,include
from apps.nuevo_editar.views import simulacionCrear,index,simular,somos,jsonParametros,simularVer
#,grafico

urlpatterns=[
url(r'^inicio$',index,name='inicio'),
url(r'^simulacion$',simulacionCrear,name='nuevaSimulacion'),
#url(r'^grafico/(?P<idSimulacion>\d+)/$',grafico,name='graficos'),
url(r'^simular$',simular,name='simula'),
url(r'^simularVer/(?P<idSimulacion>\d+)/$',simularVer,name='simularVer'),
#url(r'^editarSimulacion/(?P<idSimulacion>\d+)/$',simulacionEditar,name='editar'),
url(r'^somos$',somos,name='somos'),
url(r'^consultaGrafico$',jsonParametros,name='ajaxConsulta'),


]