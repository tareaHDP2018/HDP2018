from django.conf.urls import url,include
from apps.login_registrar.views import *
urlpatterns=[
 url(r'^login/$',auth_login),
 url(r'^login/registrar$',auth_registrar),
 



]
