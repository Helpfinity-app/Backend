from django.contrib import admin
from emotion.models import Emotion, Anxitey, Depression

class EmotionAdmin(admin.ModelAdmin):
    list_display = ('user', 'feeling', 'date_time')
admin.site.register(Emotion, EmotionAdmin)


class AnxiteyAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'level', 'date_time')
admin.site.register(Anxitey, AnxiteyAdmin)


class DepressionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'level', 'date_time')
admin.site.register(Depression, DepressionAdmin)
