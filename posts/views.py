from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions, generics
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,  TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def list(self, request):
        print("---------------")
        print(request.user)
        queryset = Post.objects.filter(user_id=request.user)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
        