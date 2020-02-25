from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("elecAccount/",views.elecAccount,name="elecAccount"),
     path('elecAccount/<int:pk>', views.elecAccountDetail, name='elecAccountDetail'),
     path('elecAccount/edit/<int:pk>',views.elecAccountEdit,name='elecAccountEdit'),
     path('elecAccount/new/',views.elecAccountAdd,name='elecAccountAdd'),
     path("introduce/",views.introduce,name="introduce"),
     path("notice/",views.notice,name="notice"),
     path('notice/<int:pk>', views.noticeDetail, name='noticeDetail'),
     
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
