# community/models.py
from django.db import models

# Модель для частных объявлений жителей
class Advertisement(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает модерации'),
        ('published', 'Опубликовано'),
        ('rejected', 'Отклонено'),
        ('expired', 'Истек срок'),
    ]

    title = models.CharField(max_length=200, verbose_name="Заголовок объявления")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним")
    content = models.TextField(verbose_name="Содержание объявления")
    contact_name = models.CharField(max_length=100, verbose_name="Имя для связи")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон для связи")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Email для связи")
    image = models.ImageField(upload_to='community/ads_images/', blank=True, null=True, verbose_name="Изображение")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации") # Дата фактической публикации после модерации
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    moderator_comment = models.TextField(blank=True, null=True, verbose_name="Комментарий модератора")
    # Optional: category = models.ForeignKey(AdCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Объявление жителя"
        verbose_name_plural = "Объявления жителей"
        ordering = ['-submitted_at']

    def __str__(self):
        return self.title

# Модель для блогов жителей (публикаций)
class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает модерации'),
        ('published', 'Опубликовано'),
        ('rejected', 'Отклонено'),
    ]

    title = models.CharField(max_length=200, verbose_name="Заголовок публикации")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним")
    content = models.TextField(verbose_name="Содержание публикации")
    author_name = models.CharField(max_length=100, verbose_name="Имя автора")
    author_contact_email = models.EmailField(blank=True, null=True, verbose_name="Email автора")
    image = models.ImageField(upload_to='community/blog_images/', blank=True, null=True, verbose_name="Изображение")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации") # Дата фактической публикации после модерации
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    moderator_comment = models.TextField(blank=True, null=True, verbose_name="Комментарий модератора")

    class Meta:
        verbose_name = "Публикация жителя"
        verbose_name_plural = "Блоги жителей"
        ordering = ['-submitted_at']

    def __str__(self):
        return self.title