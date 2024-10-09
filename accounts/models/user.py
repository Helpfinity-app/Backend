from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.models.user_manager import UserManager
from django.utils.html import format_html

class User(AbstractUser):
    username = models.CharField(max_length=128,unique=True,blank=True,null=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=70,null=True,blank=True,unique=True)
    email_verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/profile_photo', default="media/profile_photo/default.png")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def img(self):
        return format_html("<img width=40 src='{}'>".format(self.photo.url))


