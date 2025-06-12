from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/autor/', views.crear_autor, name='crear_autor'),
    path('crear/categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear/entrada/', views.crear_entrada, name='crear_entrada'),
    path('buscar/', views.buscar, name='buscar'),
]
