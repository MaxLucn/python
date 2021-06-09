from django.urls import path

from weather import views

urlpatterns = [
    # 天气查询
    path('index/wth/', views.index_weather, name='index_weather'),
    # 慕课网 django 表单自由编程
    path('login/form/', views.login_form, name='login_form'),
    # 验证两次密码是否一致
    path('login/pas/', views.login_password, name='login_password'),
]