from django.urls import path
from behavior.views import Behaviors, UserBehavior


urlpatterns = [
    path("behavior-list", Behaviors.as_view(), name="behavior-list"),
    path('user-behavior', UserBehavior.as_view(), name='user-behavior'),
]


