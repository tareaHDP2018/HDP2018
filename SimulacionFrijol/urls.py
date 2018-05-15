"""SimulacionFrijol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from apps.login_registrar.views import handler404,handler500
from django.conf.urls import handler404,handler500


handler404=handler404 
handler500=handler500
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^simula/', include('apps.configurarSimulacion.urls',namespace="configurar")),
    
    url(r'^',include('apps.login_registrar.urls',namespace="login")),
    url(r'^nuevo/',include('apps.nuevo_editar.urls',namespace="nuevo")),
    url(r'^consultar/',include('apps.consultar.urls',namespace="consulta")),

    #AQUI VAN A AGREGAR CADA UNO SUS URL GLOBLAES, Y CADA QUIEN TRABAJARA EN SU APPS ASIGNADA,
    # NO TOQUEN LAS URLS YA DEFINIDAS SIN PREVIO AVISO EN EL GRUPO
]
