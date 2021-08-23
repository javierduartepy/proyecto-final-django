from django.shortcuts import render
from .models import Integrante, Miscelanea

# Create your views here.


def inicio(request):
    return render(request, "core/inicio.html")


def ayuda(request):
    return render(request, "core/ayuda.html")


def miscelanea(request):
    titulos = Miscelanea.objects.all()
    return render(request, "core/miscelanea.html", {'titulos' : titulos})


def acercade(request):
    integrantes = Integrante.objects.all()
    return render(request, "core/acercade.html", {'integrantes': integrantes})
    
