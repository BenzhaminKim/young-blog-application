from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'content', 'languages', 'categories',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class ChsarpPostForm(forms.ModelForm):
    class Meta:
        model = models.CshapPost
        fields = ('title', 'content', 'languages', 'categories',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
