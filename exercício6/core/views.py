from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pessoa

@login_required
def perfil(request):
    try:
        pessoa = Pessoa.objects.get(usuario=request.user)
    except Pessoa.DoesNotExist:
        pessoa = None

    return render(request, 'perfil.html', {'pessoa': pessoa})
