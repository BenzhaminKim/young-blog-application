from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('article/', views.article, name='blog-article'),
    path('article/posts/', views.posts, name='blog-post'),
]
