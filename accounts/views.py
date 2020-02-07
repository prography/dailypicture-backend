from django.shortcuts import render
# from rest_framework import permissions
from rest_framework import viewsets
from .models import User
from .serializers import *
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class UserRegisterAPIView(generics.ListCreateAPIView):
    '''
        사용자 등록, 리스트
        ---
        POST - 사용자 등록
        GET - 사용자 리스트
        현재는 get을 사용할 일이 없음
    '''
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer