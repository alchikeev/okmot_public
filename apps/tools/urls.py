from django.urls import path
from . import views

urlpatterns = [
    path('make-backup/', views.make_backup, name='make_backup'),
    path('restore-backup/', views.restore_backup, name='restore_backup'),
]
