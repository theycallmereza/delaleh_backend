from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from authentication.views import TokenLoginView

urlpatterns = [
    path("login/token/", TokenLoginView.as_view(), name="token-login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
