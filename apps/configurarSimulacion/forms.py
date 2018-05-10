from django import forms
from apps.configurarSimulacion.models import Configuracion

class ConfigurarForms(forms.ModelForm):
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
		  'temperaturaMin':'Temperatura minima',
		  'humedad':'Humedad',
		  'altitud':'Altitud',
		  'luminosidad':'Luminosidad',
		  'distanciaLinea':'Distancia entre lienas',
		}

		widgets={
		  'temperaturaMax':forms.TextInput(attrs={'class':'form-control'}),
		  'temperaturaMin':forms.TextInput(attrs={'class':'form-control'}),
		  'humedad':forms.TextInput(attrs={'class':'form-control'}),
		  'altitud':forms.TextInput(attrs={'class':'form-control'}),
		  'luminosidad':forms.TextInput(attrs={'class':'form-control'}),
		  'distanciaLinea':forms.TextInput(attrs={'class':'form-control'}),

		}