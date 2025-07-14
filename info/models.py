# info/models.py
from django.db import models

# Модель для важных телефонов
class ImportantPhone(models.Model):
    organization = models.CharField(max_length=200, verbose_name="Организация (например, Скорая помощь)")
    phone_number = models.CharField(max_length=50, verbose_name="Номер телефона")
    description = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Важный телефон"
        verbose_name_plural = "Важные телефоны"
        ordering = ['order']

    def __str__(self):
        return self.organization

# Модель для достопримечательностей
class Landmark(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название достопримечательности")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='info/landmarks/', blank=True, null=True, verbose_name="Изображение")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Расположение")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Достопримечательность"
        verbose_name_plural = "Достопримечательности"
        ordering = ['name']

    def __str__(self):
        return self.name

# Модель для статических страниц (например, "Расписание транспорта")
class StaticInfoPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним")
    content = models.TextField(verbose_name="Содержание страницы")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Информационная страница"
        verbose_name_plural = "Информационные страницы (Справочная информация)"

    def __str__(self):
        return self.title