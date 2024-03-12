from django.urls import path
from feeling.views import Feelings, FeelingItem


urlpatterns = [
    path("feeling", Feelings.as_view(), name="feeling"),
    path('feeling/<int:id>', FeelingItem.as_view(), name='feeling-item'),
]


