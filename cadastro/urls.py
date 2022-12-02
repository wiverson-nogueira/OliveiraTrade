from django.urls import path, reverse_lazy
from .views import Homepage, Criarconta, Paginaperfil, Paginadetalhe
from django.contrib.auth import views as auth_view

app_name = 'cadastro'

urlpatterns = [
    # url - view - template
    path('', Homepage.as_view(), name='homepage'),
    path('detalhes/', Paginadetalhe.as_view(), name='detalhes'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarsenha.html',
                                                             success_url=reverse_lazy('cadastro:detalhes')), name='mudarsenha'),
]