from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, PessoaForm, EnderecoForm
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
    pessoas = Pessoa.objects.select_related('endereco').all()
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


@login_required(login_url='login')
def cadastro_pessoa(request):
    if request.method == 'POST':
        pessoa_form = PessoaForm(request.POST)
        endereco_form = EnderecoForm(request.POST)

        if pessoa_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            pessoa = pessoa_form.save(commit=False)
            pessoa.endereco = endereco
            pessoa.usuario = request.user  # Ajuste conforme seu modelo
            pessoa.save()

            messages.success(request, 'Pessoa cadastrada com sucesso!')
            return redirect('lista_pessoas')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        pessoa_form = PessoaForm()
        endereco_form = EnderecoForm()

    context = {
        'pessoa_form': pessoa_form,
        'endereco_form': endereco_form,
    }
    return render(request, 'usuarios/cadastro_pessoa.html', context)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'usuarios/password_reset.html'  # Template do formulário de recuperação
    email_template_name = 'usuarios/password_reset_email.html'  # Template do email que será enviado
    success_url = reverse_lazy('password_reset_done')  # Para onde redirecionar após o envio do email
