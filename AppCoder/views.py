from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Empleados, Pedidos
from AppCoder.forms import EmpleadosForm, buscar_empleado, PedidosForm
from django.views import View
from django.views.generic import ListView

def saludo(request):
    return HttpResponse("Hola Mi Primer App")

def saludo_dos(request):
    return HttpResponse("Este es otro saludo")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def mostrar_mi_template(request):
    return render (request, "AppCoder/index.html") 


def Home(request):
    return render (request, "AppCoder/home.html") 

"""Busqueda Empleados"""

class buscar_Empleado(View):

    form_class = buscar_empleado
    template_name = 'AppCoder/buscar_empleado.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_empleados = Empleados.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_empleados':lista_empleados})
        return render(request, self.template_name, {"form": form})

"""Formulario de ingreso de empleados"""

class AltaEmpleados(View):

    form_class = EmpleadosForm
    template_name = 'AppCoder/alta_empleado.html'
    initial = {"nombre":"", "apellido":"", "direccion":"", "numero_documento":"", "numero_de_telefono":"", "e_mail":"", "contrasena":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el empleado {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


"""mostrar todos los empleados"""
def mostrar_empleados(request):
  lista_empleados = Empleados.objects.all()
  return render(request, "AppCoder/empleados.html", {"lista_empleados": lista_empleados})

"""Formulario de ingreso de pedidos"""

class AltaPedidos(View):

    form_class = PedidosForm
    template_name = 'AppCoder/alta_pedido.html'
    initial = {'nombre_cliente':"", 'empleado':"", 'pedido':"", 'estado':"", 'fecha':""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el pedido de {form.cleaned_data.get('nombre_cliente')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


"""Mostrar todos los pedidos"""

def mostrar_pedidos(request):
  lista_pedidos = Pedidos.objects.all()
  return render(request, "AppCoder/pedidos.html", {"lista_pedidos": lista_pedidos})


"""prueba empleados list"""

class EmpleadosList(ListView):
  model = Empleados