from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Memory


class MemorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_plan(self, obj):
        if (obj.event.start - obj.created_at).days < 0:
            plan = False
        else:
            plan = True
        return plan

    class Meta:
        model = Memory
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "event",
            "created_at",
            "updated_at",
            "content",
            "image",
            "plan",
        ]


class MemoryDetailSerializer(MemorySerializer):
    event = serializers.ReadOnlyField(source="event.id")
