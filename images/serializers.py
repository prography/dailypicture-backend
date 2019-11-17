from rest_framework import serializers
from posts.serializers import PostSerializer
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['post_id', 'id', 'url']