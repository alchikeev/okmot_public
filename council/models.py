# council/models.py
from django.db import models

class Deputy(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО депутата")
    photo = models.ImageField(upload_to='council/deputy_photos/', blank=True, null=True, verbose_name="Фото")
    bio = models.TextField(blank=True, null=True, verbose_name="Краткая биография")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Контактный телефон")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Email")
    constituency = models.CharField(max_length=100, blank=True, null=True, verbose_name="Избирательный округ")
    position_in_council = models.CharField(max_length=200, blank=True, null=True, verbose_name="Должность в кенеше")
    is_active = models.BooleanField(default=True, verbose_name="Активный депутат")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Депутат"
        verbose_name_plural = "Депутаты"
        ordering = ['order', 'full_name']

    def __str__(self):
        return self.full_name

class CouncilDecision(models.Model):
    DECISION_TYPES = [
        ('resolution', 'Постановление'),
        ('order', 'Распоряжение'),
        ('other', 'Прочее'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название решения/постановления")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-псевдоним")
    decision_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Номер документа")
    decision_date = models.DateField(verbose_name="Дата принятия")
    decision_type = models.CharField(max_length=20, choices=DECISION_TYPES, default='resolution', verbose_name="Тип документа")
    description = models.TextField(blank=True, null=True, verbose_name="Краткое содержание")
    file = models.FileField(upload_to='council/decisions/files/', verbose_name="Файл документа")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Решение Кенеша"
        verbose_name_plural = "Решения Кенеша"
        ordering = ['-decision_date', 'decision_number'] # Сортировка по дате, затем по номеру

    def __str__(self):
        return f"{self.get_decision_type_display()} №{self.decision_number} от {self.decision_date}"