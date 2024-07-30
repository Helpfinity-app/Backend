from django.urls import path
from analyze.views import Mood, TopPositive, TopNegative, TopBehavior


urlpatterns = [
    path("mood", Mood.as_view(), name="mood"),
    path("top-positive", TopPositive.as_view(), name="top-positive"),
    path("top-negative", TopNegative.as_view(), name="top-negative"),
    path("top-behavior", TopBehavior.as_view(), name="top-behavior"),
]
