from django.urls import path
from report.views import Analyze


urlpatterns = [
    path('analyze', Analyze.as_view(), name='analyze'),
]


