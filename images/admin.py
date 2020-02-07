from django.contrib import admin
from .models import *


@admin.register(Image)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'url')
