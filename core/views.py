from django.shortcuts import render
from .models import Integrante, Miscelanea
from django.contrib.auth.decorators import login_required
from juego.models import Puntuacion
# Create your views here.

@login_required(login_url='/login')
def inicio(request):
    puntuaciones = Puntuacion.objects.all()
    return render(request, "core/inicio.html", {'puntuaciones': puntuaciones})

@login_required(login_url='/login')
def ayuda(request):
    return render(request, "core/ayuda.html")

@login_required(login_url='/login')
def miscelanea(request):
    titulos = Miscelanea.objects.all()
    return render(request, "core/miscelanea.html", {'titulos' : titulos})

@login_required(login_url='/login')
def acercade(request):
    integrantes = Integrante.objects.all()
    return render(request, "core/acercade.html", {'integrantes': integrantes})
    
