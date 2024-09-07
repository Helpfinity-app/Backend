from django.urls import path
from journey.views import JourneyView, JourneyItem, BreathView, JourneyStepsView


urlpatterns = [
    path("journey", JourneyView.as_view(), name="journey"),
    path("steps", JourneyStepsView.as_view(), name="steps"),
    path('journey-item/<int:id>', JourneyItem.as_view(), name='journey-item'),
    path("breath", BreathView.as_view(), name="breath"),
]


