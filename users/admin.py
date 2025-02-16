from django.contrib import admin
from .models import Profile # import Profile model from current directory models.py file

admin.site.register(Profile)
