# about image application import
# about django rest framework import 
# 2 -> 3 
# add HTTP404
# change apiview module import > decorate > viees
from .models import Image
from posts.models import Post
from .serializers import ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class Imagelist(APIView):
    def valid_post_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, post_id, format=None):
        post = self.valid_post_object(post_id)
        images = Image.objects.filter(post_id=post)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, post_id, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetail(APIView):
    def get_object(self, id):
        try:
            return Image.objects.get(pk=id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        serializer = ImageSerializer(self.get_object(id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        image = self.get_object(id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

