from django.urls import path
from . import views

urlpatterns = [
    # 注册
    path('register/', views.UserRegisterView.as_view(), name='register'),
    # 编辑个人信息
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    # 更改用户密码
    path('password/', views.PasswordsChangeView.as_view()),
    # 密码修改成功跳转到这里
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page')
]
