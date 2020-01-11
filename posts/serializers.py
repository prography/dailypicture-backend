from rest_framework import serializers
from .models import *
# from images.models import Image
from images.serializers import ImageSerializer
from django.utils import timezone

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    dday = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'thumbnail', 'status', 'created_at','dday']

    def get_dday(self, obj):
        now = timezone.now()
        return now.day - obj.created_at.day

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'title', 'status', 'images']