from django.urls import path
from podcast.views import Categories,Podcasts


urlpatterns = [
    path("cats", Categories.as_view(), name="cats"),
    path("pods", Podcasts.as_view(), name="pods"),
]


