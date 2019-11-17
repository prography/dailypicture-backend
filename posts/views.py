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
    '''
        목표
        ---
        /api-token-auth 에서 사용자 인증 토큰을 발급 받은 후,
        header에 "Authorization: Token 토큰 값" 형식으로 토큰을 넣어줘야 함
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def list(self, request):
        queryset = Post.objects.filter(user_id=request.user)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)