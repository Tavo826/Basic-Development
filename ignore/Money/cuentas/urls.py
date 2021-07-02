from django.urls import path
from . import views

urlpatterns = [
    path('', views.seguimiento, name='seguimiento'),
    path('cuenta/<int:transaction_id>/', views.detallesSeguimiento, name='detalles'),
]
