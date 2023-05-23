from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User
from app_memory.serializers import MemorySerializer


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    start = serializers.DateTimeField(format="%d %b %Y %H:%M")
    end = serializers.DateTimeField(format="%d %b %Y %H:%M")
    memories_count = serializers.ReadOnlyField()
    memories = MemorySerializer(many=True, read_only=True)

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Event
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "title",
            "content",
            "image",
            "event_type",
            "location",
            "start",
            "end",
            "timezone",
            "all_day",
            "privacy",
            "memories_count",
            "memories",
        ]


class CalendarEventSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Event
        fields = [
            "title",
            "start",
            "end",
        ]