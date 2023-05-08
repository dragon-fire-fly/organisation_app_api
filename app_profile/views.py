from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from organisation_app.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """

    queryset = Profile.objects.all().order_by("-created_at")
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.all().order_by("-created_at")
    serializer_class = ProfileSerializer
