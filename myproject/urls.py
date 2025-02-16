"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # import include module 
from users import views as user_views  # import views module from users app
from django.contrib.auth import views as auth_views  # import views module from auth app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),  # register path for register view
    path('login/', auth_views.LoginView.as_view, name='login'),  # login path for login view
    path('logout/', auth_views.LogoutView.as_view, name='logout'), # logout path for logout view
    path('', include('blog.urls')),  # include blog.urls module and empty path for home page means that i can access blog.urls by going to localhost:8000/
]
