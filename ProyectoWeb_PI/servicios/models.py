from django.db import models

# Create your models here.

#Se crea en la base de datos una tabla para guardar los datos del servicio
#Para hacer esta tabla se debe crear un modelo
#Realizando un mapeo ORM, se crea un modelo y dentro de ese modelo se crea una clase con los atributos de la tabla
#Cada atributo corresponde a un dato de la tabla donde se guarda la información de cada servicio

#El mapeo ORM (mapeo de objetos relacionales) consiste en crear un objeto que representa un objeto en la tabla con sus propiedades
#Esto con el fin de manipular desde python tablas con campos y registros

class Servicio(models.Model):

    #Campos que se quiere que tenga el servicio
    titulo = models.CharField(max_length=50) #Cuadro de texto
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') #Campo de imagen
    #Campos muy usados
    created = models.DateTimeField(auto_now_add=True) #Se guarda la fecha en la que se crea un servicio
    updated = models.DateTimeField(auto_now_add=True) #Se guarda la fecha en la que se modifica un servicio

    #Se crea una clase interna por si se desea determinar el nombre del modelo
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    #Retornando el título del servicio
    def __str__(self):
        return self.titulo