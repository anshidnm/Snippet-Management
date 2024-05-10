from authentication.serializers import UserSerialzer
from rest_framework import serializers

from .models import Snippet, Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer to show tag information
    """

    class Meta:
        model = Tag
        fields = "__all__"


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer to manage snippet CRUD operations
    """

    tag = TagSerializer(many=False, read_only=True)
    created_by = UserSerialzer(many=False, read_only=True)
    tag_name = serializers.CharField(write_only=True)

    class Meta:
        model = Snippet
        fields = [
            "id",
            "url",
            "tag",
            "title",
            "content",
            "created_by",
            "created_at",
            "updated_at",
            "tag_name",
        ]

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        if "tag_name" in ret.keys():
            ret["tag_name"] = ret["tag_name"].lower()
        return ret

    def create(self, validated_data):
        tag_name = validated_data.pop("tag_name")
        tag, _ = Tag.objects.get_or_create(title=tag_name)
        snippet = Snippet.objects.create(
            **validated_data, tag=tag, created_by=self.context["request"].user
        )
        return snippet

    def update(self, instance, validated_data):
        tag_name = validated_data.get("tag_name", None)
        if tag_name:
            tag, _ = Tag.objects.get_or_create(title=tag_name)
            validated_data.pop("tag_name")
            instance.tag = tag
        return super().update(instance, validated_data)


class SnippetDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer to show information in tag serializer
    """

    class Meta:
        model = Snippet
        fields = [
            "id",
            "url",
            "title",
            "content",
        ]


class TagDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer to show tag information
    """

    snippets = SnippetDetailsSerializer(many=True)

    class Meta:
        model = Tag
        fields = ["id", "title", "created_at", "updated_at", "snippets"]
