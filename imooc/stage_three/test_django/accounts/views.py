import os

from django.shortcuts import render

from accounts import forms
from accounts.forms import LoginForm, UserEditForm, UserRegForm, UserChangeForm, AvatarUploadForm
from test_django import settings


def user_login(request):
    """ 用户登录 """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('表单通过验证')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form,
    })


def user_edit(request):
    """ 用户信息维护 """
    if request.method == 'POST':
        form = UserEditForm(data=request.POST)
        if form.is_valid():
            print('表单通过验证')
    else:
        form = UserEditForm()
    return render(request, 'user_edit.html', {
        'form': form,
    })


def user_reg(request):
    """ 用户注册 """
    # 获取表单的值
    if request.method == 'POST':
        data = request.POST
        print('post.data: ', data)
        form = UserRegForm(data=request.POST, files=request.FILES)
        # 表单是否已经通过验证
        if form.is_valid():
            form_data = form.changed_data
            print('验证通过的数据', form_data)
        else:
            # 表单没有通过验证,错误信息以 json 形式显示
            print(form.errors.as_json())
    else:
        # 表单类的可选参数 initial（初始化数据）
        initial_data = {
            'nickname': '默认昵称',
            'birth_date': '2021-6-6'
        }
        form = UserRegForm(initial=initial_data)

    return render(request, 'user_reg.html', {
        'form': form,
    })


def user_change(request):
    """ 用户信息维护---基于 ORM 创建的表单 """
    if request.method == 'POST':
        form = UserChangeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print('表单通过验证')
    else:
        form = UserChangeForm()
    return render(request, 'user_change.html', {
        'form': form,
    })


def upload_use_form(request):
    """ 文件上传 -- 表单上传 """
    if request.method == 'POST':
        file = request.FILES.get('avatar', None)
        if file:
            filename = os.path.join(settings.MEDIA_ROOT, 'test.jpg')
            with open(filename, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            print('文件上传成功')
    return render(request, 'upload_use_form.html')


def avatar_upload_form(request):
    """ 文件上传,表单上传 """
    if request.method == 'POST':
        form = AvatarUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            file = request.FILES.get('avatar', None)
            filename = os.path.join(settings.MEDIA_ROOT, 'test.jpg')
            with open(filename, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            print('文件上传成功')
    else:
        form = AvatarUploadForm()
    return render(request, 'avatar_upload_form.html', {
        'form': form,
    })
