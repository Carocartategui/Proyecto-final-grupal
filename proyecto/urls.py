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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from AppCoder.views import (PedidosCrear, PedidosList, PedidosActualizar, ProductosList, About)
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls), #-> acer 1234
    path('about', About),  #<- funciona para poner la decripcion de lo que hacela pagina
    path('blog/pedidos/alta', PedidosCrear.as_view(), name="pedidos-crear"), # <- lo rompi tratando de poner la fecha automatica jajaja
    path('blog/pedidos/listado', PedidosList.as_view(), name="pedidos-lista"), #<- funciona
    path('blog/pedidos/<int:pk>/actualizar', PedidosActualizar.as_view(), name="pedidos-actualizar"),
    path('blog/productos/listado', ProductosList.as_view(), name="productos-lista"),  #<- funciona
    path('blog/', include('blog.urls'), name="Home") #<- esto relaciona a los URLS de las funciones creadas en blog.
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

