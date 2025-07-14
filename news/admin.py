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

    # ИЗМЕНЕНИЕ ЗДЕСЬ: Убираем 'published_date' и 'updated_date' из 'fieldsets'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'image', 'is_published')
        }),
        # Блок "Даты" можно убрать совсем, или оставить пустым, если он не нужен для других полей
        # (Если хотите отображать их только для информации, не для редактирования, Django сам это сделает)
        # Если вы хотите, чтобы эти поля (published_date, updated_date) просто отображались в форме без возможности редактирования
        # то их нужно убрать из fieldsets. Django админка сама покажет их в просмотре/редактировании как нередактируемые.
    )