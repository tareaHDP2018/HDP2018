from django.shortcuts import render,redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.configurarSimulacion.models import Usuario
# Create your views here.
def auth_login(request):
	if request.method== 'POST':
		action=request.POST.get('action',None)
		username=request.POST.get('username',None)
		password= request.POST.get('password',None)
		if action == 'signup':
			user=Usuario.objects.create_user(nombre=username,password=password)
			user.save()
			redirect('/login')
		elif action== 'login':
		  user = Usuario(nombre=username, password=password)
		  login(request,user)
		  redirect('/simula')
	context={}
	return render(request,'sesion/login.html',context)

def auth_registrar(request):
	if request.method== 'POST':
		action=request.POST.get('action',None)
		username=request.POST.get('username',None)
		password= request.POST.get('password',None)
		fecha=request.POST.get('fecha',None)

		if action == 'signup':
			user=Usuario(nombre=username,password=password,fechaNacimiento=fecha)
			user.save()
			redirect('sesion/login')
		elif action== 'login':
		  user = authenticate(username=username, password=password)
		  login(request,user)
	context={}
	return render(request,'sesion/registrar.html',context)