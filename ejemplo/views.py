from django.shortcuts import render
from ejemplo.models import Familiar


def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def index(request):
    return render(request, "ejemplo/saludar.html")

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8]}
    )

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
