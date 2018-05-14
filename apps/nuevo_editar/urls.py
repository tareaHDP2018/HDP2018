from django.conf.urls import url,include
from apps.nuevo_editar.views import simulacionCrear,index,grafico,simular

urlpatterns=[
url(r'^$',index),
url(r'^simulacion$',simulacionCrear,name='nuevaSimulacion'),
url(r'^grafico/(?P<idSimulacion>\d+)/$',grafico,name='graficos'),
url(r'^simular$',simular,name='simula'),


]