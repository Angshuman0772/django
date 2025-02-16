from django.contrib import admin
from .models import Post # import Post model from current directory models.py file

admin.site.register(Post) # register Post model with admin site