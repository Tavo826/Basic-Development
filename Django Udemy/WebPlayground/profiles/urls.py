from django.urls import path
from .views import ProfileListView, ProfileDetailView

#Se hace como tupla para asignarle un nombre a la aplicación y 
#acceder a las urls como profiles:url
profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], 'profiles')