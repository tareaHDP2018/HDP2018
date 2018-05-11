from django import forms
from apps.configurarSimulacion.models import Simulacion

class SimulacionForm(forms.ModelForm):
 	class Meta:
 		model = Simulacion

 		fields=[
 		 'faseCultivo',
 		]

 		labels={
 		'faseCultivo':'Fases de cultivo'
 		}

 		widgets={
 		'faseCultivo':forms.CheckboxSelectMultiple(attrs={'class':'Checkbox'}),
 		}