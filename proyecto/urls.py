"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppCoder.views import (AltaEmpleados, buscarEmpleado, mostrar_empleados, AltaPedidos, mostrar_pedidos,EmpleadosList, EmpleadosCrear, EmpleadosBorrar, EmpleadosActualizar, ProductosList, About, Home, PedidosList, PedidosCrear, PedidosActualizar)


urlpatterns = [
    path('admin/', admin.site.urls), #-> acer 1234
    path('about', About),  #<- funciona para poner la decripcion de lo que hacela pagina
    path('home', Home),  #<- funciona para el home...(que me imagino que es lo mismo que el blog?)
    path('empleados/alta', AltaEmpleados.as_view()), #<- ya funciona :)
    path('empleado/buscar', buscarEmpleado.as_view()), # <- ya funciona :)
    path('empleado/listado', mostrar_empleados), # <- ya funciona
    path('blog/pedidos/alta', AltaPedidos.as_view()), # <- lo rompi tratando de poner la fecha automatica jajaja
    path('blog/pedidos/listado', mostrar_pedidos), #<- funciona
    path('panel-empleados/', EmpleadosList.as_view(), name="empleados-lista"),  #<- funciona
    path('panel-empleados/crear', EmpleadosCrear.as_view(), name="empleados-crear"), #<- funciona
    path('panel-empleados/<int:pk>/borrar', EmpleadosBorrar.as_view(), name="empleados-borrar"),  #<- funciona
    path('panel-empleados/<int:pk>/actualizar', EmpleadosActualizar.as_view(), name="empleados-actualizar"),  #<- funciona
    path('blog/productos/listado', ProductosList.as_view(), name="productos-lista"),  #<- funciona
    path('blog/', include('blog.urls')) #<- esto relaciona a los URLS de las funciones creadas en blog.
]




"""    

Borre los path que no usamos mas (Matias)
    path('hola-mundo/saludar', saludo),
    path('hola-mundo/saludo_dos', saludo_dos),
    path('saludar_a/<nombre>', saludar_a),
    path('mostrar-mi-template/', mostrar_mi_template),
    path('saludar/', index),
    path('mostrar-notas/', index_tres),
    path('mi-familia/', monstrar_familiares),
    
    """