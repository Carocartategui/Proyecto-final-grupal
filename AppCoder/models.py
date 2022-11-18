from django.db import models

# Create your models here.

class Pedidos(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    empleado = models.CharField(max_length=100) #<- esto estaria bueno que se autocomplete cuando se loguea el empleado
    pedido = models.CharField(max_length=200)
    estado= models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)  #<- cambiado a automatico """DateTimeField(auto_created=True)"""

    def __str__(self):
        return f"{self.nombre_cliente}, {self.empleado}, {self.pedido}, {self.estado}, {self.fecha}, {self.id}"


class Productos(models.Model):
    nombre_producto = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=150) 
    descripcion = models.CharField(max_length=150) 
    codigo_producto = models.IntegerField()
    

    def __str__(self):
        return f"{self.nombre_producto}, {self.ingredientes}, {self.descripcion}, {self.codigo_producto}, {self.id}"


class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_documento = models.IntegerField()
    numero_de_telefono = models.IntegerField()
    e_mail = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.direccion}, {self.numero_documento}, {self.numero_de_telefono}, {self.e_mail}, {self.contrasena}, {self.id}"

