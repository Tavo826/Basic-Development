from django.db import models

# Create your models here.

class CategoriaProd(models.Model):

    #Campos requeridos
    nombre = models.CharField(max_length=50)
    #momento de creación
    created = models.DateTimeField(auto_now_add=True)
    #Momento en que se modifica
    updated = models.DateTimeField(auto_now_add=True)

    #Nombre en singular y en plural
    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'

    #Devolviendo el nombre de la categoría
    def __str__(self):
        return self.nombre

class Producto(models.Model):

    #Campo de la tabla de productos en la base de datos
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre