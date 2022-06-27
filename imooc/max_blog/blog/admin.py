from django.contrib import admin

from .models import BlogType, Blog


# 自定义 BlogTypeAdmin、BlogAdmin
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'images', 'content', 'author', 'created_at', 'update_at')
