from django.urls import path

from profiles.views import ProfileAPIView

urlpatterns = [
    path("", ProfileAPIView.as_view(), name="profile"),
]
