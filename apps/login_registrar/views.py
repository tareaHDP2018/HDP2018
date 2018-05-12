from django.http import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.shortcuts import render,redirect
from .forms import *
from django.template import loader

def login(request):
    if request.method=='POST':
       username=request.POST.get('username',None)
       password=request.POST.get('password',None)
       user=authenticate(username=username,password=password)
       if user is not None and user.is_activate:
         auth.login(request,user)
         return HttpResponseRedirect('/simula')
    return render(request,'sesion/login.html',context=None)


def logout (request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

def registrar(request):
    if request.method=='POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            usuario.save()
            user=User.objects.create_user(username=usuario.nombre,password=usuario.password)
            user.save()
            return HttpResponseRedirect('/simula')     
    else:
        form=RegistrarForm()
    template=loader.get_template('sesion/registrar.html')
    context={
    'form':form
    }
    return HttpResponse(template.render(context,request))

    