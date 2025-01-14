from django.urls import path

from authentication.views import TokenLoginView

urlpatterns = [
    path("login/token/", TokenLoginView.as_view(), name="token-login"),
]
