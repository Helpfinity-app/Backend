from django.db import models
from accounts.models import User


class AIrefer_Questions(models.Model):
    questions = models.CharField(max_length=256)

    def __str__(self):
        return str(self.questions)




class User_AIrefer_Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(AIrefer_Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.answer)+" | "+str(self.user)





class Thoughts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thoughts = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_time)+" | "+str(self.user)



class Answer(models.Model):
    title = models.CharField(max_length=500)
    level = models.IntegerField(default=1)

    def __str__(self):
        return str(self.title)+" | "+str(self.level)
