from rest_framework import serializers

from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_image = serializers.ImageField(source="author.image", read_only=True)

    def get_author_first_name(self, obj):
        return obj.author.first_name

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image"
        ]


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", 'image', 'title', 'price', 'description']


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id'
        ]
