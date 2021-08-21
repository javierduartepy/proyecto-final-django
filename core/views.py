from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "core/inicio.html")


def ayuda(request):
    return render(request, "core/ayuda.html")


def miscelanea(request):
    return render(request, "core/miscelanea.html")


def acercade(request):
    return render(request, "core/acercade.html")
