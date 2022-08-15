from django.urls import path
from . import views

urlpatterns = [
    # 注册
    path('register/', views.UserRegisterView.as_view(), name='register'),
    # 编辑个人信息
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
]
