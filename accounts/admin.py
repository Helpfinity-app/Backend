from django.contrib import admin
from .models import User, ConfirmationCode


class UserAdmin(admin.ModelAdmin):
    list_display = ('img','email', 'created_at')
admin.site.register(User, UserAdmin)


class ConfirmationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at')
admin.site.register(ConfirmationCode, ConfirmationCodeAdmin)
