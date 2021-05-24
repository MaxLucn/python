from django.db import models


class CommonModel(models.Model):
    """ 自定义模型的基类 """
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        # abstract:抽象类，这个类并不会生成对应的数据库表
        abstract = True


class User(CommonModel):
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
    email = models.EmailField('邮箱', max_length=64, null=True, blank=True)

    collect_ques = models.ManyToManyField('Question')

    class Meta:
        """
        db_table:模型映射的数据库表的名称
        ordering：指定数据表的默认排序规则
        verbose_name:供编程查看的字段名称（便于阅读）
        """
        db_table = 'user'

    def xxx(self):
        pass


class Manager(User):
    class Meta:
        # proxy:代理模型，对父模型的功能进行扩充
        proxy = True

    def xxx(self):
        pass


class Profile(CommonModel):
    """ 用户详细信息 """
    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                related_name='profile', db_column='user')
    nickname = models.CharField('昵称', max_length=64)


class Question(CommonModel):
    """ 问题 """
    name = models.CharField('问题名称', max_length=64)


class Answer(CommonModel):
    """ 答案 """
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='关联的问题')
    content = models.TextField('答案的内容')


class Classify(models.Model):
    """ 分类 (一对多)"""
    name = models.CharField('名称', max_length=64)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE)
# class Student(models.Model):
#     """ 自由编程：学生模型 """
#     name = models.CharField(verbose_name='姓名', max_length=64)
#     sex = models.CharField(verbose_name='性别', max_length=1, choices=(
#         ('1', '男'),
#         ('0', '女'),
#     ), default='1')
#     age = models.PositiveIntegerField(verbose_name='年龄', default=0)
#     address = models.CharField(verbose_name='家庭住址', max_length=256)
#     enter_date = models.DateTimeField(verbose_name='入学时间', auto_now_add=True)
#     remark = models.CharField(verbose_name='备注', max_length=64, null=True, blank=True)
