#Cargando el formulario por defecto de django
#from django.contrib.auth.forms import UserCreationForm
#Cargando el formulario luego de crear el campo email
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
#Para acceder a los tipos de widgets
from django import forms
#Cargando el TemplateView (para prueba)
# from django.views.generic.base import TemplateView
#Cargando el UpdateView
from django.views.generic.edit import UpdateView
#Importando decorador para comprobar que el usuario está autentificado
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#Importando el modelo
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    #Carga el formulario importado
    #form_class = UserCreationForm
    form_class = UserCreationFormWithEmail
    #Redirecciona a login luego de hacer el registro
    #success_url = reverse_lazy('login')
    #se define el template
    template_name = 'registration/signup.html'

    #Reescribiendo el método succes_url para mostrar mensaje de registro correcto
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    #Modificando el formulario de registro    
    def get_form(self, form_class=None):
        #Primero se debe recuperar
        form = super(SignUpView, self).get_form()
        #Modificando los widgets
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        #Se crea el widget para el email
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Dirección de email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'})
        return form


#Se crea una página para editar el perfil (como templateview para prueba)
# @method_decorator(login_required, name='dispatch')
# class ProfileUpdate(TemplateView):
#     template_name = 'registration/profile_form.html'

#Se crea la página para editar el perfil
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    #Se carga el formulario con el modelo
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    #Recuperando al id del usuario autenticado
    def get_object(self):
        #Lo busca o lo crea
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

#Se crea la página para editar el correo
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    #Se carga el formulario con el modelo
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    #Recuperando el usuario
    def get_object(self):        
        
        return self.request.user

    #Sobreescribiendo el widget
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        #Modificando los widgets
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})

        return form