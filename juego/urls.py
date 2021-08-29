from django.urls import path
from juego import views as juego_views

urlpatterns = [
    path('categoria/', juego_views.categoria, name='categoria'),
    path('preguntas/', juego_views.preguntas, name='preguntas'),
    path('opcionCorrecta/', juego_views.opcionCorrecta, name='opcionCorrecta'),
    path('puntuacion/', juego_views.guardarPuntuacion, name='puntuacion'),
    path('juego/<int:categoriaId>/<int:preguntaId>',
         juego_views.juego, name='juego'),

]
