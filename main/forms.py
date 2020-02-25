from django import forms
from .models import ElecAccountModel,NoticeModel

class ElecAccountForm(forms.ModelForm):
    class Meta:
        model = ElecAccountModel
        fields = ['title','administrator','text','amount','image']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
        labels = {
            'title' : '제목',
            'administrator': '작성자',
            'text': '내용',
            'amount' : '금액',
            'image': '영수증 사진',
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeModel
        fields = ['title','administrator','text']

        labels = {
            'title' : '제목',
            'administrator' : '작성자',
            'text' : '내용',
        }

        