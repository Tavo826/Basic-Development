from django.shortcuts import render
#Importando los servicios de la clase Servicios
from servicios.models import Servicio


# Create your views here.

def servicios(request):

    #Cargando todos los servicios
    servicios = Servicio.objects.all()

    #return HttpResponse('Servicios')
    return render(request, 'servicios/servicios.html', {'servicios': servicios})