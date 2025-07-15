# okmot/council/urls.py
from django.urls import path
from . import views

app_name = 'council' # <-- ДОБАВЬТЕ ЭТУ СТРОКУ!

urlpatterns = [
    # Депутаты
    path('deputies/', views.deputy_list, name='deputy_list'),
    path('deputies/<int:pk>/', views.deputy_detail, name='deputy_detail'),

    # Решения Кенеша
    path('decisions/', views.decision_list, name='decision_list'),
    path('decisions/<slug:slug>/', views.decision_detail, name='decision_detail'),
]