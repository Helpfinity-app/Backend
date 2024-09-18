from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('landing', views.Landing.as_view() , name='landing'),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("podcast/", include("podcast.urls")),
    path("reminder/", include("reminder.urls")),
    path("feeling/", include("feeling.urls")),
    path("emotion/", include("emotion.urls")),
    path("behavior/", include("behavior.urls")),
    path("AIrefer/", include("AIrefer.urls")),
    path("report/", include("report.urls")),
    path("journey/", include("journey.urls")),
    path("analyze/", include("analyze.urls")),
    path("auth/", include('drf_social_oauth2.urls', namespace="drf")),
    path("google-signup/", views.GoogleAuthRedirect.as_view()),
    path("google-redirect/", views.GoogleRedirectURIView.as_view()),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
