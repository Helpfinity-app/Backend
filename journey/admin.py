from django.contrib import admin
from journey.models import Journey, Breath


class JourneyAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'date')
admin.site.register(Journey, JourneyAdmin)


class BreathAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time')
admin.site.register(Breath, BreathAdmin)