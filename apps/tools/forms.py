from django import forms

class BackupUploadForm(forms.Form):
    file = forms.FileField(label="Загрузите backup.zip")
