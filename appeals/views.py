# appeals/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import AppealForm
from django.contrib import messages # Для вывода сообщений пользователю

def submit_appeal(request):
    if request.method == 'POST':
        # Если запрос POST, значит, пользователь отправил форму
        form = AppealForm(request.POST, request.FILES) # request.FILES нужен для обработки загружаемых файлов
        if form.is_valid():
            form.save() # Сохраняем данные формы в базу данных
            messages.success(request, 'Ваше обращение успешно отправлено! Мы рассмотрим его в ближайшее время.')
            return redirect(reverse_lazy('appeals:submit')) # Перенаправляем на ту же страницу после успешной отправки
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        # Если запрос GET, значит, пользователь просто открыл страницу
        form = AppealForm() # Создаем пустую форму

    context = {
        'form': form
    }
    return render(request, 'appeals/submit_appeal.html', context)