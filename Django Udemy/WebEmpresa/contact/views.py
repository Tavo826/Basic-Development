from django.shortcuts import render, redirect
#importando el formulario
from .forms import ContactForm
from django.urls import reverse
#Librería para correo electrónico
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        #Procesando el formulario
        contact_form = ContactForm(data=request.POST)
        #Comprobando si el formulario es válido
        if contact_form.is_valid():
            #Recuperando los datos
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            #Se envía el email
            email = EmailMessage(
                #asunto
                'La Caffetiera: Nuevo mensaje de contacto',
                #cuerpo
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email,content),
                #email_origen
                'no-contestar@inbox.mailtrap.io',
                #email_destino
                ['9gagigor816@gmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                #Redireccionando a contact
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})