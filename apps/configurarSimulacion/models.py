from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	password = models.CharField(max_length=256)
	fechaNacimiento = models.DateField()
	sexo = models.CharField(max_length=9)

class Siembra(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
    	return self.nombre

class Configuracion(models.Model):
	temperaturaMax = models.DecimalField(max_digits=5,decimal_places=2)
	temperaturaMin = models.DecimalField(max_digits=5,decimal_places=2)
	humedad = models.DecimalField(max_digits=5,decimal_places=2)
	altitud = models.DecimalField(max_digits=5,decimal_places=2)
	luminosidad = models.DecimalField(max_digits=5,decimal_places=2)
	distanciaLinea = models.DecimalField(max_digits=5,decimal_places=2)

class FaseCultivo(models.Model):
	etapa = models.IntegerField()
	descripcion = models.CharField(max_length=30)
	diasDuracion = models.IntegerField()
	hidricos = models.DecimalField(max_digits=3,decimal_places=2)

class Simulacion(models.Model):
	nombre = models.CharField(max_length=50)
	lineaSiembra = models.IntegerField()
	estado = models.IntegerField()
	configuracion = models.OneToOneField(Configuracion, blank=False)
	siembra = models.OneToOneField(Siembra, null=True, blank=False)
	faseCultivo =models.ManyToManyField(FaseCultivo)
	usuario = models.ForeignKey(Usuario,null=True,blank=False)
	def __str__(self):
		return self.nombre  