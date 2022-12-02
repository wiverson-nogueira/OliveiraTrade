from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):

    LISTA_CATEGORIAS = (
        ('', '----'),
        ("MASCULINO", 'Masculino'),
        ("FEMININO", "Feminino"),
    )

    cpf = models.CharField(max_length=11, null=True)
    telefone = models.CharField(max_length=11, null=True)
    data_de_nascimento = models.DateField(null=True)
    sexo = models.CharField(max_length=10, choices=LISTA_CATEGORIAS, null=True)
    cep = models.CharField(max_length=8, null=True)
    rua = models.CharField(max_length=50, null=True)
    numero = models.IntegerField(null=True)
    complemento = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=50, null=True)
    uf = models.CharField(max_length=2, null=True)
