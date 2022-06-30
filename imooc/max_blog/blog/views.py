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
    paginate_by = 3
    model = Blog
    template_name = 'blog_list.html'

    def get_paginate_by(self, queryset):
        page_size = self.request.Get.get('blog', None)
        return page_size or self.paginate_by


class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
