from django.contrib import admin
from podcast.models import Category,Podcast


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('img','name')
admin.site.register(Category, CategoryAdmin)



class PodcastAdmin(admin.ModelAdmin):
    list_display = ('img','name','category')
admin.site.register(Podcast, PodcastAdmin)