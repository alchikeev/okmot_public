# documents/views.py
from django.shortcuts import render, get_object_or_404
from .models import Document

def document_list(request):
    """Отображает список всех опубликованных документов."""
    # Получаем только опубликованные документы, отсортированные по дате публикации (от новых к старым)
    documents = Document.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'documents': documents
    }
    return render(request, 'documents/document_list.html', context)

def document_detail(request, slug):
    """Отображает детальную страницу одного документа."""
    # Получаем документ по его slug. Если не найден, возвращаем 404 ошибку.
    document = get_object_or_404(Document, slug=slug, is_published=True)
    context = {
        'document': document
    }
    return render(request, 'documents/document_detail.html', context)