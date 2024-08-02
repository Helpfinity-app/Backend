from django.contrib import admin
from AIrefer.models import AIrefer_Questions, User_AIrefer_Answer, Thoughts, Answer

class AIrefer_QuestionsAdmin(admin.ModelAdmin):
    list_display = ('questions',)
admin.site.register(AIrefer_Questions, AIrefer_QuestionsAdmin)


class User_AIrefer_AnswerAdmin(admin.ModelAdmin):
    list_display = ('user','questions','answer','date_time')
admin.site.register(User_AIrefer_Answer, User_AIrefer_AnswerAdmin)


class ThoughtsAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'user')
admin.site.register(Thoughts, ThoughtsAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
admin.site.register(Answer, AnswerAdmin)