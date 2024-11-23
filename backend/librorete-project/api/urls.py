from django.urls import path
from .views import get_listas

urlpatterns = [
    path('listas/', get_listas, name='lista'),
]