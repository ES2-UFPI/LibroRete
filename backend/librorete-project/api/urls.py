from django.urls import path
from .views import get_listas, get_user_lists_with_books

urlpatterns = [
    path('listas/', get_listas, name='lista'),
    path('user/<str:username>/listas/', get_user_lists_with_books, name='user-lists-with-books'),
]