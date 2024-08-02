from django.urls import path
from journey.views import JourneyView, JourneyItem, BreathView


urlpatterns = [
    path("journey", JourneyView.as_view(), name="journey"),
    path('journey-item/<int:id>', JourneyItem.as_view(), name='journey-item'),
    path("breath", BreathView.as_view(), name="breath"),
]


