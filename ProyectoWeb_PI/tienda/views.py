from django.shortcuts import render
#importando el producto
from .models import Producto

# Create your views here.

def tienda(request):

    productos = Producto.objects.all()

    #return HttpResponse('Tienda')
    return render(request, 'tienda/tienda.html', {'productos': productos})