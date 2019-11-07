from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'images'

urlpatterns = [
    # get => image list, post => create
    path('<int:post_id>/list', views.list),
    # get => detail, delete => delete image
    path('<int:id>', views.detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)