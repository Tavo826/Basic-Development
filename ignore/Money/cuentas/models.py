from django.db import models

# Create your models here.


class Cuenta(models.Model):
    tipo = models.CharField(max_length=20, verbose_name='Tipo')
    cantidad = models.FloatField(verbose_name='Cantidad')
    categoria = models.CharField(max_length=20, verbose_name='Categoría')
    descripcion = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'transacción'
        verbose_name_plural = 'transacciones'
        ordering = ['-created']

    def __str__(self):
        return self.descripcion
