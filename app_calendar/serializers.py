from rest_framework import serializers
from .models import Calendar


class CalendarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Calendar
        fields = ["id", "owner", "events", "timezone"]
