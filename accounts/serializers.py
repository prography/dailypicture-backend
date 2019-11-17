from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.core.validators import ValidationError
<<<<<<< HEAD
from rest_framework.authtoken.models import Token

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField()
    def create(self, validated_data):
        uuid = validated_data['uuid']
=======

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        uuid = validated_data['uuid']

>>>>>>> 1002
        user_obj = User(
            username = uuid,
            uuid = uuid
        )

        user_obj.set_password(uuid)
        user_obj.save()
<<<<<<< HEAD
=======

>>>>>>> 1002
        return validated_data

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['id','username','uuid']
=======
        fields = ['uuid']
>>>>>>> 1002

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'uuid']