from django.contrib import admin
from .models import Cuenta

# Register your models here.


class CuentaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tipo', 'cantidad', 'categoria', 'descripcion', 'created')
    ordering = ('-created',)
    search_fields = ('tipo', 'categoria', 'cantidad')
    date_hierarchy = 'created'
    list_filter = ('tipo', 'categoria')


admin.site.register(Cuenta, CuentaAdmin)
