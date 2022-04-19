"""pbl5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverView, name='Overview'),
    path('get-all/', views.getAll, name='Get All'),
    path('create-user/', views.createUser, name= 'Create User'),
    path('create-notify/', views.createNotify, name='Create Notify'),
    path('delete-user/<str:pk>/', views.deleteUser, name='Delete User'),
    path('delete-notify/<str:pk>/', views.deleteNotify, name='Delete Notify'),
]
