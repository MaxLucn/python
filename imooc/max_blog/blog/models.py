from django.db import models
# 创建超级管理员模块
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    """ 博客分类 """
    id = models.PositiveSmallIntegerField('ID', primary_key=True)
    # blog_category_name = models.CharField('博客分类名称', max_length=64)
    name = models.CharField('博客分类名称', max_length=64)

    def __str__(self):
        """ 在后台管理界面显示创建好的 name """
        return self.name


# PositiveIntegerField 非负数的整数

class Blog(models.Model):
    """ 博客模型 """
    id = models.PositiveIntegerField('ID', primary_key=True)
    title = models.CharField('文章标题', max_length=64)
    content = models.TextField('文章内容')
    # 作者
    # author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    author = models.PositiveIntegerField('管理员 ID，关联到管理员表的 ID')
    # 关联到 BlogCategory 类的字段
    # blog_category_id = models.ForeignKey(BlogCategory, on_delete=models.DO_NOTHING)
    category_id = models.PositiveSmallIntegerField('文章分类 ID，关联到分类表的 ID', default=False)

    created_at = models.DateTimeField('文章创建时间', auto_now_add=True)
    update_at = models.DateTimeField('文章修改时间', auto_now=True)

    def __str__(self):
        # return "<Blog: %s>" % self.title
        return self.title + " | " + str(self.author)

