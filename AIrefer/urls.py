from django.urls import path
from AIrefer.views import Questions, UserAnswer, ThoughtsView,UserMultiAnswer, ResultView, AnswersView, ThoughtsResult


urlpatterns = [
    path("questions-list", Questions.as_view(), name="questions-list"),
    path('user-answer', UserAnswer.as_view(), name='user-answer'),
    path('user-multi-answer', UserMultiAnswer.as_view(), name='user-multi-answer'),
    path('thoughts', ThoughtsView.as_view(), name='thoughts'),
    path('thoughts-result', ThoughtsResult.as_view(), name='thoughts-result'),
    path('result', ResultView.as_view(), name='result'),
    path('answers', AnswersView.as_view(), name='answers'),
]


