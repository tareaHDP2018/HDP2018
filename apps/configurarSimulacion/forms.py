from django import forms
from apps.configurarSimulacion.models import Configuracion

class ConfigurarForm(forms.ModelForm):
	class Meta:
		model = Configuracion

		fields=[
		  'temperaturaMax',
		  'temperaturaMin',
		  'humedad',
		  'altitud',
		  'luminosidad',
		  'distanciaLinea',
		]

		labels={
		  'temperaturaMax':'Temperatura maxima',
		  'temperaturaMin':'TemperaturaMinima',
		  'humedad':'Humedad',
		  'altitud':'Altitud',
		  'luminosidad':'Luminosidad',
		  'distanciaLinea':'Distancia entre linea',
		}

	
		widgets={
		  'temperaturaMax':forms.TextInput(attrs={'class':'form-control'}),
		  'temperaturaMin':forms.TextInput(attrs={'class':'form-control'}),
		  'humedad':forms.TextInput(attrs={'class':'form-control'}),
		  'altitud':forms.TextInput(attrs={'class':'form-control'}),
		  'luminosidad':forms.TextInput(attrs={'class':'form-control'}),
		  'distanciaLinea':forms.TextInput(attrs={'class':'form-control'}),

		}