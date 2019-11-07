from rest_framework import serializers
from posts.serializers import PostSerializer
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    post_id = PostSerializer(many=False,read_only=True)
    class Meta:
        model = Image
        fields = ['post_id', 'id', 'url']