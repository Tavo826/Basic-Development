from django.shortcuts import redirect, render
from .models import Cuenta
from .forms import CuentaForm


def seguimiento(request):
    form = CuentaForm(request.POST)
    if request.method == 'GET':
        transacciones = Cuenta.objects.all()

    elif request.method == 'POST':
        if form.is_valid():
            new_transaction = form.save()

            # return redirect()

    return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form})


def detallesSeguimiento(request, transaction_id):
    form = CuentaForm()
    return render(request, 'cuentas/cuentas_info.html', {'form': form})
