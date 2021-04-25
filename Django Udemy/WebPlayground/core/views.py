from django.shortcuts import render
#importando la librería para CBV
from django.views.generic.base import TemplateView

# Create your views here.


# def home(request):
#     return render(request, 'core/home.html')

# def sample(request):
#     return render(request, 'core/sample.html')


#Como estas vistas solamente devuelven un template se usa 'TemplateView'

class HomePageView(TemplateView):
    template_name = 'core/home.html'

    #Sobreescribiendo el diccionario de contexto
    # def get_context_data(self, **kwargs):
    #     #Se recupera el diccionario de contexto llamando a la propia función
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Web Playground'
    #     return context

    #Sobreescribiendo el método get de la vista
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Mi Web Playground'})

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'


