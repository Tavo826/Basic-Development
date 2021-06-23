from django.shortcuts import render
from .models import Cuenta


def seguimiento(request):
    if request.method == 'GET':
        transacciones = Cuenta.objects.all()
        return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones})

    elif request.method == 'POST':
        pass


def detallesSeguimiento(request, transaction_id):
    return render(request, 'cuentas/cuentas_info.html')
