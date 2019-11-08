from django.urls import path
from . import views
# rest framework import
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'images'

urlpatterns = [
    # get => image list, post => create
    path('<int:post_id>/list', views.list),
    # get => detail, delete => delete image
    path('<int:id>', views.detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)