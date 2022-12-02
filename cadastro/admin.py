from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


UserAdmin.fieldsets += (
    ('Informações adicionais', {'fields': ('cpf', 'telefone', 'data_de_nascimento', 'sexo')}),
    ('Endereço', {'fields': ('cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf',)}),
)

# Register your models here.
admin.site.register(Usuario, UserAdmin)