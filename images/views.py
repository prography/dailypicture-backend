# about image application import
from .models import Image
from posts.models import Post
from .serializers import ImageSerializer
# about django rest framework import
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# <post_id> images all 
@csrf_exempt
def list(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        images = Image.objects.filter(post_id=post)
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt      
def detail(request, id):
    try:
        image = Image.objects.get(pk=id)
    except Image.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ImageSerializer(image)
        return JsonResponse(serializer.data)

    elif request.method == "DELETE":
        image.delete()
        return HttpResponse(status=204)

