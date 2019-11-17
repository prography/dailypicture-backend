from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'thumbnail', 'status']