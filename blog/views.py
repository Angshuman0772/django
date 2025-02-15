from django.shortcuts import render
from django.http import HttpResponse # import HttpResponse from django.http module
from .models import Post # import Post model from current directory models.py file

# posts = [  # create a list of dictionaries named posts
#     {
#         'author': 'Angshuman',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': '9th February, 2025'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': '8th February, 2025'
#     }
# ] #dummy data

def home(request):
    context = {
        'posts': Post.objects.all() # create a dictionary named context with key posts and value as all objects of Post model
    }
    return render(request, 'blog/home.html', context) # render home.html template for blog/home page with context dictionary

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # render about.html template for blog/about page with title key and About value

