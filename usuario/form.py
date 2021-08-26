from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
        class Meta:
                model = User
                fields = [
                        'first_name',
                        'last_name',
                        'email',
                        'username',
                        'password'
                ]
                labels = {
                        'first_name':'Nombres',
                        'last_name': 'Apellidos',
                        'email': 'Correo electronico',
                        'username': 'Nombre de usuario',
                        'password': 'Ingrese su contraseña'
                }
                widgets = {
                        'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Ingrese su nombre'}),
                        'last_name': forms.TextInput(attrs={'class': 'form-control','required': True, 'placeholder': 'Ingrese su apellido'}),
                        'email': forms.EmailInput(attrs={'class': 'form-control','required': True, 'placeholder': 'Ingrese su correo electronico'}),
                        'username': forms.TextInput(attrs={'class': 'form-control','required': True, 'placeholder': 'Ingrese su nombre de usuario'}),
                        'password1': forms.PasswordInput(attrs={'class': 'form-control','required': True, 'placeholder': 'Ingrese su contraseña'}),
                        'password2': forms.PasswordInput(attrs={'class': 'form-control','required': True, 'placeholder': 'Confirme su contraseña'}),
                }