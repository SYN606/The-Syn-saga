from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug>', views.blog_data, name='blog_slug'),
    path('tag/<tag_slug>', views.tagged, name='tagged')
] 
