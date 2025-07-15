# about/urls.py
from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    # Для информационных страниц (История, Общие сведения)
    path('pages/<slug:slug>/', views.page_detail, name='page_detail'),
    path('pages/', views.page_list, name='page_list'), # Опционально, если нужен список всех инфо-страниц

    # Для руководства и сотрудников
    path('leadership/', views.leadership_list, name='leadership_list'),
    path('person/<int:pk>/', views.person_detail, name='person_detail'), # Детальная страница персоны

    # Для отделов
    path('departments/', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'), # Детальная страница отдела

    # Для отчетов
    path('reports/', views.report_list, name='report_list'),
    path('reports/<slug:slug>/', views.report_detail, name='report_detail'),

    # Для бюджетов для граждан
    path('budgets/', views.budget_list, name='budget_list'),
    path('budgets/<slug:slug>/', views.budget_detail, name='budget_detail'),
]