# investors/urls.py
from django.urls import path
from . import views

app_name = 'investors' # Определяем пространство имен для URL-ов этого приложения

urlpatterns = [
    path('projects/', views.project_list, name='project_list'), # Список проектов
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'), # Детальная страница проекта
    # Здесь также можно добавить URL для статической страницы "Для инвесторов"
    # path('', views.investors_home, name='home'), # Например, общая страница для инвесторов
]