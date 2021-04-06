from django.shortcuts import render, redirect
#importando el formulario
from .forms import FormularioContacto
#importando la clase para enviar el correo
from django.core.mail import EmailMessage

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

            email = EmailMessage(subject='Mensaje desde app Django'
                                , body='Usuario: {} correo: {} \nmensaje: {}'.format(nombre, email, contenido)
                                , from_email=''
                                , to=['9gagigor816@gmail.com']
                                , reply_to=[email])

            try:
                email.send()
            
                #Aprovechando la recarga de la página al presionar enviar
                #Se redirecciona a la url de contacto pasando un parámetro

                return redirect('/contacto/?valido')
            
            except:

                return redirect('/contacto/?novalido')
                
    #return HttpResponse('Contacto')
    return render(request, 'contacto/contacto.html', {'miFormulario': formulario_contacto})