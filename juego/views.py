from django.shortcuts import render
from .models import Categoria, Opcion, Pregunta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


@login_required(login_url='/login')
def juego(request, categoria, preguntaId):
    pregunta = Pregunta.objects.get(pk=id)
    opciones = Opcion.objects.raw(
        f"SELECT * FROM opciones WHERE pregunta_id='{id}'")
    # mensaje:  incorrecto, casi casi, perfecto, lo tienes, tiempo fuera
    return render(request, "juego/juego.html", {'pregunta': pregunta, 'categoria': categoria, 'opciones': opciones})


def categoria(request):
    preguntas = None
    categoriaId = request.GET.get('categoriaId', None)
    categoria = Categoria.objects.get(pk=categoriaId)
    if Pregunta.objects.filter(categoria_id=categoriaId).exists():
        preguntas = Pregunta.objects.filter(categoria_id=categoriaId).values()
    json_response = {'preguntas': list(preguntas)}
    return JsonResponse(json_response)
