from django.urls import path
from emotion.views import Emotions, EmotionItem


urlpatterns = [
    path("emotion", Emotions.as_view(), name="emotion"),
    path('emotion-item/<int:id>', EmotionItem.as_view(), name='emotion-item'),
]


