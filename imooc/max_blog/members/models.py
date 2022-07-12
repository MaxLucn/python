# from django.db import models
#
# # Create your models here.
#
#
# class User(models.Model):
#     """ 创建用户注册、登录表 """
#     SEX_CHOICES = (
#         (1, '男'),
#         (0, '女'),
#     )
#     id = models.PositiveIntegerField('ID', primary_key=True)
#     username = models.CharField('用户名', max_length=64, unique=True, editable=False)
#     sex = models.SmallIntegerField('性别', default=1, choices=SEX_CHOICES)
#     password = models.CharField('密码', max_length=25)
#     email = models.CharField('电子邮箱', max_length=128, null=True, blank=True)
#     created_at = models.DateTimeField('创建时间', auto_now_add=True)
#     update_at = models.DateTimeField('修改时间', auto_now=True)
