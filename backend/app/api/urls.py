from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/<str:nick>',views.get_user, name='usuarios'),
    path('perfis/<str:nick>', views.get_by_nick, name='perfis'),
    path('listas/<str:nick>', views.get_user_lists, name='listas'),
    path('interacoes/', views.create_interaction, name='criar_interacao'),
    path('buscar-usuarios/', views.search_users, name='buscar_usuarios'),
    path('buscar-livros/', views.search_books, name='buscar_livros'),
    path('novo-post/', views.create_post, name='criar_post'),
    path('posts/', views.get_all_posts, name='posts'),
    path('posts/<str:nick>', views.get_post_usuario, name='post_usuario'),
    path('posts/feed/<str:nick>', views.get_posts_feed, name='feed'), #usar esse endpoint para mostrar feed tanto recomendaçoes como seguindo.
    path('posts/top-tags/<str:username>/', views.get_users_by_user_top_tags, name='posts_top_tags'),
    ]