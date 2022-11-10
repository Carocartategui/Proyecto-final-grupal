from django.db import models

# Create your models here.

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

class Pedidos(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    empleado = models.CharField(max_length=100) #<- esto estaria bueno que se autocomplete cuando se loguea el empleado
    pedido = models.CharField(max_length=200)
    estado= models.CharField(max_length=200)
    fecha = models.CharField(max_length=200) #<- esto estaria bueno que se ponga automatico hr fecha

    def __str__(self):
        return f"{self.nombre_cliente}, {self.empleado}, {self.pedido}, {self.estado}, {self.fecha}, {self.id}"

