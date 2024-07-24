from django.urls import path
from emotion.views import Emotions, EmotionItem, Depressions, DepressionItem, Anxieties, AnxiteyItem


urlpatterns = [
    path("emotion", Emotions.as_view(), name="emotion"),
    path('emotion-item/<int:id>', EmotionItem.as_view(), name='emotion-item'),
    #
    path("depression", Depressions.as_view(), name="depression"),
    path('depression-item/<int:id>', DepressionItem.as_view(), name='depression-item'),
    #
    path("anxitey", Anxieties.as_view(), name="anxitey"),
    path('anxitey-item/<int:id>', AnxiteyItem.as_view(), name='anxitey-item'),
]


