#Se pretende que el diccionario creado extienda el contexto global
#para poder usar la clave 'Test' como una variable en todos los templates

# def context_dict(request):
#     #Se crea un diccionario de prueba
#     ctx = {'Test': 'hola'}
#     return ctx

from .models import Link

def context_dict(request):
    ctx = {}
    links = Link.objects.all()
    
    for link in links:
        ctx[link.key] = link.url
    return ctx