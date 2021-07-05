from django.shortcuts import redirect, render
from .models import Cuenta
from .forms import CuentaForm


def seguimiento(request):

    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form = form.save()
            transacciones = Cuenta.objects.all()
            return redirect(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form})
        else:
            form = CuentaForm()
    
    transacciones = Cuenta.objects.all()

    return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form})


def detallesSeguimiento(request, transaction_id):
    form = CuentaForm()
    return render(request, 'cuentas/cuentas_info.html', {'form': form})
