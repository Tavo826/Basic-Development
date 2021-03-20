from django.contrib import admin
#Se importa del archivo models.py la clase servicio
from .models import Servicio

# Register your models here.

#Clase para que aparezcan created y updated en el panel de administración
class ServicioAdmin(admin.ModelAdmin):
    #Son de solo lectura
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)