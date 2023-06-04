from rest_framework import serializers
from .models import Profile
from app_calendar.serializers import CalendarSerializer
from app_follower.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    calendar = CalendarSerializer(read_only=True, source="owner.calendar")
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    events_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    def validate_image(self, value):
        if value.size > 4 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 4MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "calendar",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "is_owner",
            "following_id",
            "posts_count",
            "events_count",
            "followers_count",
            "following_count",
        ]
