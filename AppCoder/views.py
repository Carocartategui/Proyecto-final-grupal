from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mi Primer App")

def saludo_dos(request):
    return HttpResponse("Este es otro saludo")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def mostrar_mi_template(request):
    return render (request, "AppCoder/index.html") 