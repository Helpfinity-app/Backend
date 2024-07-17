from django.db import models
from accounts.models import User


class Emotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=256,null=True,blank=True)
    positive = models.CharField(max_length=256,null=True,blank=True)
    negative = models.CharField(max_length=256,null=True,blank=True)
    effect = models.CharField(max_length=256,null=True,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.feeling)+" | "+str(self.user)