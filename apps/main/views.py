# okmot/main/views.py
from django.shortcuts import render
from apps.news.models import News
from apps.documents.models import Document
from apps.about.models import Person # <-- Добавьте эту строку

def home(request):
    latest_news = News.objects.filter(is_published=True).order_by('-published_date')[:3]
    latest_documents = Document.objects.filter(is_published=True).order_by('-published_date')[:3]
    # Получаем главу айыл окмоту (предполагаем, что есть только один с is_leader=True)
    head_of_okmot = Person.objects.filter(is_leader=True).first() # <-- Добавьте эту строку
    context = {
        'latest_news': latest_news,
        'latest_documents': latest_documents,
        'head_of_okmot': head_of_okmot, # <-- Добавьте эту строку
    }
    return render(request, 'main/home.html', context)