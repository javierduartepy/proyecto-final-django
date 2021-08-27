from django.shortcuts import render
from .models import Integrante, Miscelanea
from juego.models import Categoria
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def inicio(request):
    print("id", request.user.id)
    return render(request, "core/inicio.html")


# @login_required(login_url='/login')
# def inicio(request):
#     categorias = Categoria.objects.order_by('pk')
#     opCategorias = []
#     for c in categorias:
#         opCategorias.append(
#             {'id': c.id, 'nombre': c.nombre, 'key': 'cat' + str(c.id)})
#     return render(request, "core/inicio.html", {'categorias': opCategorias})


@login_required(login_url='/login')
def ayuda(request):
    return render(request, "core/ayuda.html")


@login_required(login_url='/login')
def miscelanea(request):
    titulos = Miscelanea.objects.all()
    return render(request, "core/miscelanea.html", {'titulos': titulos})


@login_required(login_url='/login')
def acercade(request):
    integrantes = Integrante.objects.all()
    return render(request, "core/acercade.html", {'integrantes': integrantes})
