# appeals/urls.py
from django.urls import path
from . import views

app_name = 'appeals'

urlpatterns = [
    path('submit/', views.submit_appeal, name='submit'), # Путь для формы подачи обращения
    # path('status/<uuid:appeal_uuid>/', views.appeal_status, name='status'), # Пока не используем, но оставим для будущей реализации отслеживания
]