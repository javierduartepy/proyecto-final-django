from django.shortcuts import render
from core.models import Quiz

# Create your views here.
def home(request):
    quiz = Quiz.objects.all()
    return render(request, "juego/home.html", {'quiz': quiz})

def acercade(request):
    return render(request, "juego/acercade.html")

def jugar(request):
    return render(request, "juego/jugar.html")

def ayuda(request):
    return render(request,"juego/ayuda.html")

def miscelanea(request):
    return render(request,"juego/miscelanea.html")
