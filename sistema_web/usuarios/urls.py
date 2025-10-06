from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    
    path('login/', views.login_view, name='login'),
    
    path('logout/', views.logout_view, name='logout'),
    
    path('cadastro/', views.cadastro_view, name='cadastro'),
    
    path('perfil/', views.perfil_view, name='perfil'),
    
    path('erro403/', views.erro_403_teste, name='erro403'),
    
    path('erro500/', views.erro_500_teste, name='erro500'),
    
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    
    path('pessoa/cadastro/', views.cadastro_pessoa, name='cadastro_pessoa'),

    # Recuperar senha - formulário para digitar email
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='usuarios/password_reset.html',
        email_template_name='usuarios/password_reset_email.html',
        subject_template_name='usuarios/password_reset_subject.txt',
        success_url='/password_reset_done/'
    ), name='password_reset'),

    # Mensagem de que o email foi enviado
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='usuarios/password_reset_done.html'
    ), name='password_reset_done'),

    # Link no email para redefinir a senha (confirmação)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='usuarios/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    # Página final de confirmação de senha alterada
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='usuarios/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Alterar senha para usuário logado
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/password_change.html',
        success_url='/password_change_done/'
    ), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='usuarios/password_change_done.html'
    ), name='password_change_done'),
]
