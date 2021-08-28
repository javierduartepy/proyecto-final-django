from django.urls import path
from juego import views as juego_views

urlpatterns = [
    path('categoria/', juego_views.categoria, name='categoria'),
    path('juego/<int:categoriaId>/<int:preguntaId>',
         juego_views.juego, name='juego'),

]
