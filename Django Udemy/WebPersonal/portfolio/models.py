from django.db import models

# Create your models here.

#esta clase representa una tabla en la base de datos
class Project(models.Model):
    
    title = models.CharField(max_length=20, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects') #projects se crea dentro de media
    link = models.URLField(verbose_name='Enlace', null=True, blank=True)
    #Se ejecuta una vez al crearse
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    #Se ejecuta cada que se actualiza la instancia
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
