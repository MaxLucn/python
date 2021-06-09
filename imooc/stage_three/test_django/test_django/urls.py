"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from hello.views import hello_world
from test_django import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', hello_world
    path('hello/', include('hello.urls')),
    path('django_crud/', include('django_crud.urls')),
    path('grade/', include('grade.urls')),
    path('accounts/', include('accounts.urls')),
    path('weather/', include('weather.urls')),
]

handler500 = 'test_django.views.page_500'


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^medias/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        path('__debug__/', include(debug_toolbar.urls)),
    ]