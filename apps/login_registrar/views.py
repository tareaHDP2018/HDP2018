#librerias utilizadas para el desarrollo del login y register
from django.http import * 
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.shortcuts import render,redirect
from .forms import * # se importan los formularios necesarios para realizar el login y register
from django.template import loader
from django.views.defaults import page_not_found
def login(request): #funcion de login
    if request.user.is_active:   # valida si el usuario ya accedio al sistema
            return redirect('/simula')# si ya esta logeado lo redirige a la pagina principal
    error=''
    if request.method=='POST':        
        form = LoginForm(request.POST)   # recibe los datos 
        nom=request.POST.get('nombre_usuario',None)
        con=request.POST.get('password',None) 
        us=Usuario.objects.filter(nombre_usuario=nom,password=con).exists()# verifica si el nombre de usuario existe 
        # y la contraseña valida
        if form.is_valid()and us==True:
            # si el formulario es valido y el usuario existe permite el acceso al sistema
            user=authenticate(username=nom,password=con)
            if user is not None:
                auth.login(request,user) 
                return HttpResponseRedirect('/simula')     
        else:
         form=LoginForm() # si el usuario no existe  o la contraseña fue incorrecta
         #limpia el formulario y envia un contexto 
         error="error en el nombre de usuario o contraseña"
    else:
      form=LoginForm()
    template=loader.get_template('sesion/login.html')#carga la vista que se va utilizar
    context={ #el contexto que sera enviado
    'form':form,
    'error':error
    }
    return HttpResponse(template.render(context,request))# renderiza el template y le da un contexto


def logout (request):# funcion para que el usuario cierre la sesion
    auth.logout(request)
    return HttpResponseRedirect("/") #lo redirige a la pagina de inicio de sesion

def registrar(request):
    error=''
    if request.method=='POST':
        form = RegistrarForm(request.POST)   #recoge todos los datos ingresados 
        nom=request.POST.get('nombre_usuario',None)
                
        if User.objects.filter(username=nom).exists()==False and form.is_valid(): 
        # si el nombre de usuario no existe y el formulario no tiene errores
            usuario=form.save() 
            usuario.save() #guarda los datos del formulario ingresado
            user=User.objects.create_user(username=usuario.nombre_usuario,password=usuario.password)#crea el usuario 
            user=authenticate(username=usuario.nombre_usuario,password=usuario.password) #autentifica el usuario  
            login(request) #inicia la sesion del usuario recien creado
            return HttpResponseRedirect('/')     
        if User.objects.filter(username=nom).exists()==True and form.is_valid()and nom!=' ':
            #verifica si el usuario existe y si el formulario es valido y si el nombre de usuario ingresado no esta vacio
         form=RegistrarForm() #limpia el formulario 
         error="error el nombre de usuario ya esta en uso"

    else:
      form=RegistrarForm() #si la peticion no es post limpia el formulario
    template=loader.get_template('sesion/registrar.html') # carga el template
    context={
    'form':form,
    'error':error
    }
    return HttpResponse(template.render(context,request))

    
def handler404(request):# personalizando error 404
    
    return render(request,'404.html',status=404)


def handler500(request):# personalizando error 500
    
    return render(request,'500.html',status=500)