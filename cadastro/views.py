from django.shortcuts import redirect, reverse
from django.views.generic import FormView, UpdateView, ListView, CreateView
from .models import Usuario
from .forms import CriarContaForm, HomepageForm, EditarPerfilForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


class Paginadetalhe(LoginRequiredMixin, ListView):
    template_name = 'detalhes.html'
    model = Usuario


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = HomepageForm

    def get(self, request, *args, **kwargs):
        # Caso o usuário esteja logado:
        if request.user.is_authenticated:
            # Redireciona para página 'detalhes.html'
            return redirect('cadastro:detalhes')
        else:
            # Caso contrário, redireciona para 'homepage.html'
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        # Verifica se o email digitado já existe na base de dados
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            # Caso exista redireciona para página de login
            return reverse('cadastro:login')
        else:
            # Caso contrário, redireciona para pagina de criação de conta
            return reverse('cadastro:criarconta')


class Criarconta(SuccessMessageMixin, CreateView):
    template_name = 'criarconta.html'
    model = Usuario
    form_class = CriarContaForm
    success_url = '/login'
    success_message = 'Cadastro realizado com sucesso'


class Paginaperfil(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    form_class = EditarPerfilForm
    success_url = '/detalhes'
    success_message = 'Dados atualizados com sucesso'