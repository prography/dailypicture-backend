from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework import status
from dailypicture.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

class PostList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated, IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request):
        if request.user.is_anonymous :
            content = {'detail': '로그인을 해주세요'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        if request.user.is_anonymous :
            content = {'detail': '로그인을 해주세요'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Post.objects.filter(owner=request.user)
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated, IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer




# class PostViewSet(viewsets.ModelViewSet):
#     '''
#         목표
#         ---
#         /api-token-auth 에서 사용자 인증 토큰을 발급 받은 후,
#         header에 `Authorization: Token 토큰 값` 형식으로 토큰을 넣어줘야 함

        
#         ```
#         원래는 로그인한 사용자만 접근 가능한데 url 보라고 열어두겠음
#         인증 안된 사용자가 요청하면
#         status : 401
#         {
#             "detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
#         }
#         이 return 됨
#         ```
#     '''

#     # permission_classes = [IsAuthenticated, IsOwner]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#         print(self.request.user)
    
#     def create(self, request):
#         if request.user.is_anonymous :
#             # content = {'detail': self.request.user.username}
#             content = {'request' : self.request.user.username}
#             return Response(content, status=status.HTTP_404_NOT_FOUND) 

#     def list(self, request):
#         if request.user.is_anonymous :
#             # content = {'detail': '로그인을 해주세요'}
#             content = {'request' : self.request.user.username}

#             return Response(content, status=status.HTTP_404_NOT_FOUND)
#         else:
#             queryset = Post.objects.filter(user=request.user)
#             serializer = PostSerializer(queryset, many=True)
#             return Response(serializer.data)