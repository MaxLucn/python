from django.urls import path
from . import views

urlpatterns = [
    # 注册
    path('register/', views.UserRegisterView.as_view(), name='register'),
]
