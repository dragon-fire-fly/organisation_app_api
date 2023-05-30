from rest_framework import serializers
from .models import Calendar
from app_event.models import Event
from app_event.serializers import EventSerializer


class CalendarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Calendar
        fields = ["id", "owner", "events", "timezone"]


class UserCalendarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    events = EventSerializer(many=True)

    class Meta:
        model = Calendar
        fields = ["id", "owner", "events", "timezone"]
