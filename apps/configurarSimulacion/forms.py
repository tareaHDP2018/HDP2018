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
		  'temperaturaMin':'Temperatura mainima',
		  'humedad':'Humedad',
		  'luminosidad':'Luminosidad',
		  'distanciaLinea':'Distancia entre lineas',
       }
		widgets={
		  'temperaturaMax':forms.NumberInput(attrs={'class':'form-control'}),
		  'temperaturaMin':forms.NumberInput(attrs={'class':'form-control'}),
		  'humedad':forms.NumberInput(attrs={'class':'form-control'}),
		  'altitud':forms.NumberInput(attrs={'class':'form-control'}),
		  'luminosidad':forms.NumberInput(attrs={'class':'form-control'}),
		  'distanciaLinea':forms.NumberInput(attrs={'class':'form-control'}),
		}