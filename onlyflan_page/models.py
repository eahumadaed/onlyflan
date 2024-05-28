from django.db import models
from django.contrib.auth.models import AbstractUser

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    ruta_imagen = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    destacada = models.BooleanField(default=False)
    activado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    nivel = models.IntegerField(default=0)  # 0: usuario común, 10: administrador
    activado = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_usuario_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_usuario_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username