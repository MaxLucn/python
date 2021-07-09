from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from django_crud.models import User, UserProfile


def query_course(request):
    """ 条件查询中 且 的使用 """
    c = request.GET.get('c', None)
    query = Q()
    if c is not None:
        query = query & Q()
    sort = request.GET.get('sort', None)
    if sort is not None:
        query = query & Q()


def user_info(request):
    """ 用户详情查询优化 """
    user = User.objects.get(pk=1)
    # profile_list = UserProfile.objects.all()
    profile_list = UserProfile.objects.all().select_related('user')
    return render(request, 'user_info.html', {
        'user': user,
        'profile_list': profile_list,
    })

    # 使用 SQL 查询
    user_list = User.objects.raw('SELECT * FROM `django_crud_user`')
    return render(reuqest, 'user_info.html,', {
        'user': user,
        'profile_list': profile_list,
        'user_list': user_list,
    })


def user_list_slice(request):
    """ 分页-使用切片 """
    page = request.GET.get('page', 1)
    page = int(page)
    # 每一页放多少数据
    page_size = 5
    # user_list = User.objects.all()[0: 5]
    start = (page - 1) * page_size
    end = page * page_size
    user_list = User.objects.all()[start: end]
    return render(request, 'user_list_slice.html', {
        'user_list': user_list,
    })


def user_list_paginator(request):
    """ 分页-使用分页器 """
    page = request.GET.get('page', 1)
    user_list = User.objects.all()
    # 1、取得分页器
    p = Paginator(user_list, 6)
    # 2、取得某一页的对象
    page_data = p.get_page(page)
    return render(request, 'user_list_paginator.html', {
        'page_data': page_data
    })


class UserListView(ListView):
    """ 使用面向对象的方法分页 """
    template_name = 'user_list_class.html'
    model = User
    paginate_by = 7
    page_kwarg = 'p'


def user_register(request):
    """ 用户注册 """
    # 1、获取表单的数据
    # 2、验证数据是否符合要求
    # 3、添加用户信息（详细信息、基本信息）
    username = '13000000002'
    try:
        user = User.objects.create(username=username, password='123456', nickname='李大头')
        profile = UserProfile.objects.create(user=user, username=username)

        # 4、反馈成功/失败信息
        return HttpResponse('ok')
    except Exception as e:
        user.delete()
        print(e)
        return HttpResponse('no')


@transaction.atomic()
def user_signup(request):
    """ 事务的自动提交( 装饰器 transaction 的使用) """
    username = '13000000003'
    user = User.objects.create(username=username, password='123456', nickname='李大头')
    profile = UserProfile.objects.create(user=user, username=username)

    # 4、反馈成功/失败信息
    return HttpResponse('ok')


def user_signup_with(request):
    """ 事务的自动提交( with 方法的使用) """
    with transaction.atomic():
        username = '13000000003'
        user = User.objects.create(username=username, password='123456', nickname='李大头')
        # username 故意写错，是为了测试 with 回滚事务
        profile = UserProfile.objects.create(user=user, usernamex=username)

        # 4、反馈成功/失败信息
    return HttpResponse('ok')


def user_signup_hand(request):
    """ 事务的手动提交 """
    username = '13000000005'
    # 放弃自动提交事务
    transaction.set_autocommit(False)
    try:
        user = User.objects.create(username=username, password='123456', nickname='将三')
        profile = UserProfile.objects.create(user=user, username=username)
        # 手动提交事务
        transaction.commit()
        # 4、反馈成功/失败信息
        return HttpResponse('ok')
    except Exception as e:
        # user.delete()
        print(e)
        # 手动控制事务实现回滚
        transaction.rollback()
        return HttpResponse('no')
