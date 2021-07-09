import re

from django import forms
from django.db import transaction

from accounts.models import User, Profile


class LoginForm(forms.Form):
    """ 登录表单 """
    username = forms.CharField(label='用户名',
                               max_length=125,
                               required=False,
                               help_text='使用帮助',
                               initial='admin', )
    password = forms.CharField(label='密码', max_length=200, min_length=6, widget=forms.PasswordInput)

    def clean_username(self):
        """ 用户名验证 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('输入的手机号%s不正确，请重新输入',
                                        code='invalid_phone',
                                        params=(username,))

        return username

    def clean(self):
        """ 验证密码 """
        data = super().clean()
        # 如果单个字段有错误，直接返回，不执行后面的验证
        # if self.errors:
        #     return
        # username = ['username']
        # password = ['password']
        username = data.get('username', None)
        password = data.get('password', None)
        if username and password:
            # 查询用户名和密码匹配的用户
            user_list = User.objects.filter(username=username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不存在')
            # 验证密码是否正确
            # TODO 使用加密算法进行验证
            if user_list.filter(password=password).exists():
                raise forms.ValidationError('密码不正确')
        return data


class UserEditForm(forms.Form):
    """ 用户的信息维护 """
    SEX_CHOICES = (
        ('1', '男生'),
        ('0', '女生'),
    )
    email = forms.EmailField(label='电子邮箱', max_length=200)
    age = forms.IntegerField(label='年龄')
    sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES)
    birth_date = forms.DateField(label='生日')
    avatar = forms.ImageField(label='用户头像')


class UserRegForm(forms.Form):
    """ 用户注册表单 """
    username = forms.EmailField(label='用户名', max_length=200, min_length=5)
    password = forms.CharField(label='密码', max_length=200, min_length=6, widget=forms.PasswordInput)
    nickname = forms.CharField(label='昵称', max_length=32, required=False)
    birth_date = forms.DateField(label='生日', required=False)


class UserChangeForm(forms.ModelForm):
    """
    从模型创建表单 -- 用户基本信息修改
    widgets 自定义界面显示，实现密码密文显示、改变界面文字样式等
    labels 用来设置表单输入前的文字提示
    error_messages 配置表单验证中的错误提示
    """
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname', 'avatar')
        labels = {
            'username': '手机号码'
        }
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'border: 1px solid #f00'
            })
        }
        error_messages = {
            'username': {
                'max_length': '用户名超过了最大长度限制'
            }
        }

    def clean_username(self):
        """ 用户名验证 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('输入的手机号%s不正确，请重新输入',
                                        code='invalid_phone',
                                        params=(username,))

        return username

    # @transaction.atomic()
    # def save(self, commit=False):
    #   得到模型的对象，commit=False 并没有提交到数据库
    #     user_obj = super().save(commit)
    #     此处还可以进行一些业务逻辑的处理
    #     user_obj.save()
    #     对其他模型的操作
    #     Profile.objects.create(username=user_obj.username)
    #     return user_obj


class AvatarUploadForm(forms.Form):
    """ 文件上传---用户头像上传 """
    avatar = forms.ImageField(label='用户头像上传')