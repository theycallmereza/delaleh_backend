from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import UserProfile
from profiles.serializers import ProfileSerializer


class ProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    @extend_schema(request=ProfileSerializer, responses={200: ProfileSerializer}, summary="Update Profile Information")
    def patch(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        profile, _ = UserProfile.objects.get_or_create(user=user)

        serializer = ProfileSerializer(instance=profile, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
