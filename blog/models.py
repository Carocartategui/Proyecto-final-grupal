from django.db import models
# Create your models here.

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)