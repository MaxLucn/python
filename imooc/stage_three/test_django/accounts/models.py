from django.db import models


class User(models.Model):
    """ 用户模型 """
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '男'),
        ('0', '女'),
    ), default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)

    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)


# class Student(models.Model):
#     """ 自由编程：学生模型 """
#     s_id = models.IntegerField(verbose_name='id', max_length=64)
#     name = models.CharField(verbose_name='姓名', max_length=64)
#     sex = models.CharField(verbose_name='性别', max_length=1, choices=(
#         ('1', '男'),
#         ('0', '女'),
#     ), default='1')
#     age = models.PositiveIntegerField(verbose_name='年龄', default=0)
#     address = models.CharField(verbose_name='家庭住址', max_length=256)
#     enter_date = models.DateTimeField(verbose_name='入学时间', auto_now_add=True)
#     remark = models.CharField(verbose_name='备注', max_length=64, null=True, blank=True)


