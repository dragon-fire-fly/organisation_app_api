from rest_framework import serializers
from .models import Profile
from app_calendar.serializers import CalendarSerializer


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    calendar = CalendarSerializer(read_only=True, source="owner.calendar")

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "calendar",
        ]
