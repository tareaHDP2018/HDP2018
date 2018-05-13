from django import forms
from apps.configurarSimulacion.models import Simulacion,Configuracion

class SimulacionForm(forms.ModelForm):
 	class Meta:
 		model = Simulacion

 		fields=[

 		 'nombre',
 		 'lineaSiembra',
 		 'faseCultivo',

 		]

 		widgets={
 		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		'lineaSiembra':forms.NumberInput(attrs={'class':'form-control'}),
 		'faseCultivo':forms.CheckboxSelectMultiple(attrs={'class':'Checkbox'}),
 		}


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
		  'temperaturaMax':forms.NumberInput(attrs={'class':'form-control','value':'10'}),
		  'temperaturaMin':forms.NumberInput(attrs={'class':'form-control','value':'25'}),
		  'humedad':forms.NumberInput(attrs={'class':'form-control','value':'25'}),
		  'altitud':forms.NumberInput(attrs={'class':'form-control','value':'250'}),
		  'luminosidad':forms.NumberInput(attrs={'class':'form-control','value':'25'}),
		  'distanciaLinea':forms.NumberInput(attrs={'class':'form-control','value':'25'}),
		}