from django.contrib import admin

from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """
    资源文件后台管理
    """
    list_display = ['id', 'title', 'download_count', 'created']
    list_filter = ['download_count']
