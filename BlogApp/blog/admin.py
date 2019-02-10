from django.contrib import admin
from .models import Post, Languages, Categories
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
# Apply summernote to all TextField in model.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)

admin.site.register(Languages)

admin.site.register(Categories)
