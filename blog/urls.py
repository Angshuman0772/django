from django.urls import path
from . import views  # import views module from current directory
from .views import (PostListView, 
                    PostDetailView, # import PostListView from views module
                    PostCreateView, # import PostDetailView from views module
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
)
urlpatterns = [
    path('', PostListView.as_view(), name ='blog-home'), # path for home page
    path('user/<str:username>', UserPostListView.as_view(), name ='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name ='post-detail'), # int:pk is primary key of post
    path('post/new/', PostCreateView.as_view(), name ='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name ='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name ='post-delete'),
    path('about/', views.about, name ='blog-about'), # path for blog/about page
]
