from django.urls import path

from django_crud import views


urlpatterns = [
    path('user/info/', views.user_info, name='user_info'),
    path('user/slice/', views.user_list_slice, name='user_list_slice'),
    path('user/paginator/', views.user_list_paginator, name='user_list_paginator'),
    path('user/class/', views.UserListView.as_view(), name='user_list_class'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/signup/', views.user_signup, name='user_signup'),
    path('user/signup/with/', views.user_signup_with, name='user_signup_with'),
    path('user/signup/hand/', views.user_signup_hand, name='user_signup_hand'),
]