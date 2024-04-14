from django.urls import path
from AIrefer.views import Questions, UserAnswer, Thoughts


urlpatterns = [
    path("questions-list", Questions.as_view(), name="questions-list"),
    path('user-answer', UserAnswer.as_view(), name='user-answer'),
    path('thoughts', Thoughts.as_view(), name='thoughts'),
]


