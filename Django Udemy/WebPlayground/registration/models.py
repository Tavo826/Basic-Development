from django.db import models
from django.contrib.auth.models import User
#Función para decorar la señal
from django.dispatch import receiver
#importando la forma de activar la señal
from django.db.models.signals import post_save

# Create your models here.


#Función para sobreescribir la imagen del avatar
def custom_upload_to(instance, filename):
    #recuperando la instancia antes de ser guardada
    old_instance = Profile.objects.get(pk=instance.pk)
    #Eliminando al avatar anterior
    old_instance.avatar.delete()
    return 'profiles/' + filename


#Modelo para completar el registro del usuario
class Profile(models.Model):
    #Relación para relacionar al usuario con el perfil (One to One)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Se guarda la imagen más reciente del perfil del usuario
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']


#Señal que crea automáticamente el perfil de cada usuario luego de registrarse
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    #Como se activa cada que se guarda el usuario, se comprueba si es la primera vez que se guarda
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('Se creó el usuario y su perfil asociado')


