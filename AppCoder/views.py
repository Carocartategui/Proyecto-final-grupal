from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Empleados, Pedidos, Productos
from AppCoder.forms import EmpleadosForm, buscar_empleado, PedidosForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required


"""Mostrar todos los pedidos"""

def mostrar_pedidos(request):
  lista_pedidos = Pedidos.objects.all()
  return render(request, "AppCoder/pedidos.html", {"lista_pedidos": lista_pedidos})

"""prueba productos list"""

class ProductosList(ListView):
  model = Productos

"""pagina de about"""

def About(request):
    return render (request, "AppCoder/about.html") 


"""lista de pedidos"""

class PedidosList(ListView):
  model = Pedidos


"""create view de pedidos"""

class PedidosCrear(CreateView):
  model = Pedidos
  success_url = "/blog/pedidos/listado"
  fields = ["nombre_cliente", "empleado", "pedido", "estado", "fecha"]

"""update view de pedidos"""

class PedidosActualizar(UpdateView):
  model = Pedidos
  success_url = "/blog/pedidos/listado"
  fields = ["nombre_cliente", "empleado", "pedido", "estado", "fecha"]


  