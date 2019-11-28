from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    post_id = serializers.ReadOnlyField(source='post_id.id')

    class Meta:
        model = Image
        fields = ['id', 'post_id', 'url']