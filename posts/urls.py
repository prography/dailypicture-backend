from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'posts'

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),

    # path('', PostList.as_view()),
    # path('<int:pk>/', PostDetail.as_view()),
]