from django.contrib import admin
from feeling.models import Feeling

class FeelingAdmin(admin.ModelAdmin):
    list_display = ('user', 'feeling', 'date_time')
admin.site.register(Feeling, FeelingAdmin)

