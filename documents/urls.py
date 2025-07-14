# documents/urls.py
from django.urls import path
from . import views

app_name = 'documents' # Важно для создания уникальных имен URL

urlpatterns = [
    path('', views.document_list, name='list'), # Путь для списка всех документов
    path('<slug:slug>/', views.document_detail, name='detail'), # Путь для детального документа
]