from django.db import models
from django.core.validators import RegexValidator

cpf_validator = RegexValidator(
    r'^\d{11}$',
    'Informe 11 dígitos (apenas números) para o CPF.'
)

telefone_validator = RegexValidator(
    r'^\+?\d{8,15}$',
    'Informe apenas números (8 a 15 dígitos, opcional + no início).'
)

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, validators=[telefone_validator])
    data_nascimento = models.DateField(blank=True, null=True)
    rg = models.CharField(max_length=12, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=100, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
