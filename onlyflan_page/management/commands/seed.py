from django.core.management.base import BaseCommand
from onlyflan_page.models import Usuario, Producto

class Command(BaseCommand):
    help = 'Creando Database Inicial'

    def handle(self, *args, **kwargs):
        # Crea usuarios iniciales
        Usuario.objects.create_user(username='admin', password='admin123', rut='12345678-9', email='admin@example.com', nivel=10, is_superuser=True, is_staff=True)
        Usuario.objects.create_user(username='user', password='user123', rut='98765432-1', email='user@example.com', nivel=0)
        
        # Crea productos iniciales
        productos = [
            {'nombre': 'Flan de Vainilla', 'descripcion': 'Delicioso flan de vainilla.', 'precio': 1000, 'destacada': True, 'activado': True},
            {'nombre': 'Flan de Chocolate', 'descripcion': 'Delicioso flan de chocolate.', 'precio': 2000, 'destacada': False, 'activado': True},
            {'nombre': 'Flan de Coco', 'descripcion': 'Delicioso flan de coco.', 'precio': 3000, 'destacada': True, 'activado': True},
        ]

        for producto in productos:
            Producto.objects.create(**producto)
        self.stdout.write(self.style.SUCCESS('Database INICIAL CREADA'))
    