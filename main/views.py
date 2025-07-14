# okmot/main/views.py
from django.shortcuts import render
from news.models import News
from documents.models import Document # <-- Добавьте эту строку для импорта модели Document

def home(request):
    latest_news = News.objects.filter(is_published=True).order_by('-published_date')[:3]
    # Получаем 3 последних опубликованных документа
    latest_documents = Document.objects.filter(is_published=True).order_by('-published_date')[:3] # <-- Добавьте эту строку
    context = {
        'latest_news': latest_news,
        'latest_documents': latest_documents, # <-- Добавьте эту строку
        # 'appeal_form_url': reverse_lazy('appeals:submit') # Не нужно передавать через контекст, лучше генерировать в шаблоне
    }
    return render(request, 'main/home.html', context)