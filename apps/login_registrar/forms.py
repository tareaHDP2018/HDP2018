from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.configurarSimulacion.models import Usuario


year=('1930','1931','1932','1933','1934','1935','1936','1937','1938','1939',
	'1940','1941','1942','1943','1944','1945','1946','1947','1948','1949',
	'1950','1951','1952','1953','1954','1955','1956',
	'1957','1958','1959','1961','1962','1963','1964','1965',
	'1966','1967','1968','1969','1970','1971','1972','1973','1974','1975',
	'1976','1977','1978','1979',
	'1980','1981','1982','1969','1983','1984','1985','1986','1987','1988','1989',
	'1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
	'2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
	)
genero=(('masculino','masculino')
	,('femenino','femenino'))

class RegistrarForm(forms.ModelForm):
	nombre_usuario=forms.CharField(label='nombre de usuario',widget=forms.TextInput(attrs={'placeholder':'su nombre de usuario aqui','class':'form-control form-control-sm'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}),max_length=8)
	nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
	apellido=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
	fechaNacimiento=forms.DateField(label='Fecha de nacimiento',widget = forms.SelectDateWidget(years=year,attrs={'class':'form-control','id':'fecha'}))
	sexo=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=genero)
	class Meta:
		model=Usuario
		fields= '__all__'

class LoginForm(forms.ModelForm):
	nombre_usuario=forms.CharField(label='nombre de usuario',widget=forms.TextInput(attrs={'placeholder':'su nombre de usuario aqui','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=8)
	class Meta:                                                     
		model=Usuario
		fields= ('nombre_usuario','password')
