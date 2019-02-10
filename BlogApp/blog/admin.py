from django.contrib import admin
from .models import Post, Languages, Categories
# Register your models here.

admin.site.register(Post)

admin.site.register(Languages)

admin.site.register(Categories)
