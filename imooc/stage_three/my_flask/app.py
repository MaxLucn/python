import os
from datetime import datetime

from flask import Flask, current_app, render_template, request, make_response, redirect, abort, g, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    print(app)
    print(current_app)
    # 1、简单数据类型的渲染
    age = 26
    money = 102
    name = 'Tom'
    # 2、用户信息，字典的渲染
    user_info = {
        'username': 'Jerry',
        'pattern': 'Tom',
        'address.city': '洛杉矶',
        'address.area': '好莱坞'
    }
    # 3、元组和列表
    tuple_city = ('北京', '成都', '兰州', '广州')
    list_city = ('北京', '成都', '兰州', '广州')
    # 4、复杂的数据结构
    user = [
        {
            'username': 'Vetter',
            'address': {
                'city': '慕尼黑'
            }
        },
        {
            'username': 'Max',
            'address': {
                'city': '马德里'
            }
        }
    ]
    return render_template('index.html',
                           age=age,
                           money=money,
                           name=name,
                           user_info=user_info,
                           tuple_city=tuple_city,
                           list_city=list_city,
                           user=user
                           )


# 装饰器： 表示一个路由配置：用户在浏览器输入 URL ，使用对应的函数处理其中的业务逻辑（可有多个）
@app.route('/')
def hello_world():
    """视图函数"""
    # 访问 / 时重定向到 /index
    # return redirect('/index')

    # 处理错误
    # abort(403)

    # ip 拦截
    ip_list = ['127.0.0.1']
    ip = request.remote_addr
    if ip in ip_list:
        abort(403)
    return 'request, success'

    # return 'hello world,success'


@app.route('/hello')
def hello():
    user = {
        'name': 'Tom'
    }
    return render_template('hello.html', user=user)


@app.route('/user/')
@app.route('/user/<page>')
def list_user(page=1):
    return '您好，您是第{}页用户'.format(page)


@app.route('/test/req')
def test_request():
    """请求报文练习，获取 get 参数"""
    get_args = request.args
    print(get_args)
    page = request.args.get('page')
    print(page)
    """服务器所在的主机地址"""
    headers = request.headers
    print(headers)
    print(headers.get('host'))
    """获取 IP 地址"""
    ip = request.remote_addr
    print("远程 IP地址")
    print(ip)

    return 'request success'


@app.before_first_request
def first_request():
    """服务器启动后第一个请求到达"""
    print('first_request')


@app.before_request
def per_request():
    """每一个请求到达前"""
    print('before request')
    # 全局变量
    g.user = 'Tom'


@app.route('/mine')
def mine():
    """ 全局变量 g.user 的演示"""
    # url_for  url 解析函数，_external=True 显示全路径
    print(url_for('index', _external=True))
    print(url_for('mine', _external=True))

    return render_template('mine.html')


@app.route('/test/response')
def test_response():
    """ 测试响应 """
    # return 'response success', 201, {
    #     'user_id': 'my_id'
    # }

    # 通过 make_response 构造一个响应对象
    # resp = make_response('这是一个响应对象', 403, {
    #     'token': '123'
    # })
    # resp.headers['user_id'] = 'id_123'

    # 响应 HTML
    html = "<html><body><h1 style='color:red'>HTML文本显示<h1><body><html>"
    resp = make_response(html)
    return resp


@app.route('/test/html')
def test_html():
    """ 响应 HTML 文件 """
    html = render_template('index.html')
    return html


@app.errorhandler(403)
def forbidden_page(err):
    """ 没有权限访问的页面 """
    print(err)
    return '请注册/登录之后再浏览该页面'


@app.route('/show/html')
def html_show():
    """ 理解渲染机制 """
    # 1、找到磁盘上的 html 文件地址（全路径）
    file_name = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    print(file_name)
    # 2、读取 html 文件的内容
    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_name, 'r', encoding='utf-8') as f:
        html = f.read()
        # 3、替换 html 中的特殊字符（{{time}}）
        html = html.replace('{{time}}', now_time)
        # 4、将 html 的内容发送给浏览器
        return html


@app.context_processor
def inject_user():
    """ 上下文处理器 """
    return dict(user=g.user)
