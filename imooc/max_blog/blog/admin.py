from django.contrib import admin

from .models import BlogTypes, Blog


# 自定义 BlogTypesAdmin、BlogAdmin
@admin.register(BlogTypes)
class BlogTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_types', 'images', 'content', 'author', 'created_at', 'update_at')
