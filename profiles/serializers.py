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
