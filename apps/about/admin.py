# about/admin.py
from django.contrib import admin
from .models import Page, Person, Department, Report, Budget

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'updated_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'is_leader', 'order', 'phone', 'email')
    list_filter = ('is_leader', 'position')
    search_fields = ('full_name', 'position', 'biography')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'position', 'photo', 'biography', 'is_leader', 'order')
        }),
        ('Контактная информация', {
            'fields': ('phone', 'email', 'reception_schedule'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'phone', 'email', 'order')
    list_filter = ('head',)
    search_fields = ('name', 'description')
    raw_id_fields = ('head',) # Полезно для выбора руководителя, если их много

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'report_year', 'is_published', 'published_date')
    list_filter = ('is_published', 'report_year')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget_year', 'is_published', 'published_date')
    list_filter = ('is_published', 'budget_year')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'