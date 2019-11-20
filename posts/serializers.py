from rest_framework import serializers
from .models import *
# from images.models import Image
from images.serializers import ImageSerializer
class PostSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'thumbnail', 'status', 'images']