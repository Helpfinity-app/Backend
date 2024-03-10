from django.db import models
from accounts.models import User


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_time)+" | "+str(self.user)








