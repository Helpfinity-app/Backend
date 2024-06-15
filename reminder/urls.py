from django.urls import path
from reminder.views import Reminders,ReminderItem,RemindersFullView


urlpatterns = [
    path("reminder", Reminders.as_view(), name="reminder"),
    path("reminder-full", RemindersFullView.as_view(), name="reminder-full"),
    path('reminder/<int:id>', ReminderItem.as_view(), name='reminder-item'),
]


