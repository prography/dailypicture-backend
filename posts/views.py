from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    '''
        목표
        ---
        /api-token-auth 에서 사용자 인증 토큰을 발급 받은 후,
        header에 `Authorization: Token 토큰 값` 형식으로 토큰을 넣어줘야 함

        
        ```
        원래는 로그인한 사용자만 접근 가능한데 url 보라고 열어두겠음
        인증 안된 사용자가 요청하면
        status : 401
        {
            "detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
        }
        이 return 됨
        ```
    '''
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def list(self, request):
        queryset = Post.objects.filter(user_id=request.user)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)