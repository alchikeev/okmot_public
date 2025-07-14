# info/urls.py
from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    # Важные телефоны
    path('phones/', views.phone_list, name='phone_list'),

    # Достопримечательности
    path('landmarks/', views.landmark_list, name='landmark_list'),
    path('landmarks/<slug:slug>/', views.landmark_detail, name='landmark_detail'),

    # Информационные страницы
    path('pages/<slug:slug>/', views.static_page_detail, name='static_page_detail'),
]