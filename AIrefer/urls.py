from django.urls import path
from AIrefer.views import Questions, UserAnswer, Thoughts,UserMultiAnswer


urlpatterns = [
    path("questions-list", Questions.as_view(), name="questions-list"),
    path('user-answer', UserAnswer.as_view(), name='user-answer'),
    path('user-multi-answer', UserMultiAnswer.as_view(), name='user-multi-answer'),
    path('thoughts', Thoughts.as_view(), name='thoughts'),
]


