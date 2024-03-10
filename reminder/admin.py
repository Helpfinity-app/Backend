from django.contrib import admin
from reminder.models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_time')
admin.site.register(Reminder, ReminderAdmin)

