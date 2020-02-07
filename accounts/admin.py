from django.contrib import admin
from .models import *


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'uuid')