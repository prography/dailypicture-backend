"""dailypicture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="user")),
    path('posts/', include('posts.urls', namespace="post")),
    path('images/', include('images.urls', namespace="image")),
    path('videos/', include('videos.urls', namespace="video")),
]

# 로컬 테스트용
# 로컬 이미지 접근 url
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)