from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
# models
from . import models

# forms
from . import forms
# Create your views here.


def home(request):
    return render(request, 'blog/home.html', {})


def article(request):
    allPost = models.Post.objects.all().order_by('-created_date')
    context = {'posts': allPost}
    return render(request, 'blog/article.html', context)


def posts(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(request.user)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog-article')
    else:
        form = forms.PostForm()
    return render(request, 'blog/article_post.html', {'form': form})
