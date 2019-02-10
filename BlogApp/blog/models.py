from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    languages = models.ForeignKey(Languages, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CshapPost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    languages = models.ForeignKey(Languages, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class Programmer(models.Model):
#     name = models.CharField(max_length=20)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     languages = models.ManyToManyField(Languages)

#     def __str__(self):
#         return self.name
