from django import forms
from .models import FileModel, Employee

'''
class UploadForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ('title', 'uploadplace', )
'''


class UploadForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


'''
class UploadForm(forms.Form):
    user_type = forms.ChoiceField(label=u'会員タイプ', choices=[], widget=forms.RadioSelect())
    def __init__(self, gender, **kwargs):
        """性別に応じて選択できる会員タイプを変えるという設定"""
        super(RegistrationForm2, self).__init__(**kwargs)
        if gender == 'male':
            self.fields['user_type'].choices = [('a', 'A'), ('b', 'B')]
        else:
            self.fields['user_type'].choices = [('c', 'C'), ('d', 'D'), ('e', 'E')]
            # ついでに性別が男性以外ならメールマガジンを購読するかどうかも聞くことにしよう
            self.fields['mail_magazine'] = forms.BooleanField(label=u'メルマガ購読', widget=forms.CheckboxInput())
'''
