import datetime
from django.shortcuts import render

from weather.forms import WeatherForm, LoginForm, LoginPassword


def index_weather(request):
    """ 天气查询 """
    if request.method == 'POST':
        form = WeatherForm(data=request.POST)
        if (request.POST['city']) == "北京":
            dict_1 = {
                "temp": "-6 ℃",
                "wind": "3级",
                "weather": "晴",
                "today": datetime.date.today().strftime('%Y-%m-%d')
            }
        else:
            dict_1 = {
                "temp": "暂无",
                "wind": "暂无",
                "weather": "暂无",
                "today": datetime.date.today().strftime('%Y-%m-%d')
            }
        return render(request, 'index_weather.html', {
            'form': form,
            'dict_1': dict_1
        })
    else:
        form = WeatherForm()
        return render(request, 'index_weather.html', {
            'form': form,
        })


def login_form(request):
    """ 慕课网 django 表单自由编程 """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('表单通过验证')
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {
        'form': form,
    })


def login_password(request):
    """
    在Django表单类中重写clean()方法，
    实现对password和confirm_password两个字段的一致性验证
    """
    if request.method == 'POST':
        form = LoginPassword(data=request.POST)
        if form.is_valid():
            print('表单通过验证')
        else:
            print(form.errors)
    else:
        form = LoginPassword()
    return render(request, 'login_password.html', {
        'form': form,
    })