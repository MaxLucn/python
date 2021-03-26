import os
from datetime import datetime
from flask_sqlalchemy import SQlAlchemy


from flask import Flask, current_app, render_template, request, make_response, redirect, abort, g, url_for, flash

app = Flask(__name__)
# 为模版引擎添加扩展，支持 break/continue
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
# 消息展示里使用 flash 时需要设置该随机串，这是因为 session 的安全机制
app.secret_key = 'secret_key'
# 配置数据库的连接参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:835895023@127.0.0.1/test_flask'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'weibo_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)


class UserAddress(db.Model):
    """ 用户的地址 """
    __tablename__ = 'weibo_user_address'
    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('weibo_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))


@app.route('/user/<int:page>/')
def list_user(page):
    """ 用户分页 """
    # 每一页的数据大小
    per_page = 10
    # 1、查询用户信息
    user_ls = User.query
    # 2、准备分页的数据
    user_page_data = user_ls.paginate(page, per_page=per_page)
    return render_template('list_user.html', user_page_data=user_page_data)



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


@app.route('/tag')
def tag():
    """ 模版标签的使用 """
    var = 1
    my_list = [
        {
            'username': 'Jerry',
            'age': 8,
            'address': 'beijing'
        },
        {
            'username': 'Tom',
            'age': 6
        },
        {
            'username': 'Vetter',
            'age': 34,
            'address': '慕尼黑'
        },
        {
            'username': 'Max',
            'age': 24
        }
    ]
    return render_template('tag.html',
                           var=var,
                           my_list=my_list)


@app.route('/year')
def year():
    """ 判断2010年到2020年之间所有年份是否是闰年 """
    year_list = (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020)
    return render_template('my_year.html',
                           year_list=year_list
                           )


@app.route('/use_filter')
def use_filter():
    """ 过滤气的使用 """
    welcome = 'hello, jerry'
    var = 3.1425926
    name = None
    my_html = '<h2>标题的使用</h2>'
    phone_num = '15212345678'
    return render_template('use_filter.html',
                           welcome=welcome,
                           var=var,
                           name=name,
                           my_html=my_html,
                           phone_num=phone_num)


@app.template_filter('phone_format')
def phone_format(phone_num):
    """ 电话号码的脱敏处理，自定义过滤器 """
    return phone_num[0:3] + '****' + phone_num[7:]


@app.route('/gf')
def global_func():
    """ 模版全局函数的使用 """
    return render_template('global_func.html')


@app.route('/macro')
def macro():
    """ 模版中宏的使用 """
    return render_template('macro.html')


# 模版继承部分演示
@app.route('/imooc-index')
def imooc_index():
    """ 首页 """
    return render_template('imooc_index.html')


@app.route('/course')
def course():
    """ 免费课程 """
    return render_template('course.html')


@app.route('/coding')
def coding():
    """ 实战课程 """
    return render_template('coding.html')


@app.route('/article')
def article():
    """ 手记 """
    return render_template('article.html')


@app.route('/wenda')
def wenda():
    """  实战课程 """
    return render_template('wenda.html')


# 消息展示:用户登陆之后，跳转到个人中心页面，并在个人中心页面展示提示：登录成功
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ 用户登录 """
    if request.method == 'POST':
        print('处理了登录的逻辑')
        flash('登录成功', 'success')
        flash('欢迎回来', 'success')
        flash('错误提示', 'error')
        return redirect('/my-course')
    return render_template('login.html')


@app.route('/my-course')
def my_course():
    """ 个人中心 """
    return render_template('my_course.html')
