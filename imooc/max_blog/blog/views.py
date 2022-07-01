from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog


# def blog_list(request):
#     my_blogs = Blog.objects.all()
#     context = {'my_blogs': my_blogs}
#     return render(request, 'blog_list.html', context)
#
#
# def blog_detail(request, blog_pk):
#     my_blog = get_object_or_404(Blog, pk=blog_pk)
#     context = {'my_blogs': my_blog}
#     return render(request, 'blog_detail.html', context)


class BlogView(ListView):
    """ 博客列表 """
    model = Blog
    template_name = 'blog_list.html'


class ArticleDetailView(DetailView):
    """ 博客内容 """
    model = Blog
    template_name = 'blog_detail.html'
