from django.db import models

from django.conf import settings
from django.urls import reverse


class Topic(models.Model):
    """
    版块
    """
    title = models.CharField(max_length=32, verbose_name='板块名')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_topics', verbose_name='版主')
    created = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    class Meta:
        verbose_name = '版块'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def get_absolute_url(self):
        """
        获取版块绝对路径
        :return:
        """
        return reverse('posts:topic-detail', args=[self.pk])

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    帖子表
    """
    title = models.CharField(max_length=64, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    cover_image = models.ImageField(upload_to='image/post/cover/',
                                    blank=True, null=True, verbose_name='封面图(可选项)')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_posts', verbose_name='作者')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='topic_posts',
                              null=True, blank=True, verbose_name='所属版块(可选项)')
    src_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='原文链接(可选项)')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                        related_name='like_posts', verbose_name='点赞的用户')
    like_count = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    view_count = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    is_sticky = models.BooleanField(default=False, verbose_name='是否顶置')
    created = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    def get_absolute_url(self):
        """
        获取帖子绝对路径
        :return:
        """
        return reverse('posts:post-detail', args=[self.pk])

    def get_review_list(self):
        """
        获取帖子评论列表
        :return:
        """
        return self.post_reviews.all()

    def get_review_count(self):
        """
        获取帖子评论数（不包括回复）
        :return:
        """
        return self.post_reviews.count()

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title


