from django.shortcuts import render
# from rest_framework import permissions
from rest_framework import viewsets
from .models import User
from .serializers import *

# permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer