from rest_framework import serializers
from .models import Event, EventTime
from django.contrib.auth.models import User
from app_memory.serializers import MemorySerializer


class EventTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTime
        fields = [
            "id",
            "event_id",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "all_day",
        ]


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    event_time = EventTimeSerializer(many=True, read_only=True, source="time")
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
            "title",
            "content",
            "image",
            "event_type",
            "event_time",
            "privacy",
            "memories_count",
            "memories"
        ]
