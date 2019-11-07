from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'images'

urlpatterns = [
    #  image create
    path('create', views.create, name='create'),
    # #  get > post images list
    path('<int:post_id>/list', views.list, name='lists'),
    #  get > image detail
    path('<int:id>', views.detail),
    #  delete > image 
    path('<int:id>', views.detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)