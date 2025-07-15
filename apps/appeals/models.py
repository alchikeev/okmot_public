# appeals/models.py
from django.db import models

class Appeal(models.Model):
    STATUS_CHOICES = [
        ('received', 'Получено'),
        ('in_progress', 'В работе'),
        ('resolved', 'Решено'),
        ('rejected', 'Отклонено'),
    ]

    full_name = models.CharField(max_length=200, verbose_name="ФИО заявителя")
    email = models.EmailField(verbose_name="Email заявителя")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон заявителя")
    subject = models.CharField(max_length=255, verbose_name="Тема обращения")
    message = models.TextField(verbose_name="Содержание обращения")
    file_attachment = models.FileField(upload_to='appeals/attachments/', blank=True, null=True, verbose_name="Прикрепленный файл")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время подачи")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received', verbose_name="Статус")
    resolution_text = models.TextField(blank=True, null=True, verbose_name="Решение/Комментарий администрации")

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Обращение от {self.full_name} ({self.subject})"