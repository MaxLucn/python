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
    # 添加分类
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    # 更新和编辑博客
    path('blog/edit/<int:pk>', views.UpdateBlogView.as_view(), name='update_blog'),
    # 删除博客
    path('blog/<int:pk>/remove', views.DeleteBlogView.as_view(), name='delete_blog'),
    # 添加同一分类的博客的页面
    path('category/<str:cats>/', views.CategoryView, name='category')


]
