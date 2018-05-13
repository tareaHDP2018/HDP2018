from django import forms
from apps.configurarSimulacion.models import Simulacion

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
		'lineaSiembra':forms.TextInput(attrs={'class':'form-control'}),
 		'faseCultivo':forms.CheckboxSelectMultiple(attrs={'class':'Checkbox'}),
 		}