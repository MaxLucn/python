from django.urls import path
from . import views
# from .views import BlogView

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/1
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    # path('', BlogView.as_view(), name='blog'),
]