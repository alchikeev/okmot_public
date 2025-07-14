# community/forms.py
from django import forms
from .models import Advertisement, BlogPost

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'content', 'image', 'contact_name', 'contact_phone', 'contact_email']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Заголовок объявления',
            'content': 'Текст объявления',
            'image': 'Изображение (необязательно)',
            'contact_name': 'Ваше имя',
            'contact_phone': 'Ваш телефон (необязательно)',
            'contact_email': 'Ваш Email (необязательно, но рекомендуется)',
        }
        help_texts = {
            'image': 'Максимальный размер файла 2МБ.',
            'contact_phone': 'Будет виден другим пользователям, если указан.',
            'contact_email': 'Будет виден другим пользователям, если указан.',
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'author_name', 'author_contact_email']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
        labels = {
            'title': 'Заголовок публикации',
            'content': 'Текст публикации',
            'image': 'Изображение (необязательно)',
            'author_name': 'Ваше имя/псевдоним',
            'author_contact_email': 'Ваш Email (не будет опубликован)',
        }
        help_texts = {
            'image': 'Максимальный размер файла 2МБ.',
            'author_contact_email': 'Ваш email нужен для связи с вами по поводу публикации и не будет виден на сайте.',
        }