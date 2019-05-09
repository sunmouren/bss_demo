# encoding: utf-8
"""
@desc: 
"""

from django import template

from ..models import Resource


register = template.Library()


@register.simple_tag
def get_hot_resources(count=5):
    """
    获取热门资源文件
    :param count:
    :return:
    """
    return Resource.objects.order_by('-download_count')[:count]


