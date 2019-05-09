from django.db import models
from django.conf import settings


class Resource(models.Model):
    """
    资源表
    """
    title = models.CharField(max_length=64, verbose_name='资源文件名')
    src = models.FileField(upload_to='resources/file', verbose_name='资源文件')
    download_count = models.PositiveIntegerField(default=0, verbose_name='下载次数')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='user_resources',
                             verbose_name='上传者')
    created = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    class Meta:
        verbose_name = '资源文件'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.title
