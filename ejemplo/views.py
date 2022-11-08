from django.shortcuts import render


def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def index(request):
    return render(request, "ejemplo/saludar.html")

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8]}
    )
