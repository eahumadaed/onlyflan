from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegisterForm(UserCreationForm):
    rut = forms.CharField(max_length=12)
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'rut', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)