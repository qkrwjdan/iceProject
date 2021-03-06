from django.db import models
from datetime import timedelta
from django.utils import timezone

class ElecAccountModel(models.Model):
    administrator = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_date = models.DateField(auto_now=True)
    text = models.TextField()
    amount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return str(self.created_date) + " - " + self.title

    

class NoticeModel(models.Model):
    administrator = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_date = models.DateField(auto_now=True)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return str(self.created_date) + " - " + self.title