from django.conf.urls import url,include
from apps.login_registrar.views import *
app_name='login_registrar'
urlpatterns=[
 url(r'^$',login, name='log'),
 url(r'^registrar/$',registrar,name='registrar'),
 #url(r'^login/registrar$',auth_registrar),
 



]
