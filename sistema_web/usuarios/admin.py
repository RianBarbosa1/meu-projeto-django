from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email", "telefone", "bairro")
    search_fields = ("nome", "cpf", "email", "rg", "bairro")
    list_filter = ("bairro",)
    ordering = ("nome",)
