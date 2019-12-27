from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger import renderers

app_name = 'posts'
# router = DefaultRouter()
# router.register(r'', PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]