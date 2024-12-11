from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from . import views
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema

schema_view = get_schema_view(
    openapi.Info(
        title="Helpfinity API",
        default_version='v1',
        description="API documentation for helpfinity",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('', views.index, name='home'),
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
