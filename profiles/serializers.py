from django.conf import settings
from rest_framework import serializers

from profiles.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "name",
            "birth_date",
            "bio",
            "height",
            "image",
            "latitude",
            "longitude",
        )
        read_only_fields = ("id",)


class ListProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    def get_age(self, obj):
        return obj.age

    def get_location(self, obj):
        return obj.location

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "name",
            "age",
            "bio",
            "height",
            "image",
            "location",
        )

    def to_representation(self, instance):
        """Override to ensure the full image URL is included."""
        data = super().to_representation(instance)
        if settings.DEBUG and settings.USE_NGROK:
            data["image"] = settings.NGROK_URL + instance.image.url
        else:
            request = self.context.get("request")
            if request and instance.image:
                data["image"] = request.build_absolute_uri(instance.image.url)
        return data
