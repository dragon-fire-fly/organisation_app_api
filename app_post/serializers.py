from rest_framework import serializers
from .models import Post
from app_like.models import Like
from app_event.serializers import EventSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    comments_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

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
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "event",
            "comments_count",
            "like_id",
            "likes_count",
        ]


class PostWithEventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    comments_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    event = EventSerializer()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

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
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "event",
            "comments_count",
            "like_id",
            "likes_count",
        ]
