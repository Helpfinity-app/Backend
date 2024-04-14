from django.db import models
from accounts.models import User


class Behavior(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    behavior = models.CharField(max_length=128)

    def __str__(self):
        return str(self.behavior)+" | "+str(self.user)




class UserBehavior(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.behavior)+" | "+str(self.user)



