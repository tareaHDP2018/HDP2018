from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	nombre_usuario = models.CharField(max_length=50)
	password = models.CharField(max_length=256)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	fechaNacimiento = models.DateField()
	sexo = models.CharField(max_length=9)
	def __str__(self):
		return self.nombre_usuario

class Siembra(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
    	return self.nombre

class Configuracion(models.Model):
	temperaturaMax = models.DecimalField(max_digits=5,decimal_places=2)
	temperaturaMin = models.DecimalField(max_digits=5,decimal_places=2)
	humedad = models.DecimalField(max_digits=6,decimal_places=2)
	altitud = models.DecimalField(max_digits=6,decimal_places=2)
	luminosidad = models.DecimalField(max_digits=5,decimal_places=2)
	distanciaLinea = models.DecimalField(max_digits=5,decimal_places=2)

class FaseCultivo(models.Model):
	germinacion = models.BooleanField(default=0)
	mergencia = models.BooleanField(default=0)
	hojaPrimaria = models.BooleanField(default=0)
	primeraHoja = models.BooleanField(default=0)
	terceraHoja = models.BooleanField(default=0)
	prefloracion = models.BooleanField(default=0)
	floracion = models.BooleanField(default=0) 

class Simulacion(models.Model):
	nombre = models.CharField(max_length=50)
	lineaSiembra = models.IntegerField()
	estado = models.IntegerField()
	configuracion = models.OneToOneField(Configuracion, blank=False,on_delete=models.CASCADE)
	siembra = models.ForeignKey(Siembra, null=True, blank=False,on_delete=models.CASCADE)
	faseCultivo =models.ForeignKey(FaseCultivo,blank=True,on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario,null=True,blank=False)
	def __str__(self):
		return self.nombre  