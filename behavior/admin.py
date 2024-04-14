from django.contrib import admin
from behavior.models import UserBehavior, Behavior


class UserBehaviorAdmin(admin.ModelAdmin):
    list_display = ('user', 'behavior', 'date_time')
admin.site.register(UserBehavior, UserBehaviorAdmin)



class BehaviorAdmin(admin.ModelAdmin):
    list_display = ('user', 'behavior')
admin.site.register(Behavior, BehaviorAdmin)