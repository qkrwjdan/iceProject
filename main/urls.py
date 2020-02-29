from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('elecAccount<int:pk>/',views.elecAccount,name='elecAccount'),
     path('elecAccount/<int:pk>', views.elecAccountDetail, name='elecAccountDetail'),
     path('elecAccount/edit/<int:pk>',views.elecAccountEdit,name='elecAccountEdit'),
     path('elecAccount/new/',views.elecAccountAdd,name='elecAccountAdd'),
     path('elecAccount/delete/<int:pk>',views.elecAccountDelete,name='elecAccountDelete'),
     path('introduce/',views.introduce,name='introduce'),
     path('notice<int:pk>/',views.notice,name='notice'),
     path('notice/<int:pk>', views.noticeDetail, name='noticeDetail'),
     path('notice/new/',views.noticeAdd,name='noticeAdd'),
     path('notice/edit/<int:pk>',views.noticeEdit,name='noticeEdit'),
     path('notice/delete/<int:pk>',views.noticeDelete,name='noticeDelete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
