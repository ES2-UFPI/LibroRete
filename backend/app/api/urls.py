from django.urls import path
from . import views


# router = DefaultRouter()
# router.register(r'usuarios', UsuarioViewSet, basename='usuario')
# router.register(r'perfis/<str:nick>', PerfilViewSet, basename='perfil')
# urlpatterns = router.urls

urlpatterns = [
    path('usuarios/<str:nick>',views.get_user, name='usuarios'),
    path('perfis/<str:nick>', views.get_by_nick, name='perfis'),
    path('listas/<str:nick>', views.get_user_lists, name='listas'),
    path('interacoes/', views.criar_interacao, name='criar_interacao'),
    path('posts/', views.get_posts, name='posts'),
    path('posts/<int:id>', views.get_post, name='post'),
    path('posts/<int:id>/interacoes', views.get_post_interacoes, name='post_interacoes'),
]
