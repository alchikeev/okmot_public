# gallery/models.py
from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-псевдоним")
    description = models.TextField(blank=True, null=True, verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория галереи"
        verbose_name_plural = "Категории галереи"

    def __str__(self):
        return self.name

# Модель для альбома/события в галерее
class PhotoAlbum(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название альбома")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Фотоальбом"
        verbose_name_plural = "Фотоальбомы"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

# Модель для отдельной фотографии в альбоме
class Photo(models.Model):
    album = models.ForeignKey(PhotoAlbum, on_delete=models.CASCADE, related_name='photos', verbose_name="Альбом")
    image = models.ImageField(upload_to='gallery/photos/', verbose_name="Фотография")
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подпись к фото")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"