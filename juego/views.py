from django.shortcuts import render
from .models import Pregunta

# Create your views here.


def juego(request):
    pregunta = Pregunta.objects.order_by('-pk')[0]
    return render(request, "juego/juego.html", {'pregunta': pregunta})


def categoria(request):
    categoria = request.GET.get('categoria', None)
    print(categoria)
    return render(request, "core/inicio.html", {'categoria': categoria})
