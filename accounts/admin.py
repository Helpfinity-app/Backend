from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('img','email', 'created_at')
admin.site.register(User, UserAdmin)

