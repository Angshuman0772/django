from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()        #unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, delete all posts
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  #dunder method
        return self.title #return title of post in shell 
