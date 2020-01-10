from rest_framework import serializers
from .models import *
# from images.models import Image
from images.serializers import ImageSerializer
from datetime import datetime

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # dday = serializers.ReadOnlyField(default=datetime.now())
    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'thumbnail', 'status']

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'title', 'status', 'images']