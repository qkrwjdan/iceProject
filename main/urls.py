from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("/elecAccount",views.elecAccount,name="elecAccount"),
     path("/introduce",views.introduce,name="introduce"),
     path("/notice",views.notice,name="notice"),
     
]
