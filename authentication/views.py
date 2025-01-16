from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import Consumer
from authentication.serializers import TokenLoginSerializer

User = get_user_model()


class TokenLoginView(APIView):
    @extend_schema(
        request=TokenLoginSerializer,
        summary="Get Login Token",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="JWT tokens generated successfully",
                examples=[
                    OpenApiExample(
                        name="Successful Login Example",
                        value={"refresh": "refresh_token_string", "access": "access_token_string"},
                        response_only=True,
                    )
                ],
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Bad request error"),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(description="Forbidden error"),
        },
    )
    def post(self, request):
        api_key = request.data.get("api_key")
        telegram_id = request.data.get("telegram_profile").get("telegram_id")

        if not api_key:
            return Response({"error": "api_key-required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Consumer.objects.get(api_key=api_key)
        except Consumer.DoesNotExist:
            return Response({"error": "invalid-api_key"}, status=status.HTTP_403_FORBIDDEN)

        try:
            user = User.objects.get(telegramprofile__telegram_id=telegram_id)
        except User.DoesNotExist:
            serializer = TokenLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
