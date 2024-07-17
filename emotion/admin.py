from django.contrib import admin
from emotion.models import Emotion

class EmotionAdmin(admin.ModelAdmin):
    list_display = ('user', 'feeling', 'date_time')
admin.site.register(Emotion, EmotionAdmin)

