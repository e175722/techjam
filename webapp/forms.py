from django import forms
from .models import FileModel, Employee


class UploadForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
