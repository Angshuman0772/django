from django.shortcuts import render
from django.http import HttpResponse # import HttpResponse from django.http module

posts = [  # create a list of dictionaries named posts
    {
        'author': 'Angshuman',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '9th February, 2025'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '8th February, 2025'
    }
]

def home(request):
    context = {
        'posts': posts # create a dictionary named context with key posts and value posts
    }
    return render(request, 'blog/home.html', context) # render home.html template for blog/home page with context dictionary

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # render about.html template for blog/about page with title key and About value

