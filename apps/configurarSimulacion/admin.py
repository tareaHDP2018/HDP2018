from django.contrib import admin
from apps.configurarSimulacion.models import Siembra,Configuracion,FaseCultivo,Simulacion,Usuario

# Register your models here.
admin.site.register(Siembra)
admin.site.register(Configuracion)
admin.site.register(FaseCultivo)
admin.site.register(Simulacion)
@admin.register(Usuario)
class AdminUsuarios(admin.ModelAdmin):
	list_display=('nombre','apellido','password','fechaNacimiento','sexo')