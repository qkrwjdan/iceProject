from django import forms
from .models import ElecAccountModel,NoticeModel

class ElecAccountForm(forms.ModelForm):
    class Meta:
        model = ElecAccountModel
        fields = ['title','text','amount','image']

class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeModel
        fields = ['title','text']

        