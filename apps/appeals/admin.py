# appeals/admin.py
from django.contrib import admin
from .models import Appeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'submitted_at', 'status')
    list_filter = ('status', 'submitted_at')
    search_fields = ('full_name', 'email', 'subject', 'message')
    readonly_fields = ('submitted_at',) # Поле с датой подачи не должно редактироваться
    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'phone', 'subject', 'message', 'file_attachment')
        }),
        ('Статус и решение', {
            'fields': ('status', 'resolution_text'),
        }),
        ('Информация о подаче', {
            'fields': ('submitted_at',),
            'classes': ('collapse',), # Можно свернуть этот блок
        }),
    )