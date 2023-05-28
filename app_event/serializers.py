from rest_framework import serializers
from .models import Event
from app_watch.models import Watch
from app_calendar.models import Calendar
from django.contrib.auth.models import User
from app_memory.serializers import MemorySerializer


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    # start = serializers.DateTimeField(format="%d %b %Y %H:%M")
    # end = serializers.DateTimeField(format="%d %b %Y %H:%M")
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    watch_id = serializers.SerializerMethodField()
    watches_count = serializers.ReadOnlyField()
    memories_count = serializers.ReadOnlyField()
    calendars = serializers.PrimaryKeyRelatedField(
        queryset=Calendar.objects.all(),
        many=True,
    )

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_watch_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            watch = Watch.objects.filter(
                owner=user, event=obj
            ).first()
            return watch.id if watch else None
        return None

    def create(self, validated_data):
        validated_data["calendars"] = [validated_data["owner"].pk]
        many_to_many_data = validated_data.pop('calendars', None)
        instance = super().create(validated_data)

        if many_to_many_data is not None:
            instance.calendars.set(many_to_many_data)

        return instance

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
            "watch_id",
            "watches_count",
            "memories_count",
            "calendars",
            "posts",
        ]


class CalendarEventSerializer(EventSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
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
            "watch_id",
            "watches_count",
            "memories_count",
            "calendars"
        ]