from django.conf.urls import url,include
from apps.consultar.views import *


 
urlpatterns=[
 url(r'^simulaciones$',simulacionlist,name='consultar'),
 url(r'^editar/(?P<idSimulacion>\d+)/$',simulacionEditar,name='editar'),
  url(r'^eliminarSimulacion/(?P<idSimulacion>\d+)$',simulacionEliminar,name='eliminar'),

]