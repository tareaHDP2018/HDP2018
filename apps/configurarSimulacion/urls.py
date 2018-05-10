from django.conf.urls import url,include
from apps.configurarSimulacion.views import nuevo,configuracion,index

urlpatterns=[
url(r'^$',index),
 url(r'^nuevo$',nuevo,name='nuevo'),
 url(r'^configurar$',configuracion,name='configuracion'),

]
