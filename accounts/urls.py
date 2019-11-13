from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'accounts'

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)