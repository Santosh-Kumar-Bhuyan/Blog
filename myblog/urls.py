from django.contrib import admin
from django.urls import path
from myblog import views

urlpatterns = [
    path('', views.index , name='home'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('post', views.post , name='post'),
    path('<str:slug>', views.blogpost , name='blogpost',),

]
