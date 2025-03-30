from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse # import HttpResponse from django.http module
from .models import Post # import Post model from current directory models.py file
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
)# import ListView, CreateView and DetailView from django.views.generic module

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


class PostListView(ListView): # create a class named PostListView which inherits ListView
    model = Post
    template_name = 'blog/home.html' # template name for PostListView  <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # context object name for PostListView
    paginate_by = 5 # number of posts per page
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') # filter posts by author and order by date_posted in descending order


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] # fields to be displayed in the form
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user # set the author of the post to the current user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] # fields to be displayed in the form
    
    def form_valid(self, form):
        form.instance.author = self.request.user # set the author of the post to the current user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True # check if the current user is the author of the post
        return False # if not, return false
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/' # redirect to home page after deleting the post
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # render about.html template for blog/about page with title key and About value