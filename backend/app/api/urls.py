from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/<str:nick>',views.get_user, name='usuarios'),
    path('perfis/<str:nick>', views.get_by_nick, name='perfis'),
    path('listas/<str:nick>', views.get_user_lists, name='listas'),
    path('interacoes/', views.create_interaction, name='criar_interacao'),
    path('buscar-usuarios/', views.search_users, name='buscar_usuarios'),
    path('buscar-livros/', views.search_books, name='buscar_livros'),
    path('usuarios/<str:nick>/tags/contar/', views.get_user_tag_interactions, name='buscar_tags_contador_usuario'),
    path('novo-post/', views.create_post, name='criar_post'),
    path('posts/', views.get_all_posts, name='posts'),
    path('posts/<str:nick>', views.get_post_usuario, name='post_usuario'),
    path('posts/top-tags/<str:username>/', views.get_users_by_user_top_tags, name='posts_top_tags'),
    path('posts-seguindo/feed/<str:nick>', views.get_posts_feed, name='posts_seguindo_feed'),
    path('posts-recomendados/feed/<str:nick>', views.get_posts_by_user_top_tags, name='posts_recomendados_feed'),
    path('posts/feed/<str:nick>', views.combined_feed, name='posts_combinado_recomendados_seguindo_feed'),
    ]