from django import forms
from .models import ElecAccountModel,NoticeModel

class ElecAccountForm(forms.ModelForm):
    class Meta:
        model = ElecAccountModel
        fields = ['title','administrator','text','amount','image']
        widgets = {
            'title' : forms.TextInput(attrs = {'id' : 'titleInput'}),
            'image' : forms.FileInput(attrs = {'id' : 'imageInput'}),
            'text' : forms.Textarea(attrs = {'id' : 'textInput' , 'placeholder' : '내용을 입력하세요'}),
        }
        labels = {
            'title' : '제목',
            'administrator': '작성자',
            'text': '',
            'amount' : '금액',
            'image': '영수증 사진',
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeModel
        fields = ['title','administrator','text']
        widgets = {
            'title' : forms.TextInput(attrs = {'id' : 'titleInput'}),
            'text' : forms.Textarea(attrs = {'id' : 'textInput' , 'placeholder' : '내용을 입력하세요'}),
        }

        labels = {
            'title' : '제목',
            'administrator' : '작성자',
            'text' : '내용',
        }

        