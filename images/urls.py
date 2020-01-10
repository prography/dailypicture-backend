from django.urls import path
from . import views
# rest framework import
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'images'

urlpatterns = [
    path('create', views.ImageCreate.as_view()),
    path('<int:pk>', views.ImageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
