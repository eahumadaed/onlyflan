# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Usuario
from .forms import RegisterForm, LoginForm

def home(request):
    return render(request, 'main/home.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'main/productos.html', {'productos': productos})

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
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def admin_page(request):
    if request.user.nivel == 10:
        return render(request, 'main/admin_page.html')
    else:
        return redirect('home')
