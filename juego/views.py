from django.shortcuts import render, redirect
from .models import Categoria, Opcion, Pregunta, Puntuacion
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


@login_required(login_url='/login')
def juego(request, categoriaId, preguntaId):
    categoria = Categoria.objects.get(pk=categoriaId)
    pregunta = Pregunta.objects.get(pk=preguntaId)
    opciones = Opcion.objects.raw(
        f"SELECT * FROM opciones WHERE pregunta_id='{preguntaId}'")

    return render(request, "juego/juego.html", {'pregunta': pregunta, 'categoria': categoria, 'opciones': opciones})


def categoria(request):
    preguntas = None
    categoriaId = request.GET.get('categoriaId', None)
    if Pregunta.objects.filter(categoria_id=categoriaId).exists():
        preguntas = Pregunta.objects.filter(
            categoria_id=categoriaId).order_by('pk').values()
    json_response = {'preguntas': list(preguntas)}
    return JsonResponse(json_response)


def opcionCorrecta(request):
    opciones = None
    preguntaId = request.GET.get('preguntaId', None)
    if Opcion.objects.filter(pregunta_id=preguntaId).exists():
        opciones = Opcion.objects.filter(pregunta_id=preguntaId).values()

    json_response = {'opciones': list(opciones)}
    return JsonResponse(json_response)


def preguntas(request):
    preguntas = None
    categoriaId = request.GET.get('categoriaId', None)
    preguntaId = request.GET.get('preguntaId', None)
    siguientesPreguntas = []
    if Pregunta.objects.filter(categoria_id=categoriaId).exists():
        preguntas = list(Pregunta.objects.filter(
            categoria_id=categoriaId).values())
        preguntasFiltrasxCategoria = Pregunta.objects.filter(
            categoria_id=categoriaId)
        totalElementos = len(list(preguntas))

        # Aca tenia que enviar todas las preguntas que faltan menos la pregunta actual
        # pero tuve que enviar un arreglo de ids de preguntas porque el objeto horrible de django
        # no me dejo iterar el arreglo, se va hacer un workaround con JS hasta encontrar una solucion mejor
        for index, item in enumerate(preguntasFiltrasxCategoria):
            siguientesPreguntas.append(item.id)

    json_response = {'preguntas': preguntas,
                     'siguientesPreguntas': siguientesPreguntas}
    return JsonResponse(json_response)


def guardarPuntuacion(request):
    if request.method == 'POST':
        datosDeLaPuntuacion = request.POST
        print(datosDeLaPuntuacion)
        # puntuacion = Puntuacion(usuario=1, categoria=1, nivel= 1, cantidad_preguntas=15, cantidad_respuestas=2)
        # puntuacion.save()
    return redirect('inicio')
