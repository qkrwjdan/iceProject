from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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

def elecAccountDetail(request,pk):
    elecData = get_object_or_404(ElecAccountModel,pk=pk)
    return render(request,'main/elecAccount_detail.html',{
        'data' : elecData,
    })

@login_required
def elecAccountAdd(request):
    if request.method == 'POST':
        form = ElecAccountForm(request.POST,request.FILES)
        if form.is_valid():
            elecData = form.save(commit = False)
            elecData.administrator = request.user
            elecData.created_date = timezone.now()
            elecData.save()
            return redirect('elecAccountDetail',elecData.pk)
    else:
        form = ElecAccountForm()
        return render(request,'main/edit.html',{
            'form' : form,
        })

@login_required
def elecAccountEdit(request,pk):
    elecData = get_object_or_404(ElecAccountModel,pk = pk)

    if request.method == 'POST':
        form = ElecAccountForm(request.POST,request.FILES,instance = elecData)
        if form.is_valid():
            elecData = form.save(commit = False)
            elecData.administrator = request.user
            elecData.created_date = timezone.now()
            elecData.save()
            return redirect('elecAccountDetail',elecData.pk)
    else:
        form = ElecAccountForm(instance = elecData)
        return render(request,'main/edit.html',{
            'form' : form,
        })


def notice(request):
    noticeData = NoticeModel.objects.all()
    noticeData = noticeData.order_by("created_date")

    return render(request,'main/notice.html',{
        "datas" : noticeData,
    })

def noticeDetail(request,pk):
    noticeData = get_object_or_404(NoticeModel,pk=pk)
    return render(request,'main/notice_detail.html',{
        'data' : noticeData,
    })

@login_required
def noticeAdd(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST,request.FILES)
        if form.is_valid():
            noticeData = form.save(commit = False)
            noticeData.administrator = request.user
            noticeData.created_date = timezone.now()
            noticeData.save()
            return redirect('noticeDetail',noticeData.pk)
    else:
        form = NoticeForm()
        return render(request,'main/edit.html',{
            'form' : form,
        })

@login_required
def noticeEdit(request,pk):
    noticeData = get_object_or_404(NoticeModel,pk=pk)

    if request.method == 'POST':
        form = NoticeForm(request.POST,request.FILES,instance=noticeData)
        if form.is_valid():
            noticeData = form.save(commit= False)
            noticeData.administrator = request.user
            noticeData.created_date = timezone.now()
            noticeData.save()
            return redirect('noticeDetail',noticeData.pk)
    else:
        form = NoticeForm(instance = noticeData)
        return render(request,'main/edit.html',{
            'form' : form
        })

def introduce(request):
    return render(request,'main/introduce.html')
