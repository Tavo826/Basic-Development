from django.shortcuts import render, HttpResponse

# Create your views here.

#Ventanas del menú
def home(request):

    #return HttpResponse('Home')
    return render(request, 'ProyectoWebApp/home.html')
