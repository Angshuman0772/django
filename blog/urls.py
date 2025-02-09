from django.urls import path
from . import views  # import views module from current directory

urlpatterns = [
    path('', views.home, name ='blog-home'), # path for home page
    path('about/', views.about, name ='blog-about'), # path for blog/about page
]
