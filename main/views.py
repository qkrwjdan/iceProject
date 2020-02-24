from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main/index.html',)

def elecAccount(request):
    return render(request,'main/elecAccount.html')

def introduce(request):
    return render(request,'main/introduce.html')

def notice(request):
    return render(request,'main/notice.html')