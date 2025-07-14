# community/admin.py
from django.contrib import admin
from django.utils import timezone # Импортируем timezone для установки даты публикации
from .models import Advertisement, BlogPost

# Действие для модерации: Опубликовать
@admin.action(description='Опубликовать выбранные элементы')
def make_published(modeladmin, request, queryset):
    for item in queryset:
        if item.status == 'pending': # Публикуем только те, что в ожидании
            item.status = 'published'
            item.published_at = timezone.now() # Устанавливаем дату публикации
            item.save()
    modeladmin.message_user(request, "Выбранные элементы успешно опубликованы.", level='success')

# Действие для модерации: Отклонить
@admin.action(description='Отклонить выбранные элементы')
def make_rejected(modeladmin, request, queryset):
    queryset.update(status='rejected')
    modeladmin.message_user(request, "Выбранные элементы отклонены.", level='warning')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_name', 'submitted_at', 'status', 'published_at', 'is_published_method')
    list_filter = ('status', 'submitted_at')
    search_fields = ('title', 'content', 'contact_name', 'contact_phone', 'contact_email')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('submitted_at', 'published_at') # Эти поля не редактируются вручную
    actions = [make_published, make_rejected] # Добавляем действия модерации

    def get_fieldsets(self, request, obj=None):
        # Разделяем поля для формы создания и редактирования
        if obj: # Режим редактирования
            return (
                (None, {
                    'fields': ('title', 'slug', 'content', 'image')
                }),
                ('Контактная информация', {
                    'fields': ('contact_name', 'contact_phone', 'contact_email'),
                    'classes': ('collapse',),
                }),
                ('Модерация и статус', { # Этот блок виден только при редактировании
                    'fields': ('status', 'moderator_comment', 'published_at', 'submitted_at'),
                }),
            )
        return ( # Режим создания (скрываем поля модерации)
            (None, {
                'fields': ('title', 'slug', 'content', 'image')
            }),
            ('Контактная информация', {
                'fields': ('contact_name', 'contact_phone', 'contact_email'),
                'classes': ('collapse',),
            }),
        )

    # Кастомный метод для отображения "Опубликовано" в списке, чтобы он зависел от статуса
    def is_published_method(self, obj):
        return obj.status == 'published'
    is_published_method.boolean = True # Отображать как галочку
    is_published_method.short_description = 'Опубликовано' # Название колонки


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'submitted_at', 'status', 'published_at', 'is_published_method')
    list_filter = ('status', 'submitted_at')
    search_fields = ('title', 'content', 'author_name', 'author_contact_email')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('submitted_at', 'published_at')
    actions = [make_published, make_rejected] # Добавляем действия модерации

    def get_fieldsets(self, request, obj=None):
        if obj: # Режим редактирования
            return (
                (None, {
                    'fields': ('title', 'slug', 'content', 'image')
                }),
                ('Информация об авторе', {
                    'fields': ('author_name', 'author_contact_email'),
                    'classes': ('collapse',),
                }),
                ('Модерация и статус', {
                    'fields': ('status', 'moderator_comment', 'published_at', 'submitted_at'),
                }),
            )
        return ( # Режим создания
            (None, {
                'fields': ('title', 'slug', 'content', 'image')
            }),
            ('Информация об авторе', {
                'fields': ('author_name', 'author_contact_email'),
                'classes': ('collapse',),
            }),
        )

    def is_published_method(self, obj):
        return obj.status == 'published'
    is_published_method.boolean = True
    is_published_method.short_description = 'Опубликовано'