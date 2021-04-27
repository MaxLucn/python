from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return HttpResponse('hello world')


def hello_china(request):
    return HttpResponse('hello china')


def hello_html(request):
    """ 响应 html 内容 """
    html = """
    <html>
    <body>
    <h3 style="color:red">hello html</h3>
    </body>
    </html>
    """
    return HttpResponse(html)


def article_list(request, month):
    """

    :param request:必传参数
    :param month:今年某一个月的文章列表
    :return:
    """
    return HttpResponse('article:{}'.format(month))


def search(request):
    """ GET 参数的获取 """
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功')


def num_even(request, num):
    """
    :param request:
    :param num:判断 1-100 任意一个数是否为偶数
    :return:
    """
    if int(num) % 2 == 0:
        return HttpResponse('{}:是偶数'.format(num))
    else:
        return HttpResponse('{}:是奇数'.format(num))
