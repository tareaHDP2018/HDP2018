from django.http import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.shortcuts import render,redirect
from .forms import *
from django.template import loader
from django.views.defaults import page_not_found
def login(request):
    if request.user.is_active:
            return redirect('/simula')
    error=''
    if request.method=='POST':
        form = LoginForm(request.POST)
        nom=request.POST.get('nombre_usuario',None)
        con=request.POST.get('password',None) 
        us=Usuario.objects.filter(nombre_usuario=nom,password=con).exists()
        if form.is_valid()and us==True:
            #nom=request.POST.get('nombre',None)
            
            user=authenticate(username=nom,password=con)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/simula')     
        else:
         form=LoginForm()
         error="error en el nombre de usuario o contraseña"
    else:
      form=LoginForm()
    template=loader.get_template('sesion/login.html')
    context={
    'form':form,
    'error':error
    }
    return HttpResponse(template.render(context,request))


def logout (request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def registrar(request):
    error=''
    if request.method=='POST':
        form = RegistrarForm(request.POST)
        nom=request.POST.get('nombre de usuario',None)
        us=Usuario.objects.filter(nombre_usuario=nom).exists()
        if us==False and form.is_valid(): 
            usuario=form.save()
            usuario.save()
            user=User.objects.create_user(username=usuario.nombre_usuario,password=usuario.password)
            user=authenticate(username=usuario.nombre_usuario,password=usuario.password)
            login(request)
            return HttpResponseRedirect('/')     
        else:
         form=RegistrarForm()
         error="error el nombre de usuario ya esta en uso"

    else:
      form=RegistrarForm()
    template=loader.get_template('sesion/registrar.html')
    context={
    'form':form,
    'error':error
    }
    return HttpResponse(template.render(context,request))

    
def handler404(request):
    
    return render(request,'sesion/404.html',status=404)


def handler500(request):
    
    return render(request,'sesion/500.html',status=500)