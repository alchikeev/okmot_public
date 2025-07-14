# info/admin.py
from django.contrib import admin
from .models import ImportantPhone, Landmark, StaticInfoPage

@admin.register(ImportantPhone)
class ImportantPhoneAdmin(admin.ModelAdmin):
    list_display = ('organization', 'phone_number', 'order')
    list_editable = ('order',) # Позволяет редактировать порядок прямо в списке
    list_display_links = ('organization',) # Чтобы можно было кликать по организации

@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(StaticInfoPage)
class StaticInfoPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}