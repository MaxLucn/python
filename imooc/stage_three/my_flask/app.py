from flask import Flask, current_app, render_template, request

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
    return 'request success'
