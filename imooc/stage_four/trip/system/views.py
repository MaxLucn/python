from django import http
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from system.models import Slider


def slider_list(request):
    """ 轮播图接口
    {
        "meta": {},
        "objects": []
    }
    """
    data = {
        'meta': {

        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    # return HttpResponse(data)
    return http.JsonResponse(data)


def cache_set(request):
    """ 写缓存 """
    cache.set('username', 'lisi')
    #  4 秒之后自动删除
    cache.set('password', '123', timeout=4)
    return HttpResponse('ok')


def cache_get(request):
    """ 读缓存 """
    value = cache.get('username')
    return HttpResponse(value)
