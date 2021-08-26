from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django import forms
from .forms import UserCreationFormWithEmail


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "usuario/login.html", {'form': form})


# def registro(request):
#     form = UsuarioForm()
#     if request.method == "POST":
#         form = UsuarioForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             if user is not None:
#                 do_login(request, user)
#                 return redirect('/login')
#     return render(request, "usuario/registro.html", {'form': form})


def salir(request):
    do_logout(request)
    return redirect('/login')


class Registro(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'usuario/registro.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?registro'

    def get_form(self, form_class=None):
        form = super(Registro, self).get_form()
        # Modificamos en tiempo real
        form.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'})
        return form
