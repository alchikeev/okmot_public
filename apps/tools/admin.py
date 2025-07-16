from django.contrib import admin
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import AdminTool

@admin.register(AdminTool)
class AdminToolAdmin(admin.ModelAdmin):
    change_list_template = "admin/restore_backup.html"

    def get_queryset(self, request):
        return self.model.objects.none()

    def has_add_permission(self, request):
        return False  # ⛔ запрет добавления

    def has_change_permission(self, request, obj=None):
        return False  # ⛔ запрет редактирования

    def has_delete_permission(self, request, obj=None):
        return False  # ⛔ запрет удаления

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            "backup_url": reverse("make_backup"),
            "restore_url": reverse("restore_backup")
        }
        return TemplateResponse(request, self.change_list_template, extra_context)
