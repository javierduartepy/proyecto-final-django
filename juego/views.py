from django.shortcuts import render
from .models import Opcion, Pregunta

# Create your views here.


def juego(request, categoria, id):
    pregunta = Pregunta.objects.get(pk=id)
    opciones = Opcion.objects.raw(
        f"SELECT * FROM opciones WHERE pregunta_id='{id}'")
    # mensaje:  incorrecto, casi casi, perfecto, lo tienes, tiempo fuera
    return render(request, "juego/juego.html", {'pregunta': pregunta, 'categoria': categoria, 'opciones': opciones})


def categoria(request):
    categoria = request.GET.get('categoria', None)
    print(categoria)
    return render(request, "core/inicio.html", {'categoria': categoria})
