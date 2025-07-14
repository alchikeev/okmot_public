# gallery/admin.py
from django.contrib import admin
from .models import GalleryCategory, PhotoAlbum, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3 # Количество пустых форм для загрузки сразу
    fields = ('image', 'caption')

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    inlines = [PhotoInline] # Подключаем инлайн-модель здесь!