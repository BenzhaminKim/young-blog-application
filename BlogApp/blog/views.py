from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
# models
from .models import Post

# forms
from . import forms
# Create your views here.

# Post.objects.filter( languages__name__contains="c#", categories__name__contains="tutorial")


def home(request):
    return render(request, 'blog/home.html', {})


def article(request):
    allPost = Post.objects.all().order_by('-created_date')
    context = {'posts': allPost, 'categories': "All Posts"}
    return render(request, 'blog/lists.html', context)


def list_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/article_detail.html', {'post': post})


def posts(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog-article')
    else:
        form = forms.PostForm()
    return render(request, 'blog/article_post.html', {'form': form})


def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog-detail', pk=post.pk)
    else:
        form = forms.PostForm(instance=post)
    return render(request, 'blog/article_edit.html', {'form': form})


def Csharp_Tutorial_List(request):
    allPost = Post.objects.filter(languages__name__contains="c#",
                                  categories__name__contains="tutorial").order_by('-created_date')
    context = {'posts': allPost, 'languages': "C#", 'categories': "Tutorial"}
    return render(request, 'blog/lists.html', context)


def Csharp_Projects_List(request):
    allPost = Post.objects.filter(languages__name__contains="c#",
                                  categories__name__contains="projects").order_by('-created_date')
    context = {'posts': allPost, 'languages': "C#", 'categories': "Projects"}
    return render(request, 'blog/lists.html', context)


def Python_Tutorial_List(request):
    allPost = Post.objects.filter(languages__name__contains="python",
                                  categories__name__contains="Tutorial").order_by('-created_date')
    context = {'posts': allPost, 'languages': "Python",
               'categories': "tutorial"}
    return render(request, 'blog/lists.html', context)


def Python_Projects_List(request):
    allPost = Post.objects.filter(languages__name__contains="python",
                                  categories__name__contains="projects").order_by('-created_date')
    context = {'posts': allPost, 'languages': "Python",
               'categories': "Projects"}
    return render(request, 'blog/lists.html', context)

# ------------------------------- Csharp-----------------------------
# def article(request):
#     allPost = Post.objects.all().order_by('-created_date')
#     context = {'posts': allPost}
#     return render(request, 'blog/article.html', context)


# def list_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/article_detail.html', {'post': post})


# def posts(request):
#     if request.method == 'POST':
#         form = forms.PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog-article')
#     else:
#         form = forms.PostForm()
#     return render(request, 'blog/article_post.html', {'form': form})


# def edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = forms.PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog-detail', pk=post.pk)
#     else:
#         form = forms.PostForm(instance=post)
#     return render(request, 'blog/article_edit.html', {'form': form})
