# investors/admin.py
from django.contrib import admin
from .models import InvestmentProject

@admin.register(InvestmentProject)
class InvestmentProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'budget_needed', 'contact_person', 'is_published', 'published_at')
    list_filter = ('status', 'is_published', 'start_date', 'end_date')
    search_fields = ('title', 'short_description', 'full_description', 'contact_person')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'short_description', 'full_description', 'image', 'is_published', 'status')
        }),
        ('Финансовая информация', {
            'fields': ('budget_needed', 'expected_return'),
            'classes': ('collapse',),
        }),
        ('Сроки', {
            'fields': ('start_date', 'end_date'),
            'classes': ('collapse',),
        }),
        ('Контакты', {
            'fields': ('contact_person', 'contact_email', 'contact_phone'),
            'classes': ('collapse',),
        }),
    )