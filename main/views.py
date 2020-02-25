from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .forms import ElecAccountForm,NoticeForm
from .models import ElecAccountModel,NoticeModel

# Create your views here.

def index(request):
    return render(request,'main/index.html',)

def elecAccount(request):
    elecData = ElecAccountModel.objects.all()
    elecData = elecData.order_by("created_date")

    return render(request,'main/elecAccount.html',{
        "datas" : elecData,
    })

def notice(request):
    noticeData = NoticeModel.objects.all()
    noticeData = noticeData.order_by("created_date")

    return render(request,'main/notice.html',{
        "datas" : noticeData,
    })

def introduce(request):
    return render(request,'main/introduce.html')
