from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crea_tablero', views.tablero, name='crea_tablero'),

]