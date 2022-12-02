from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.core.validators import RegexValidator


class HomepageForm(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    first_name = forms.CharField(required=True, label='Primeiro nome')
    last_name = forms.CharField(required=True, label='Último nome')
    email = forms.EmailField(required=True)
    cpf = forms.CharField(required=True, min_length=11, max_length=11, validators=[RegexValidator(r'^\d{1,11}$')],
                           label='CPF', widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    telefone = forms.CharField(required=True, min_length=11, max_length=11, validators=[RegexValidator(r'^\d{1,11}$')],
                          widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    data_de_nascimento = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(required=False, choices=Usuario.LISTA_CATEGORIAS)
    cep = forms.CharField(required=True, min_length=8, max_length=8, validators=[RegexValidator(r'^\d{1,11}$')],
                           label='CEP', widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    rua = forms.CharField(required=True, max_length=50)
    numero = forms.IntegerField(required=True)
    complemento = forms.CharField(required=False, max_length=50)
    bairro = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Preencha o campo CEP',
                                                                                         'readonly': 'True'}))
    cidade = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Preencha o campo CEP',
                                                                                         'readonly': 'True'}))
    uf = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Preencha o campo CEP',
                                                                                    'readonly': 'True'}))

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'cpf', 'telefone',
                  'data_de_nascimento', 'sexo', 'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf')


class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Primeiro nome')
    last_name = forms.CharField(required=True, label='Último nome')
    email = forms.EmailField(required=True)
    cpf = forms.CharField(required=True, min_length=11, max_length=11, validators=[RegexValidator(r'^\d{1,11}$')],
                           label='CPF', widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    telefone = forms.CharField(required=True, min_length=11, max_length=11, validators=[RegexValidator(r'^\d{1,11}$')],
                          widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    data_de_nascimento = forms.DateField(required=True)
    sexo = forms.ChoiceField(required=False, choices=Usuario.LISTA_CATEGORIAS)
    cep = forms.CharField(required=True, min_length=8, max_length=8, validators=[RegexValidator(r'^\d{1,11}$')],
                           label='CEP', widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    rua = forms.CharField(required=True, max_length=50)
    numero = forms.IntegerField(required=True)
    complemento = forms.CharField(required=False, max_length=50)
    bairro = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Preencha o campo CEP',
                                                                                         'readonly': 'True'}))
    cidade = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Preencha o campo CEP',
                                                                                         'readonly': 'True'}))
    uf = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Preencha o campo CEP',
                                                                                    'readonly': 'True'}))

    class Meta:
        model = Usuario
        exclude = ('password1', 'password2')
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf', 'telefone',
                  'data_de_nascimento', 'sexo', 'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf')
