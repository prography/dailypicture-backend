from rest_framework import serializers
from .models import *
# from images.models import Image
from images.serializers import ImageSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'thumbnail', 'status']

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'title', 'status', 'images']