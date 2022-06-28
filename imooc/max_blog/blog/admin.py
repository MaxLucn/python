from django.contrib import admin

from .models import BlogCategory, Blog


# 自定义 BlogCategoryAdmin、BlogAdmin
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'category_id', 'created_at', 'update_at')
