from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('', UserRegisterAPIView.as_view(),name='register'),
    path('list/', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)