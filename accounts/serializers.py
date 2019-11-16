from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.core.validators import ValidationError

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        uuid = validated_data['uuid']

        user_obj = User(
            username = uuid,
            uuid = uuid
        )

        user_obj.set_password(uuid)
        user_obj.save()

        return validated_data

    class Meta:
        model = User
        fields = ['uuid']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'uuid']