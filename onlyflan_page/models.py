from django.db import models
from django.contrib.auth.models import AbstractUser

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    destacada = models.BooleanField(default=False)
    activado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    nivel = models.IntegerField(default=0)
    activado = models.BooleanField(default=True)

    def __str__(self):
        return self.username
