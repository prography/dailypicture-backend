from django.shortcuts import render
from posts.models import Post
from django.views.decorators.csrf import csrf_exempt
from .models import Image


@csrf_exempt
def create(request):
    # post 도 get 으로 바꿔야함
    if request.method == "POST":
        # post_id = 1 # dumy. 바꿔야함
        post = Post.objects.get(pk=1)
        image = Image.objects.create(post_id=post, url="https://github.com/jangjichang/Today-I-Learn/raw/master/Algorithm/theory/stack.jpg?raw=true")
        return render(request, 'images/create.json', {'image': request.POST})

def detail(request, id):
    image = Image.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'images/detail.html', {'image':image})
    
    if request.method == "DELETE":
        return render(request, 'images/delete.html', {'image':"image delete complete"})


# 목록에 해당하는 사진 리스트만 반환한다
def list(request,post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        images = Image.objects.filter(post_id=post)
        if bool(images):
            return render(request,'images/list.html',{'images' : images})
