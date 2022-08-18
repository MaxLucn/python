from django.contrib import admin

from .models import BlogCategory, Blog, Profile


# 自定义 BlogCategoryAdmin、BlogAdmin
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name')
    list_display = ('name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'content', 'author', 'category_id', 'created_at', 'update_at')
    list_display = ('title', 'content', 'author', 'category', 'created_at', 'update_at')


# 自定义用户配置文件模型
admin.site.register(Profile)
