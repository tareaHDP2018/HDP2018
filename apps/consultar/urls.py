from django.conf.urls import url,include
from apps.consultar.views import simulacionlist,simulacionEditar

 
urlpatterns=[
 url(r'^simulaciones$',simulacionlist,name='consultar'),
 url(r'^editar/(?P<idSimulacion>\d+)/$',simulacionEditar,name='editar'),
  #url(r'^eliminar/(?P<id_simulacion>\d*)/$',simulacion_eliminar,name='eliminar'),

]