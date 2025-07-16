# community/urls.py
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # Объявления жителей
    path('ads/', views.advertisement_list, name='advertisement_list'),
    path('ads/submit/', views.submit_advertisement, name='submit_advertisement'), # Поднимите этот маршрут выше
    path('ads/<slug:slug>/', views.advertisement_detail, name='advertisement_detail'),

    # Блоги жителей
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/submit/', views.submit_blog_post, name='submit_blog_post'), # Поднимите этот маршрут выше
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
]