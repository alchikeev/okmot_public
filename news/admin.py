# news/admin.py
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published', 'updated_date')
    list_filter = ('is_published', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Автоматически заполняет slug на основе заголовка
    date_hierarchy = 'published_date' # Иерархия по дате для удобной навигации
    # Добавляем поле для загрузки изображений в админке
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'image', 'is_published')
        }),
        ('Даты', {
            'fields': ('published_date', 'updated_date'),
            'classes': ('collapse',), # Можно свернуть этот блок
        }),
    )