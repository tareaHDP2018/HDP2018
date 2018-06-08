from django.conf.urls import url,include
from apps.login_registrar.views import *
app_name='login_registrar'
urlpatterns=[
 url(r'^$',login, name='log'),
 url(r'^registrar/$',registrar,name='registrar'), 
 url(r'^logout/$',logout,name='lo'),
 url(r'^404/$',handler404,name='404'),
 url(r'^500/$',handler500,name='500'),





]
