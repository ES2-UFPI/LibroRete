from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/<str:nick>',views.get_user, name='usuarios'),
    path('perfis/<str:nick>', views.get_by_nick, name='perfis'),
    path('listas/<str:nick>', views.get_user_lists, name='listas'),
    path('interacoes/', views.create_interaction, name='criar_interacao'),
    path('buscar-usuarios/', views.search_users, name='buscar_usuarios'),
    path('novo-post/', views.create_post, name='criar_post'),
    path('posts/<str:nick>', views.get_post_usuario, name='post_usuario'),
    ]
