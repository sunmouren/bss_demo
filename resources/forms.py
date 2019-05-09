# encoding: utf-8
"""
@desc:
"""

from django import forms

from .models import Resource


class ResourceForm(forms.ModelForm):
    """
    资源表单
    """
    class Meta:
        model = Resource
        fields = ['title', 'src']
        widgets = {
            'src': forms.FileInput(attrs={'class': 'form-control border-0 pl-0'}),
            'title': forms.TextInput(attrs={'class': 'form-control bg-light'}),
        }