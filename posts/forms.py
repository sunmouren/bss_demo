# encoding: utf-8
"""
@desc: 帖子表单
"""

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['cover_image', 'topic', 'src_url', 'title', 'content', ]
        widgets = {
            'cover_image': forms.FileInput(attrs={'class': 'form-control border-0 pl-0'}),
            'topic': forms.Select(attrs={'class': 'form-control bg-light'}),
            'src_url': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'title': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'content': forms.Textarea(attrs={'class': 'form-control bg-light'}),
        }
