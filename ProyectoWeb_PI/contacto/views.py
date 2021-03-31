from django.shortcuts import render, redirect
#importando el formulario
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    #instanciando el formulario
    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        #Se carga en el formulario la info introducida
        formulario_contacto = FormularioContacto(data=request.POST)
        #Si el formulario es válido
        if formulario_contacto.is_valid():
            #Se guardan los datos
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            
            #Aprovechando la recarga de la página al presionar enviar
            #Se redirecciona a la url de contacto pasando un parámetro

            return redirect('/contacto/?valido')

    #return HttpResponse('Contacto')
    return render(request, 'contacto/contacto.html', {'miFormulario': formulario_contacto})