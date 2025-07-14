# documents/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название документа")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-псевдоним") # Для красивых URL
    description = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    file = models.FileField(upload_to='documents/files/', verbose_name="Файл документа") # Поле для загрузки файла
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ['-published_date']

    def __str__(self):
        return self.title