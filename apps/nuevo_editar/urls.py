from django.conf.urls import url,include
from apps.nuevo_editar.views import simulacionCrear,index,grafico

urlpatterns=[
url(r'^$',index),
url(r'^simulacion$',simulacionCrear.as_view(),name='nuevaSimulacion'),
url(r'^grafico$',grafico,name='graficos'),


]