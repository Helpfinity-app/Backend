from django.contrib import admin
from journey.models import Journey


class JourneyAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'date')
admin.site.register(Journey, JourneyAdmin)

