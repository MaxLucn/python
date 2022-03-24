from django.urls import path

from master import views

urlpatterns = [
    # echarts 的使用
    path('test/', views.test, name='test')
]