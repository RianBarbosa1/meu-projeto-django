from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Pessoa


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Usuário digitado: {username}")
        print(f"Senha digitada: {password}")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a home após login
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_view(request):
    return render(request, 'usuarios/home.html')


@login_required(login_url='login')
def perfil_view(request):
    return render(request, 'usuarios/perfil.html', {'user': request.user})


@login_required(login_url='login')
def erro_403_teste(request):
    raise PermissionDenied


@login_required(login_url='login')
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'usuarios/lista_pessoas.html', {'pessoas': pessoas})


@login_required(login_url='login')
def erro_500_teste(request):
    1 / 0  # Força um erro de divisão por zero, gerando erro 500


def error_403_view(request, exception):
    return render(request, '403.html', status=403)


def error_500_view(request):
    return render(request, '500.html', status=500)


def cadastro_view(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'usuarios/password_reset.html'  # Template do formulário de recuperação
    email_template_name = 'usuarios/password_reset_email.html'  # Template do email que será enviado
    success_url = reverse_lazy('password_reset_done')  # Para onde redirecionar após o envio do email
