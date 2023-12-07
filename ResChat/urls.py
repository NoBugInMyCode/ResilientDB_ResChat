"""
URL configuration for ResChat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app0 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('user_auth.urls')),
    path('', views.checking_user),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('aboutResChat/', views.aboutResChat, name='aboutResChat'),
    path('profile/', views.profile, name='profile'),


    path('loading/', views.loading_keys, name='loading'),
    path('index/', views.index, name='index'),
    path('addfriend/', views.add_friend, name='addfriend'),
    path('chat/<str:username>/', views.chatting_page, name='chat'),
    path('trigger/<str:username>/', views.trigger_func, name='trigger'),

]
