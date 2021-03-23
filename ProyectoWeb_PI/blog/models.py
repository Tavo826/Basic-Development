from django.db import models
#importando la clase user para relacionarlo a los post
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):

    #Campos que se quiere que tenga el servicio
    nombre = models.CharField(max_length=50) #Cuadro de texto
    #Campos muy usados
    created = models.DateTimeField(auto_now_add=True) #Se guarda la fecha en la que se crea un servicio
    updated = models.DateTimeField(auto_now_add=True) #Se guarda la fecha en la que se modifica un servicio

    #Se crea una clase interna por si se desea determinar el nombre del modelo
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    #Retornando el título del servicio
    def __str__(self):
        return self.nombre
        
class Post(models.Model):

    #Campos que se quiere que tenga el servicio
    titulo = models.CharField(max_length=50) #Cuadro de texto
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True) #Campo de imagen
    #Si el autor elimina su cuenta, los post que este haya publicado también se eliminan (relaciones entre tablas y DB, relación 1 a varios)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #relación varios a varios entre categorías y posts
    categorias = models.ManyToManyField(Categoria)
    #Campos muy usados
    created = models.DateTimeField(auto_now_add=True) #Se guarda la fecha en la que se crea un servicio
    updated = models.DateTimeField(auto_now_add=True) #Se guarda la fecha en la que se modifica un servicio

    #Se crea una clase interna por si se desea determinar el nombre del modelo
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    #Retornando el título del servicio
    def __str__(self):
        return self.titulo