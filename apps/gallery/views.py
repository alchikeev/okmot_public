# gallery/views.py
from django.shortcuts import render, get_object_or_404
from .models import PhotoAlbum

def album_list(request):
    """Отображает список всех опубликованных фотоальбомов."""
    albums = PhotoAlbum.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'albums': albums
    }
    return render(request, 'gallery/album_list.html', context)

def album_detail(request, slug):
    """Отображает детальную страницу альбома с фотографиями."""
    album = get_object_or_404(PhotoAlbum, slug=slug, is_published=True)
    photos = album.photos.all() # Получаем все фотографии, связанные с этим альбомом
    context = {
        'album': album,
        'photos': photos
    }
    return render(request, 'gallery/album_detail.html', context)