from django.contrib import admin
from .models import Pessoa, Endereco  # importe Endereco também

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email", "telefone", "get_bairro")
    search_fields = ("nome", "cpf", "email", "rg")
    list_filter = ()
    ordering = ("nome",)

    def get_bairro(self, obj):
        try:
            return obj.endereco.bairro
        except:
            return "Sem endereço"

    get_bairro.short_description = "Bairro"

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    search_fields = ('bairro', 'cidade', 'estado', 'cep')
    list_filter = ('estado', 'cidade')

