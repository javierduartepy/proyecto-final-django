from django.shortcuts import render
from core.models import Quiz

# Create your views here.

# mensaje:  incorrecto, casi casi, perfecto, lo tienes, tiempo fuera


def juego(request, categoria, id):
    quiz = Quiz.objects.order_by('-pk')[0]
    return render(request, "juego/juego.html", {'quiz': quiz, 'categoria': categoria})


def categoria(request):
    categoria = request.GET.get('categoria', None)
    print(categoria)
    return render(request, "core/inicio.html", {'categoria': categoria})
