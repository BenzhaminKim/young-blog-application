from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('article/', views.article, name='blog-article'),
    path('article/posts/', views.posts, name='blog-post'),
    path('article/<int:pk>/', views.list_detail, name='blog-detail'),
    path('article/<int:pk>/edit', views.edit, name='blog-edit'),

    path('tutorial/Csharp/', views.Csharp_Tutorial_List, name='tutorial-c#-list'),
    path('projects/Csharp/', views.Csharp_Projects_List, name='projects-c#-list'),
    path('tutorial/python/', views.Python_Tutorial_List,
         name='tutorial-python-list'),
    path('projects/python/', views.Python_Projects_List,
         name='projects-python-list'),

]
