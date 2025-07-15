# about/views.py
from django.shortcuts import render, get_object_or_404
from .models import Page, Person, Department, Report, Budget

# --- Представления для Информационных страниц ---
def page_list(request):
    pages = Page.objects.filter(is_published=True).order_by('title')
    context = {'pages': pages}
    return render(request, 'about/page_list.html', context)

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    context = {'page': page}
    return render(request, 'about/page_detail.html', context)

# --- Представления для Руководства и сотрудников ---
def leadership_list(request):
    leaders = Person.objects.filter(is_leader=True).order_by('order')
    other_staff = Person.objects.filter(is_leader=False).order_by('order')
    context = {
        'leaders': leaders,
        'other_staff': other_staff
    }
    return render(request, 'about/leadership_list.html', context)

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {'person': person}
    return render(request, 'about/person_detail.html', context)

# --- Представления для Отделов ---
def department_list(request):
    departments = Department.objects.all().order_by('order')
    context = {'departments': departments}
    return render(request, 'about/department_list.html', context)

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    context = {'department': department}
    return render(request, 'about/department_detail.html', context)

# --- Представления для Отчетов ---
def report_list(request):
    reports = Report.objects.filter(is_published=True).order_by('-report_year', '-published_date')
    context = {'reports': reports}
    return render(request, 'about/report_list.html', context)

def report_detail(request, slug):
    report = get_object_or_404(Report, slug=slug, is_published=True)
    context = {'report': report}
    return render(request, 'about/report_detail.html', context)

# --- Представления для Бюджетов для граждан ---
def budget_list(request):
    budgets = Budget.objects.filter(is_published=True).order_by('-budget_year', '-published_date')
    context = {'budgets': budgets}
    return render(request, 'about/budget_list.html', context)

def budget_detail(request, slug):
    budget = get_object_or_404(Budget, slug=slug, is_published=True)
    context = {'budget': budget}
    return render(request, 'about/budget_detail.html', context)