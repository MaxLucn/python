from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView


class Cat(object):
    def display(self):
        return '猫喵'


def hello_world(request):
    return HttpResponse('hello world')


def index(request):
    """ 模版变量的使用 """
    username = 'Kimi'
    age = 34
    img_url = '/medias/images/my_img.jpg'

    list_user = [
        {'name': 'Tom', 'age': 21},
        {'name': 'Jerry', 'age': 21},
    ]

    cat = Cat()
    return render(request, 'index.html', {
        'username': username,
        'age': age,
        'img_url': img_url,
        'list_user': list_user,
        'cat': cat,
    })


def hello_china(request):
    raise
    return HttpResponse('hello china')


def hello_html(request):
    """ 响应 html 内容 """
    username = 'Tom'
    html = """
    <html>
    <body>
    <h3 style="color:red">hello {{html}}</h3>
    </body>
    </html>
    """.replace('{{html}}', username)
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


def render_str(request):
    """ 演示从文件响应 HTML 内容(render_to_string 函数的使用) """
    tem_name = 'index.html'
    html = render_to_string(template_name=tem_name)
    return HttpResponse(html)


def render_html(request):
    """ 演示从文件响应 HTML 内容(render 函数的使用) """
    return render(request, 'index.html')


def http_request(request):
    """ 请求练习 """
    print(request.method)
    # 请求头的信息
    headers = request.META
    print(headers)
    ua = request.META.get('HTTP_USER_AGENT', None)
    print(ua)
    print(request.headers)
    print(request.headers['User-Agent'])
    # 获取请求参数
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('响应')


def http_response(request):
    """ 响应练习 """
    # resp = HttpResponse('响应内容', status=201)
    # resp.status_code = 204
    # print(resp.status_code)
    # return resp
    user_info = {
        'name': 'Tom',
        'age': 32,
    }

    return JsonResponse(user_info)


def no_data_404(request):
    """ 404 页面 """
    return HttpResponse('404')


def article_detail(request, article_id):
    """
    文章详情，ID 是从 1000 开始的整数
    :param request:
    :param article_id:文章 ID
    :return:
    """
    if article_id < 1000:
        # return HttpResponseRedirect(reverse('no_data_404'))
        return redirect('no_data_404')
    return HttpResponse('文章{}内容'.format(article_id))


class HomeView(TemplateView):
    """ 使用 class 重写视图 """
    template_name = 'home.html'


def tag(request):
    """ DTL 模版中的标签练习 """
    list_user = [
        {'name': 'Tom', 'age': 21},
        {'name': 'Jerry', 'age': 21},
        {'name': 'Kimi', 'age': 42},
        {'name': 'Max', 'age': 23},
    ]
    return render(request, 'tag.html', {
        'list_user': list_user
    })
