from django.conf.urls import url,include
from apps.consultar.views import simulacionlist

urlpatterns=[
 url(r'^simulaciones$',simulacionlist,name='consultar'),

]