# news/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним") # Для красивых URL
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-published_date'] # Сортировка по дате публикации (от новых к старым)

    def __str__(self):
        return self.title