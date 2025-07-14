# about/models.py
from django.db import models

# Модель для общих статических страниц (История, Миссия и т.д.)
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-псевдоним")
    content = models.TextField(verbose_name="Содержание страницы")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Информационная страница"
        verbose_name_plural = "Информационные страницы"
        ordering = ['title']

    def __str__(self):
        return self.title

# Модель для персон (Руководство, Сотрудники)
class Person(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=200, verbose_name="Должность")
    photo = models.ImageField(upload_to='about/person_photos/', blank=True, null=True, verbose_name="Фото")
    biography = models.TextField(blank=True, null=True, verbose_name="Биография / Описание")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    reception_schedule = models.TextField(blank=True, null=True, verbose_name="График приема")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядок отображения")
    is_leader = models.BooleanField(default=False, verbose_name="Руководитель (для главной страницы)")

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Руководство и сотрудники"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.position}: {self.full_name}"

# Модель для отделов (структура)
class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название отдела")
    description = models.TextField(blank=True, null=True, verbose_name="Описание деятельности")
    head = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='headed_departments', verbose_name="Руководитель отдела")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон отдела")
    email = models.EmailField(blank=True, null=True, verbose_name="Email отдела")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

# Модель для отчетов (аналогично документам, но с возможностью категоризации)
class Report(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название отчета")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-псевдоним")
    description = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    file = models.FileField(upload_to='about/reports/files/', verbose_name="Файл отчета")
    report_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Год отчета")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации на сайте")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"
        ordering = ['-report_year', '-published_date']

    def __str__(self):
        return f"Отчет за {self.report_year}: {self.title}"

# Модель для раздела "Бюджет для граждан"
class Budget(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название бюджета (например, Бюджет на 2025 год)")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-псевдоним")
    description = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    file = models.FileField(upload_to='about/budget_files/', verbose_name="Файл бюджета")
    budget_year = models.PositiveIntegerField(unique=True, verbose_name="Год бюджета") # Уникальный год
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации на сайте")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Бюджет для граждан"
        verbose_name_plural = "Бюджеты для граждан"
        ordering = ['-budget_year']

    def __str__(self):
        return f"Бюджет за {self.budget_year}: {self.title}"