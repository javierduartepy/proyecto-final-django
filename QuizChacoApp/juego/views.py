from django.shortcuts import render
from core.models import Quiz

# Create your views here.


def juego(request):
    quiz = Quiz.objects.order_by('-pk')[0]
    return render(request, "juego/juego.html", {'quiz': quiz})


def categoria(request):
    categoria = request.GET.get('categoria', None)
    print(categoria)
    return render(request, "core/inicio.html", {'categoria': categoria})
