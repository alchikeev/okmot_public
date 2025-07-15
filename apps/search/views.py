# search/views.py
from django.shortcuts import render
from django.db.models import Q
from apps.news.models import News
from apps.documents.models import Document
from apps.community.models import BlogPost
from apps.about.models import Page
from apps.info.models import Landmark
# Можно добавить и другие модели по мере необходимости

def search_results(request):
    query = request.GET.get('q') # Получаем поисковый запрос из GET-параметра 'q'
    results = {
        'news': None,
        'documents': None,
        'blogs': None,
        'pages': None,
        'landmarks': None
    }

    if query:
        # Используем Q-объекты для поиска по нескольким полям
        news_results = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        ).distinct()

        documents_results = Document.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            is_published=True
        ).distinct()

        blogs_results = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author_name__icontains=query),
            status='published'
        ).distinct()

        pages_results = Page.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        ).distinct()

        landmarks_results = Landmark.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query),
            is_published=True
        ).distinct()

        results = {
            'news': news_results,
            'documents': documents_results,
            'blogs': blogs_results,
            'pages': pages_results,
            'landmarks': landmarks_results
        }

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search/search_results.html', context)