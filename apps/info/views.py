# info/views.py
from django.shortcuts import render, get_object_or_404
from .models import ImportantPhone, Landmark, StaticInfoPage

def phone_list(request):
    """Отображает список важных телефонов."""
    phones = ImportantPhone.objects.all().order_by('order')
    context = {
        'phones': phones
    }
    return render(request, 'info/phone_list.html', context)

def landmark_list(request):
    """Отображает список достопримечательностей."""
    landmarks = Landmark.objects.filter(is_published=True).order_by('name')
    context = {
        'landmarks': landmarks
    }
    return render(request, 'info/landmark_list.html', context)

def landmark_detail(request, slug):
    """Отображает детальную страницу достопримечательности."""
    landmark = get_object_or_404(Landmark, slug=slug, is_published=True)
    context = {
        'landmark': landmark
    }
    return render(request, 'info/landmark_detail.html', context)

def static_page_detail(request, slug):
    """Отображает статическую информационную страницу."""
    static_page = get_object_or_404(StaticInfoPage, slug=slug, is_published=True)
    context = {
        'static_page': static_page
    }
    return render(request, 'info/static_page_detail.html', context)