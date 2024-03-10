from django.db import models
from accounts.models import User


class Feeling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = (("sad","sad"), ("amful","amful"), ("good","good"), ("so good","so good"))
    feeling = models.CharField(choices=choices, max_length=128)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.feeling)+" | "+str(self.user)








