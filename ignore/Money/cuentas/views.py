from django.shortcuts import redirect, render
from .models import Cuenta
from .forms import CuentaForm


def seguimiento(request):

    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():

            print('Tipo: ', form['tipo'].value())
            print('Monto: ', form['cantidad'].value())
            print('Categoría: ', form['categoria'].value())
            print('Descripcion: ', form['descripcion'].value())            

            form = form.save()
            transacciones = Cuenta.objects.all
            return redirect(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form})
        else:
            print('Invalid form')
    else:
        form = CuentaForm()
    
    transacciones = Cuenta.objects.all

    return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form})


def detallesSeguimiento(request, transaction_id):
    form = CuentaForm()
    return render(request, 'cuentas/cuentas_info.html', {'form': form})
