from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
from juego import views as juego_views

urlpatterns = [
    path('', core_views.inicio, name='inicio'),
    path('inicio/', core_views.inicio, name='inicio'),
    path('acercade/', core_views.acercade, name='acercade'),
    path('juego/', juego_views.juego, name='juego'),
    path('ayuda/', core_views.ayuda, name='ayuda'),
    path('miscelanea/', core_views.miscelanea, name='miscelanea'),
    path('categoria/', juego_views.categoria, name='categoria'),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
