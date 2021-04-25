#from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
#vista basada en clases para devolver una lista de las instancias de un modelo
from django.views.generic.list import ListView
#vista basada en clases para devolver una instancia de un modelo
from django.views.generic.detail import DetailView
#vista para la creación de nuevas páginas
from django.views.generic.edit import CreateView
#Para redireccionar
from django.urls import reverse, reverse_lazy

# Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})

class PageListView(ListView):    
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    #Campo que puede edutar el usuario
    fields = ['title', 'content', 'order']
    
    #redirecciona luego de que se crea la página correctamente
    # def get_success_url(self):
    #     return reverse('pages:pages')

    success_url = reverse_lazy('pages:pages')