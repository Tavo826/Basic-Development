from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#importando el modelo
from .models import Profile

#Extendiendo el formulario para que valide el email del usuario

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 max, debe ser válido')

    class Meta:
        model = User
        #Se pasa el campo email que se creó
        fields = ('username', 'email', 'password1', 'password2')
        
        #No tiene sentido cambiar acá los widgets (se estropean los que están por defecto)
        #mejor modificarlos en tiempo de ejecución

    #Se añade una validación para que el email sea único para cada usuario
    def clean_email(self):
        #Se recupera el email
        email = self.cleaned_data.get('email')
        #Si existe el correo que se intenta registrar
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra registrado')
        return email


#Formulario para mejorar el perfil
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        #Añadiendo los estilos
        widgets = {
            #Permite limpiar el campo del avatar
            'avatar': forms.ClearableFileInput(attrs={'class':'forms-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'forms-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'forms-control mt-3', 'placeholder':'Enlace'}),
        }

#Formulario para editar el correo electrónico del usuario
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 max, debe ser válido')

    class Meta:
        model = User
        fields = ['email']

    #Se añade una validación para que el email sea único para cada usuario
    def clean_email(self):
        #Se recupera el email
        email = self.cleaned_data.get('email')
        #Si se ha modificado el email
        if 'email' in self.changed_data:
            #Si existe el correo que se intenta registrar
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya se encuentra registrado')
        return email