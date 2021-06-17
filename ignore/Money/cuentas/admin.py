from django.contrib import admin
from .models import Cuenta

# Register your models here.


class CuentaAdmin(admin.ModelAdmin):

    readonly_fields = ('updated',)


admin.site.register(Cuenta, CuentaAdmin)
