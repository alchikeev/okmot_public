# news/urls.py
from django.urls import path
from . import views

app_name = 'news' # Важно для создания уникальных имен URL (например, news:list)

urlpatterns = [
    path('', views.news_list, name='list'), # Путь для списка всех новостей
    path('<slug:slug>/', views.news_detail, name='detail'), # Путь для детальной новости
]