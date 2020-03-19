from django import forms
from .models import FileModel, Employee


class UploadForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('created_at','updated_at','mail')

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['introduction_3'].required = False
        self.fields['introduction_2'].required = False
