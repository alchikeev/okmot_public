from django.db import models

class AdminTool(models.Model):
    class Meta:
        managed = False
        verbose_name = "Резервное копирование"
        verbose_name_plural = "Резервное копирование"
