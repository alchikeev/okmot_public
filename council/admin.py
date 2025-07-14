# council/admin.py
from django.contrib import admin
from .models import Deputy, CouncilDecision

@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position_in_council', 'constituency', 'is_active', 'order')
    list_filter = ('is_active', 'constituency', 'position_in_council')
    search_fields = ('full_name', 'bio', 'constituency')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'photo', 'bio', 'is_active', 'order')
        }),
        ('Информация в кенеше', {
            'fields': ('position_in_council', 'constituency'),
        }),
        ('Контактная информация', {
            'fields': ('contact_phone', 'contact_email'),
            'classes': ('collapse',),
        }),
    )

@admin.register(CouncilDecision)
class CouncilDecisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'decision_type', 'decision_number', 'decision_date', 'is_published')
    list_filter = ('decision_type', 'is_published', 'decision_date')
    search_fields = ('title', 'description', 'decision_number')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'decision_date'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'decision_number', 'decision_date', 'decision_type', 'description', 'file', 'is_published')
        }),
    )