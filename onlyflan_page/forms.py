from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Usuario,Producto

class RegisterForm(UserCreationForm):
    rut = forms.CharField(max_length=12)
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'rut', 'email', 'password1', 'password2']
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nivel', 'activado']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'destacada', 'activado']