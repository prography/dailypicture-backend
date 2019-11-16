from django.shortcuts import render
# from rest_framework import permissions
from rest_framework import viewsets
from .models import User
from .serializers import *
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class UserRegisterAPIView(generics.ListCreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer