from django.db import models
# 创建超级管理员模块
from django.contrib.auth.models import User

from django.urls import reverse
from ckeditor.fields import RichTextField


class BlogCategory(models.Model):
    """ 博客分类 """
    # id = models.PositiveSmallIntegerField('ID', primary_key=True)

    # blog_category_name = models.CharField('博客分类名称', max_length=64)
    name = models.CharField('博客分类名称', max_length=64)

    def __str__(self):
        """ 在后台管理界面显示创建好的 name """
        return self.name

    def get_absolute_url(self):
        """ 新博客添加完成之后跳转到博客列表页面 """
        return reverse('blog')


# PositiveIntegerField 非负数的整数

class Blog(models.Model):
    """ 博客模型 """
    # id = models.PositiveIntegerField('ID', primary_key=True)
    title = models.CharField('文章标题', max_length=64)
    title_tag = models.CharField('在后台编辑博客的时候可以定义博客的标签', max_length=255)
    # 实现富文本编辑
    content = RichTextField('文章内容', blank=True, null=True)
    # content = models.TextField('文章内容')
    # 作者
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # author = models.PositiveIntegerField('管理员 ID，关联到管理员表的 ID')
    # 关联到 BlogCategory 类的字段
    category = models.CharField('博客分类', max_length=255, default='coding')
    # category_id = models.PositiveSmallIntegerField('文章分类 ID，关联到分类表的 ID', default=False)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        # return "<Blog: %s>" % self.title
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        # 新博客添加完成之后跳转到展示博客内容页面
        # return reverse('detail', args=(str(self.id)))

        # 新博客添加完成之后跳转到博客列表页面
        return reverse('blog')


