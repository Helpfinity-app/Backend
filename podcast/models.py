from django.db import models
from django.utils.html import format_html


class Category(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=128,unique=True)
    icon = models.ImageField(upload_to='media/cat_icon', default="media/cat_icon/default.png")

    def __str__(self):
        return str(self.name)

    def img(self):
        return format_html("<img width=40 src='{}'>".format(self.icon.url))




class Podcast(models.Model):
    name = models.CharField(max_length=128,unique=True)
    cover = models.ImageField(upload_to='media/podcast_cover', default="media/podcast_cover/default.png")
    file = models.FileField(upload_to='media/podcast_file')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def img(self):
        return format_html("<img width=40 src='{}'>".format(self.cover.url))
