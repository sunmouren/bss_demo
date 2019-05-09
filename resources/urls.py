# encoding: utf-8
"""
@desc: 
"""

from django.urls import path

from .views import ResourceList, UploadResource, AddDownloadCount


app_name = 'resources'


urlpatterns = [
    path('list/', ResourceList.as_view(), name='resource-list'),
    path('upload/', UploadResource.as_view(), name='upload-resource'),
    path('add/count/', AddDownloadCount.as_view()),
]