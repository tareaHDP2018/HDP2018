from django.conf.urls import url,include
from apps.consultar.views import simulacionlist,simulacion_editar,simulacion_eliminar

urlpatterns=[
 url(r'^simulaciones$',simulacionlist,name='consultar'),
 url(r'^editar/(?P<id_simulacion>\d*)/$',simulacion_editar,name='editar'),
  url(r'^eliminar/(?P<id_simulacion>\d*)/$',simulacion_eliminar,name='eliminar'),

]