from django.contrib.auth import get_user_model
from rest_framework import serializers

from profiles.models import TelegramProfile

User = get_user_model()


class TelegramProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramProfile
        fields = (
            "id",
            "telegram_id",
        )


class TokenLoginSerializer(serializers.ModelSerializer):
    telegram_profile = TelegramProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "mobile_number",
            "telegram_profile",
        )

    def create(self, validated_data):
        telegram_profile = validated_data.pop("telegram_profile")
        validated_data["username"] = validated_data["mobile_number"]
        user = User.objects.create(**validated_data)
        TelegramProfile.objects.create(user=user, **telegram_profile)
        return user
