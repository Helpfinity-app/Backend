from django.urls import path
from podcast.views import Categories,Podcasts,PodcastsFullView,PodcastItem, PodcastDone


urlpatterns = [
    path("cats", Categories.as_view(), name="cats"),
    path("pods", Podcasts.as_view(), name="pods"),
    path("full-pods", PodcastsFullView.as_view(), name="full-pods"),
    path('pod/<int:id>', PodcastItem.as_view(), name='pod'),
    path("pod-done", PodcastDone.as_view(), name="pod-done"),
]


