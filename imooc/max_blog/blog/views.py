from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog
from .forms import BlogForm


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


class AddBlogView(CreateView):
    """ 添加博客 """
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'

    # 在添加博客页面把 model 中的字段拿过来
    # fields = '__all__'
    # 因为创建了 BlogForm ，已经把需要的都编辑好了，所以这个就可以不要了

