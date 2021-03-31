from django.shortcuts import render
#importando el formulario
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    #instanciando el formulario
    formulario_contacto = FormularioContacto()

    #return HttpResponse('Contacto')
    return render(request, 'contacto/contacto.html', {'miFormulario': formulario_contacto})