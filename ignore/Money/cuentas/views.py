from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Cuenta
from .forms import CuentaForm


def seguimiento(request):

    form = CuentaForm()
    transacciones = Cuenta.objects.all

    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            total = form['cantidad'].value()
            # saldo = saldoTotal(total)

            print(form['tipo'].value())

            return redirect(reverse('seguimiento'))  # Reset formulario

        else:
            print('Invalid form')

    return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form, 'saldo': 100})


def detallesSeguimiento(request, pk):

    cuenta = get_object_or_404(Cuenta, pk=pk)

    if request.method == 'POST':

        if 'botonEliminar' in request.POST:
            cuenta.delete()

        else:
            form = CuentaForm(request.POST, instance=cuenta)
            if form.is_valid():
                form.save()

        return redirect(reverse('seguimiento'))

    else:
        form = CuentaForm(instance=cuenta)

    return render(request, 'cuentas/cuentas_info.html', {'cuenta': cuenta, 'form': form})


def saldoTotal(total, operacion=1):

    saldo = 300000

    if operacion:
        saldo += int(total)
    else:
        saldo -= int(total)

    return saldo
