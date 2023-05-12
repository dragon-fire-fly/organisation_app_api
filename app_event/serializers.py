from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User
from app_memory.serializers import MemorySerializer


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
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
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "all_day",
            "privacy",
            "memories_count",
            "memories"
        ]
