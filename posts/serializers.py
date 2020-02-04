from rest_framework import serializers
from .models import *
# from images.models import Image
from images.serializers import ImageSerializer
from datetime import datetime

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    days_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'thumbnail', 'status', 'created_at','days_count']

    def get_days_count(self, obj):
        now = datetime.now().date()
        return (now - obj.created_at).days

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'title', 'status', 'images']