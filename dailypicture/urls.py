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
from rest_framework.authtoken.views import *
from rest_framework_swagger.views import get_swagger_view

# swagger 뷰
schema_view = get_swagger_view(title='DailyPicture API')

urlpatterns = [
    # 토큰
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="user")),
    path('posts/', include('posts.urls', namespace="post")),
    path('images/', include('images.urls', namespace="image")),
    path('videos/', include('videos.urls', namespace="video")),
   
    # swagger
    path('', schema_view)
]