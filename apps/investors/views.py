# investors/views.py
from django.shortcuts import render, get_object_or_404
from .models import InvestmentProject

def project_list(request):
    """Отображает список всех опубликованных инвестиционных проектов."""
    projects = InvestmentProject.objects.filter(is_published=True).order_by('-published_at')
    context = {
        'projects': projects
    }
    return render(request, 'investors/project_list.html', context)

def project_detail(request, slug):
    """Отображает детальную страницу одного инвестиционного проекта."""
    project = get_object_or_404(InvestmentProject, slug=slug, is_published=True)
    context = {
        'project': project
    }
    return render(request, 'investors/project_detail.html', context)

# Опционально: Общая страница для инвесторов (если будет статический контент)
# from apps.about.models import Page # Если используете Page для статики
# def investors_home(request):
#    # Можно использовать Page для контента "Инвестиционный профиль"
#    investor_info_page = get_object_or_404(Page, slug='investor-profile') # Предполагаем, что есть такая страница
#    projects = InvestmentProject.objects.filter(is_published=True, status='active').order_by('-published_at')[:3]
#    context = {
#        'investor_info_page': investor_info_page,
#        'active_projects': projects
#    }
#    return render(request, 'investors/investors_home.html', context)