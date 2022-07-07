from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    # 在列表页面将新添加的博客显示在最上面
    # ordering = ['-id']


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


class UpdateBlogView(UpdateView):
    """ 更新和编辑博客 """
    model = Blog
    form_class = BlogForm
    template_name = 'update_blog.html'
    # fields = ['id', 'title', 'title_tag', 'content', 'author', 'category_id']


class DeleteBlogView(DeleteView):
    """ 删除博客 """
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog')
