from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url']