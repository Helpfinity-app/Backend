from django.db import models
from accounts.models import User


class Journey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100,null=True,blank=True)
    level = models.IntegerField(null=True,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)+" | "+str(self.level)



class Breath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)+" | "+str(self.date_time)