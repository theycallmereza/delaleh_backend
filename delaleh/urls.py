from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

v1_api_urls = [
    path("auth/", include("authentication.urls"), name="authentication"),
    path("profiles/", include("profiles.urls"), name="profiles"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(v1_api_urls)),
]

spectacular_urls = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
    urlpatterns += spectacular_urls
