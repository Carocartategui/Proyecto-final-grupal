from django.db import models

# Create your models here.

from django.db import models


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

