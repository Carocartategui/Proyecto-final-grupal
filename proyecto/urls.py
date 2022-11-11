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
from django.urls import path
from AppCoder.views import (AltaEmpleados, buscarEmpleado, mostrar_empleados, AltaPedidos, mostrar_pedidos,EmpleadosList, EmpleadosCrear, EmpleadosBorrar, EmpleadosActualizar)
from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_index),
    path('empleados/alta', AltaEmpleados.as_view()), #<- ya funciona :)
    path('empleado/buscar', buscarEmpleado.as_view()), # <- ya funciona :)
    path('empleado/listado', mostrar_empleados), # <- ya funciona
    path('pedidos/alta', AltaPedidos.as_view()), # <- funciona
    path('pedidos/listado', mostrar_pedidos), #<- funciona
    path('panel-empleados/', EmpleadosList.as_view()),  #<- funciona
    path('panel-empleados/crear', EmpleadosCrear.as_view()),  #<- funciona
    path('panel-empleados/<int:pk>/borrar', EmpleadosBorrar.as_view()),  #<- funciona
    path('panel-empleados/<int:pk>/actualizar', EmpleadosActualizar.as_view()),  #<- funciona
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