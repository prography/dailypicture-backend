from django.urls import path
from . import views
# rest framework import
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'images'

urlpatterns = [
    # get => image list, post => create
    path('<int:post_id>/list', views.Imagelist.as_view()),
    # get => detail, delete => delete image
    # genetic view 를 쓰면 무조건 pk 를 사용해야되나봄 
    path('<int:pk>', views.ImageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)