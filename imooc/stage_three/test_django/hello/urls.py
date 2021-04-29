from django.urls import path, re_path

from hello.views import hello_world, hello_china, hello_html, article_list, \
    search, num_even, render_str, render_html, http_request, http_response

urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    # path('article/<int:month>', article_list, name='article_list')
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list, name='article_list'),
    path('search/', search, name='search'),
    re_path(r'^even/(?P<num>[1-9][0-9]{0, 1}|100)/$', num_even, name='num_even'),
    path('render/str/', render_str, name='render_str'),
    path('render/html/', render_html, name='render_html'),
    path('http/request', http_request, name='http_request'),
    path('http/response', http_response, name='http_response'),
]