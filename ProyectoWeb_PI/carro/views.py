from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

#redirect para redireccionar al generar algún cambio


# Create your views here.

def agregar_producto(request, producto_id):
    
    #Se crea el carro
    carro = Carro(request)
    
    #Obteniendo el producto
    producto = Producto.objects.get(id=producto_id)

    #Agregando el producto al carro
    carro.agregar(producto=producto)

    #Redireccionando a la tienda
    return redirect('Tienda')

def eliminar_producto(request, producto_id):
    
    #Se crea el carro
    carro = Carro(request)
    
    #Obteniendo el producto
    producto = Producto.objects.get(id=producto_id)

    #Eliminando el producto del carro
    carro.eliminar(producto=producto)

    #Redireccionando a la Tienda
    return redirect('Tienda')

def restar_producto(request, producto_id):
    
    #Se crea el carro
    carro = Carro(request)
    
    #Obteniendo el producto
    producto = Producto.objects.get(id=producto_id)

    #Restando el producto al carro
    carro.restar_producto(producto=producto)

    #Redireccionando a la Tienda
    return redirect('Tienda')

def limpiar_carro(request, producto_id):
    
    #Se crea el carro
    carro = Carro(request)
    
    #Limpiando el carro
    carro.limpiar_carro()

    #Redireccionando a la Tienda
    return redirect('Tienda')
