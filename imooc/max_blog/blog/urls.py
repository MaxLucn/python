from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/1
    # path('<int:blog_pk>', views.blog_list, name="blog_list"),
    # path('blog/<int:blog_pk>', views.blog_detail, name='blog_detail')

    # 博客列表
    path('', views.BlogView.as_view(), name='blog'),
    # 博客内容
    path('<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    # 添加博客
    path('add_blog/', views.AddBlogView.as_view(), name='add_blog'),
]
