from django.shortcuts import render
#Importano la ListView
from django.views.generic.list import ListView
#Importando el modelo
from registration.models import Profile
#importando el DtailView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    #Se establece el número de registros por página que se quiere mostrar
    paginate_by = 10

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        #Se accede al perfil desde el username en el path
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
