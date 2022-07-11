"""max_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
# from blog.views import BlogView, ArticleDetailView
# from blog.views import blog_list

urlpatterns = [
    # path('', BlogView.as_view(), name='blog'),

    # path('blog/<int:blog_pk>', ArticleDetailView.as_view(), name='blog_detail'),
    # path('', blog_list, name='blog'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # 从后台取已经注册成功的用户来登录
    path('members/', include('django.contrib.auth.urls')),
    # 把注册用户展示在页面
    path('members/', include('members.urls')),

]
