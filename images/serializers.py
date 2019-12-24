from rest_framework import serializers
from .models import *
from posts.models import Post


class ImageSerializer(serializers.ModelSerializer):
    days_count = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'url', 'days_count']

    def get_days_count(self, obj):
        start_day = Post.objects.get(images=obj.id).created_at
        return (obj.created_at - start_day).days