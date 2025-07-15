# documents/admin.py
from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'published_date', 'is_published')
    list_filter = ('is_published', 'published_date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    # Убираем auto_now_add и auto_now поля из fieldsets, как и для новостей
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'file', 'is_published')
        }),
    )