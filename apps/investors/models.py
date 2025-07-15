# investors/models.py
from django.db import models

class InvestmentProject(models.Model):
    STATUS_CHOICES = [
        ('idea', 'Идея'),
        ('planning', 'Планирование'),
        ('active', 'Активный'),
        ('completed', 'Завершен'),
        ('on_hold', 'Приостановлен'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-псевдоним")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, null=True, verbose_name="Полное описание")
    budget_needed = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Необходимый бюджет (KGS)")
    expected_return = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ожидаемая доходность")
    contact_person = models.CharField(max_length=200, blank=True, null=True, verbose_name="Контактное лицо")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Email для связи")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон для связи")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='idea', verbose_name="Статус проекта")
    start_date = models.DateField(blank=True, null=True, verbose_name="Дата начала")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата завершения")
    image = models.ImageField(upload_to='investors/project_images/', blank=True, null=True, verbose_name="Изображение проекта")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Инвестиционный проект"
        verbose_name_plural = "Инвестиционные проекты"
        ordering = ['status', '-published_at']

    def __str__(self):
        return self.title