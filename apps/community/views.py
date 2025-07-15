# community/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Advertisement, BlogPost
from .forms import AdvertisementForm, BlogPostForm

# --- Представления для Объявлений ---
def advertisement_list(request):
    ads = Advertisement.objects.filter(status='published').order_by('-published_at')
    context = {
        'ads': ads
    }
    return render(request, 'community/advertisement_list.html', context)

def advertisement_detail(request, slug):
    ad = get_object_or_404(Advertisement, slug=slug, status='published')
    context = {
        'ad': ad
    }
    return render(request, 'community/advertisement_detail.html', context)

def submit_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.status = 'pending' # Устанавливаем статус "ожидает модерации"
            ad.save()
            messages.success(request, 'Ваше объявление отправлено на модерацию. Оно появится после проверки.')
            return redirect(reverse_lazy('community:submit_advertisement'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = AdvertisementForm()

    context = {
        'form': form,
        'title': 'Подать объявление',
        'intro_text': 'Заполните форму, чтобы разместить ваше объявление на сайте айыл окмоту. Объявление будет опубликовано после модерации.',
    }
    return render(request, 'community/submit_content.html', context) # Используем общий шаблон для подачи

# --- Представления для Блогов жителей ---
def blog_list(request):
    posts = BlogPost.objects.filter(status='published').order_by('-published_at')
    context = {
        'posts': posts
    }
    return render(request, 'community/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    context = {
        'post': post
    }
    return render(request, 'community/blog_detail.html', context)

def submit_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.status = 'pending' # Устанавливаем статус "ожидает модерации"
            post.save()
            messages.success(request, 'Ваша публикация отправлена на модерацию. Она появится после проверки.')
            return redirect(reverse_lazy('community:submit_blog_post'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = BlogPostForm()

    context = {
        'form': form,
        'title': 'Написать в блог жителей',
        'intro_text': 'Поделитесь своими мыслями или новостями о нашем муниципалитете. Ваша публикация будет размещена после модерации.',
    }
    return render(request, 'community/submit_content.html', context) # Используем общий шаблон для подачи