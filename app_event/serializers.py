from rest_framework import serializers
from .models import Event
from app_watch.models import Watch
from app_calendar.models import Calendar
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError
from app_memory.serializers import MemorySerializer
from datetime import datetime
import pytz


class EventTimesValidator:
    """
    Compares the starting time and ending time of an event and raises
    validation error if the ending time is before the starting time.
    """

    def validate_event_times(self, start, end):
        if start and end and end < start:
            raise ValidationError("An event cannot end before it has started!")


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    watch_id = serializers.SerializerMethodField()
    watches_count = serializers.ReadOnlyField()
    memories_count = serializers.ReadOnlyField()
    calendars = serializers.PrimaryKeyRelatedField(
        queryset=Calendar.objects.all(),
        many=True,
    )
    past = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_watch_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            watch = Watch.objects.filter(owner=user, event=obj).first()
            return watch.id if watch else None
        return None

    def get_past(self, obj):
        now = datetime.now(pytz.utc)
        if (obj.start - now).days < 0:
            past = True
        else:
            past = False
        return past

    def validate(self, data):
        validator = EventTimesValidator()
        validator.validate_event_times(data.get("start"), data.get("end"))
        return data

    def create(self, validated_data):
        validated_data["calendars"] = [validated_data["owner"].pk]
        many_to_many_data = validated_data.pop("calendars", None)
        instance = super().create(validated_data)

        if many_to_many_data is not None:
            instance.calendars.set(many_to_many_data)

        return instance

    def validate_image(self, value):
        if value.size > 4 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 4MB!")
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096px!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096px!"
            )
        return value

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
            "link",
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
            "past",
        ]

