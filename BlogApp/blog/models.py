from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Languages)

    def __str__(self):
        return self.name
