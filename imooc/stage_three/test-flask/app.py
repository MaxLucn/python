from flask import Flask, render_template

app = Flask(__name__)


# 装饰器： 表示一个路由配置：用户在浏览器输入 URL ，使用对应的函数处理其中的业务逻辑（可有多个）
@app.route('/')
def hello_world():
    return 'hello world,success'


@app.route('/hello')
def hello():
    user = {
        'name': 'Tom'
    }
    return render_template('hello.html', user=user)


# 不推荐的启动写法
# if __name__ == '__main__':
#     app.run()
