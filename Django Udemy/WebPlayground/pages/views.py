#from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
#vista basada en clases para devolver una lista de las instancias de un modelo
from django.views.generic.list import ListView
#vista basada en clases para devolver una instancia de un modelo
from django.views.generic.detail import DetailView
#vista para la creación de nuevas páginas, la edición de páginas y eliminar páginas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Para redireccionar
from django.urls import reverse, reverse_lazy
#Cargando el formulario
from .forms import PageForm
#Redireccionando a un usuario no registrado
from django.shortcuts import redirect
#Decorador de identificación
from django.contrib.admin.views.decorators import staff_member_required
#Decorador de métodos
from django.utils.decorators import method_decorator

# Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})


class StaffRequiredMixin(object):
    ''' Este mixin require que el usuario sea miembro del staff '''
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PageListView(ListView):    
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(#StaffRequiredMixin, 
                CreateView):
    model = Page
    #Formato de formulario a mostrar
    form_class = PageForm
    #Campo que puede editar el usuario
    #fields = ['title', 'content', 'order']
    
    #redirecciona luego de que se crea la página correctamente
    # def get_success_url(self):
    #     return reverse('pages:pages')

    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(#StaffRequiredMixin, 
                UpdateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'order']
    #por defecto busca el template de cración, para cambiar eso:
    template_name_suffix = '_update_form'
    #redirecciona luego de que se edita la página
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(#StaffRequiredMixin, 
                DeleteView):
    model = Page
    form_class = PageForm
    #redirecciona luego de que se elimina la página
    success_url = reverse_lazy('pages:pages')