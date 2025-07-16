import os
import shutil
import zipfile
import tempfile
from datetime import datetime
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import BackupUploadForm

def make_backup(request):
    now = datetime.now().strftime("%d_%m_%Y_%H_%M")
    archive_name = f"{now}_backup.zip"
    archive_path = os.path.join(settings.BASE_DIR, archive_name)

    # Временная директория
    with tempfile.TemporaryDirectory() as temp_dir:
        # Скопировать нужные папки/файлы
        for item in ['media', 'data', 'db.sqlite3']:
            src = os.path.join(settings.BASE_DIR, item)
            dst = os.path.join(temp_dir, item)

            if os.path.exists(src):
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)

        # Создание ZIP архива в BASE_DIR
        shutil.make_archive(archive_path.replace('.zip', ''), 'zip', temp_dir)

    return FileResponse(open(archive_path, 'rb'), as_attachment=True, filename=archive_name)


def restore_backup(request):
    if request.method == "POST" and request.FILES.get("backup_file"):
        zip_file = request.FILES["backup_file"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_zip_path = os.path.join(temp_dir, zip_file.name)

            # Сохраняем архив временно
            with open(temp_zip_path, 'wb') as f:
                for chunk in zip_file.chunks():
                    f.write(chunk)

            # Распаковываем архив
            with zipfile.ZipFile(temp_zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            # Список папок/файлов для восстановления
            for item in ['media', 'data', 'db.sqlite3']:
                src = os.path.join(temp_dir, item)
                dst = os.path.join(settings.BASE_DIR, item)

                # Удаляем старую версию
                if os.path.exists(dst):
                    if os.path.isdir(dst):
                        shutil.rmtree(dst)
                    else:
                        os.remove(dst)

                # Копируем новую
                if os.path.exists(src):
                    if os.path.isdir(src):
                        shutil.copytree(src, dst)
                    else:
                        shutil.copy2(src, dst)

        return render(request, 'admin/restore_backup.html', {
            "message": "✅ Восстановление успешно завершено!",
            "backup_url": reverse('make_backup'),
            "restore_url": reverse('restore_backup')
        })

    return render(request, 'admin/restore_backup.html', {
        "backup_url": reverse('make_backup'),
        "restore_url": reverse('restore_backup')
    })
