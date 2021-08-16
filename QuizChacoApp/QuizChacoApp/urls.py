from django.contrib import admin
from django.urls import path
from core import views as core_views
from juego import views as juego_views

urlpatterns = [
    path('', core_views.inicio, name='inicio'),
    path('inicio/', core_views.inicio, name='inicio'),
    path('acercade/', core_views.acercade, name='acercade'),
    path('juego/', juego_views.juego, name='juego'),
    path('ayuda/', core_views.ayuda, name='ayuda'),
    path('miscelanea/', core_views.miscelanea, name='miscelanea'),
    path('admin/', admin.site.urls)
]
