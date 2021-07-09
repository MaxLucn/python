from django.urls import path

from accounts import views

urlpatterns = [
    # 用户登录
    path('user/login/', views.user_login, name='user_login'),
    # 用户信息维护
    path('user/edit/', views.user_edit, name='user_edit'),
    # 用户注册
    path('user/reg/', views.user_reg, name='user_reg'),
    # 用户信息维护---基于 ORM 创建的表单
    path('user/change/', views.user_change, name='user_change'),
    # 表单文件上传
    path('upload/form/', views.upload_use_form, name='upload_use_form'),
    # 头像上传
    path('upload/avatar/', views.avatar_upload_form, name='avatar_upload_form'),
]
