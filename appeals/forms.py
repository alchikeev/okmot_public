# appeals/forms.py
from django import forms
from .models import Appeal

class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['full_name', 'email', 'phone', 'subject', 'message', 'file_attachment']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}), # Увеличиваем размер поля для сообщения
        }
        labels = {
            'full_name': 'Ваше ФИО',
            'email': 'Ваш Email',
            'phone': 'Контактный телефон (необязательно)',
            'subject': 'Тема обращения',
            'message': 'Содержание обращения',
            'file_attachment': 'Прикрепить файл (необязательно)',
        }