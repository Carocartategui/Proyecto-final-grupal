from django.db import models

# Create your models here.

from django.db import models


class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_documento = models.IntegerField()
    numero_de_telefono = models.IntegerField()
    E_Mail = models.CharField(max_length=100)
    Contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.direccion}, {self.numero_documento}, {self.numero_de_telefono}, {self.E_Mail}, {self.Contrasena}, {self.id}"

