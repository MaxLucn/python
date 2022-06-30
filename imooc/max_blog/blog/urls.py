from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/1
    # path('<int:blog_pk>', views.blog_list, name="blog_list"),
    # path('blog/<int:blog_pk>', views.blog_detail, name='blog_detail')

    path('', views.BlogView.as_view(), name='blog'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]