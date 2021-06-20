from django.shortcuts import render
from .models import Cuenta


def seguimiento(request):
    transacciones = Cuenta.objects.all()
    return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones})

