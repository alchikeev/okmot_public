from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Пример для главной страницы
]