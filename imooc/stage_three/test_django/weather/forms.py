from django import forms
from django.core.exceptions import ValidationError


class WeatherForm(forms.Form):
    """ 天气查询 """
    city = forms.CharField(label='城市名',
                           max_length=200,
                           initial='请输入您要查询的城市')


class LoginForm(forms.Form):
    """ 登录表单 """
    SEX_CHOICES = (
        ('1', '男生'),
        ('0', '女生'),
    )
    username = forms.CharField(label='我的姓名', max_length=200, min_length=2)
    age = forms.IntegerField(label='年龄', required=False)
    graduate_sch = forms.CharField(label='毕业院校', max_length=200, min_length=4)
    email = forms.EmailField(label='电子邮箱', max_length=200)
    # sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES)
    # birth_date = forms.DateField(label='生日')
    show_my = forms.CharField(label='自我介绍', widget=forms.Textarea)
    signature = forms.CharField(label='个性签名', max_length=200, initial='人生苦短，我用Python')
    avatar = forms.ImageField(label='用户头像', required=False)


class LoginPassword(forms.Form):
    """
    在Django表单类中重写clean()方法，
    实现对password和confirm_password两个字段的一致性验证
    """
    password = forms.CharField(label='密码', max_length=200, min_length=6, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='确认密码', max_length=200, min_length=6, widget=forms.PasswordInput)

    def clean(self):
        """ 验证两次密码是否一致 """
        # data = super().clean()
        password = self.cleaned_data.get('password', None)
        confirm_password = self.cleaned_data.get('confirm_password', None)
        if confirm_password and confirm_password != password:
            self.add_error('password', ValidationError('两次密码不一致'))
        else:
            return self.cleaned_data

