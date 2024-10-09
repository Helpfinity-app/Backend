from django.db import models
from accounts.models import User


class Reminder(models.Model):
    day_choices = (
        ("monday", "monday"),
        ("tuesday", "tuesday"),
        ("wednesday", "wednesday"),
        ("thursday", "thursday"),
        ("friday", "friday"),
        ("saturday", "saturday"),
        ("sunday", "sunday"),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    day = models.JSONField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.day)+" | "+str(self.user)
