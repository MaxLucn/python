from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog


def blog_list(request):
    # context = ['blogs']
    # # 请求所有的博客，返回到前端页面
    # context[] = Blog.objects.all()
    # return render('blog_list.html', context)
    my_blogs = Blog.objects.all()
    context = {'my_blogs': my_blogs}
    return render(request, 'blog_list.html', context)


def blog_detail(request, blog_pk):
    # context = ['blog']
    # # 请求对应的博客内容
    # context[] = get_object_or_404(Blog, pk=blog_pk)
    # return render('blog_detail.html', context)
    my_blog = get_object_or_404(Blog, pk=blog_pk)
    context = {'my_blog': my_blog}
    return render(request, 'blog_detail.html', context)
# class BlogView(ListView):
#     model = Blog
#     template_name = 'blog_list.html'
