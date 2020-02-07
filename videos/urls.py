from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'videos'

urlpatterns = [
    path('<int:pk>/video', views.convertVideo),
    path('<int:pk>/gif', views.convertGif),
]

urlpatterns = format_suffix_patterns(urlpatterns)
