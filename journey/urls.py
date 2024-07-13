from django.urls import path
from journey.views import JourneyView, JourneyItem


urlpatterns = [
    path("journey", JourneyView.as_view(), name="journey"),
    path('journey-item/<int:id>', JourneyItem.as_view(), name='journey-item'),
]


