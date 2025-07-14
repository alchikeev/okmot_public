# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    """Отображает список всех опубликованных новостей."""
    # Получаем только опубликованные новости, отсортированные по дате публикации (от новых к старым)
    news_items = News.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'news_items': news_items
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    """Отображает детальную страницу одной новости."""
    # Получаем новость по ее slug. Если не найдена, возвращаем 404 ошибку.
    news_item = get_object_or_404(News, slug=slug, is_published=True)
    context = {
        'news_item': news_item
    }
    return render(request, 'news/news_detail.html', context)