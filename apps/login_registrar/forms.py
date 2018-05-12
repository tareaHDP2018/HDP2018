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

class RegistrarForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput,max_length=8)
	fechaNacimiento=forms.DateField(label='Fecha de nacimiento',widget = forms.SelectDateWidget(years=year))
	class Meta:
		model=Usuario
		fields= '__all__'