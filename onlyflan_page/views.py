# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm, RegisterForm, LoginForm
import os
from django.conf import settings


def home(request):
    productos = Producto.objects.all()
    return render(request, 'main/home.html', {'productos': productos , 'MEDIA_URL': settings.MEDIA_URL})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'main/productos.html', {'productos': productos , 'MEDIA_URL': settings.MEDIA_URL})

def about(request):
    return render(request, 'main/about.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def admin_page(request):
    if request.user.nivel != 10:
        return redirect('home')

    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        if 'change_user_level' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(Usuario, pk=user_id)
            user.nivel = request.POST.get('nivel')
            user.activado = 'activado' in request.POST
            user.save()
            
        elif 'change_password' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(Usuario, pk=user_id)
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                
        elif 'add_product' in request.POST:
            product_form = ProductoForm(request.POST, request.FILES)
            if product_form.is_valid():
                product = product_form.save(commit=False)
                product.save()
                if 'ruta_imagen' in request.FILES:
                    uploaded_file = request.FILES['ruta_imagen']
                    file_path = os.path.join(settings.MEDIA_ROOT, 'imagenes_productos', f'{product.id}.jpg')
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                    product.ruta_imagen = f'imagenes_productos/{product.id}.jpg'
                    product.save()
                    
        elif 'update_product' in request.POST:
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Producto, pk=product_id)
            product_form = ProductoForm(request.POST, request.FILES, instance=product)
            if product_form.is_valid():
                product_form.save(commit=False)
                if 'ruta_imagen' in request.FILES:
                    uploaded_file = request.FILES['ruta_imagen']
                    file_path = os.path.join(settings.MEDIA_ROOT, 'imagenes_productos', f'{product.id}.jpg')
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                    product.ruta_imagen = f'imagenes_productos/{product.id}.jpg'
                product.save()

    context = {
        'usuarios': usuarios,
        'productos': productos,
        'password_form': PasswordChangeForm(user=request.user),
        'product_form': ProductoForm(),
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'main/admin_page.html', context)
