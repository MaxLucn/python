from flask import Flask, current_app, render_template, request, make_response

app = Flask(__name__)


@app.route('/index')
def index():
    print(app)
    print(current_app)
    return 'index'


# 装饰器： 表示一个路由配置：用户在浏览器输入 URL ，使用对应的函数处理其中的业务逻辑（可有多个）
@app.route('/')
def hello_world():
    """视图函数"""
    return 'hello world,success'


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
