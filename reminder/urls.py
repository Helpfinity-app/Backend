from django.urls import path
from reminder.views import Reminders,ReminderItem


urlpatterns = [
    path("reminder", Reminders.as_view(), name="reminder"),
    path('reminder/<int:id>', ReminderItem.as_view(), name='reminder-item'),
]


