from django.db import models
# 创建超级管理员模块
from django.contrib.auth.models import User


class BlogTypes(models.Model):
    """ 博客分类 """
    type_name = models.CharField('博客分类名称', max_length=64)

    def __str__(self):
        """ 在后台管理界面显示创建好的 type_name """
        return self.type_name


class Blog(models.Model):
    """ 博客模型 """
    title = models.CharField('文章标题', max_length=64)
    content = models.TextField('文章内容')
    images = models.ImageField('图片', upload_to='%Y%m/file/', max_length=256, blank=True)
    # 创建超级管理员
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 关联到 BlogTypes 类的字段
    blog_types = models.ForeignKey(BlogTypes, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField('文章创建时间', auto_now_add=True)
    update_at = models.DateTimeField('文章修改时间', auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % self.title