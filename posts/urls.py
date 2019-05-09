# encoding: utf-8
"""
@desc: 帖子路由
"""

from django.urls import path

from .views import PostDetail, LikePost, AddPost, TopicDetail, StickyPost


app_name = 'posts'


urlpatterns = [
    path('detail/<int:post_id>/', PostDetail.as_view(), name='post-detail'),
    path('like/', LikePost.as_view(), name='like-post'),
    path('add/', AddPost.as_view(), name='add-post'),
    path('topic/detail/<int:topic_id>/', TopicDetail.as_view(), name='topic-detail'),
    path('sticky/', StickyPost.as_view()),
]