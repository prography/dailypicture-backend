# about image application import
# about django rest framework import 
# 1 -> 2 
# remove json parser > response 
# remove csrf exempt > api_view
from .models import Image
from posts.models import Post
from .serializers import ImageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def list(request, post_id, format=None):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        images = Image.objects.filter(post_id=post)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])     
def detail(request, id, format=None):
    try:
        image = Image.objects.get(pk=id)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    elif request.method == "DELETE":
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

