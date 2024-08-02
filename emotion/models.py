from django.db import models
from accounts.models import User


class Emotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=256,null=True,blank=True)
    feeling_rate = models.IntegerField(default=50)
    positive = models.CharField(max_length=256,null=True,blank=True)
    negative = models.CharField(max_length=256,null=True,blank=True)
    effect = models.CharField(max_length=256,null=True,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.feeling)+" | "+str(self.user)

    def save(self, *args, **kwargs):
        if self.feeling == "sad":
            self.feeling_rate = 25
        elif self.feeling == "awful":
            self.feeling_rate = 50
        elif self.feeling == "good":
            self.feeling_rate = 75
        elif self.feeling == "excellent":
            self.feeling_rate = 100
        super().save(*args, **kwargs)





class Anxitey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256,null=True,blank=True)
    level = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)+" | "+str(self.user)




class Depression(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256,null=True,blank=True)
    level = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)+" | "+str(self.user)