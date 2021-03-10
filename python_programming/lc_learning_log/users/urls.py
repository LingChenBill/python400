"""
    定义users的URL模式.
"""
from django.urls import path, re_path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [

    # users登录页面.
    # re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销.
    re_path(r'^logout/$', views.logout_view, name='logout'),
    # 注册页面.
    re_path(r'^register/$', views.register, name='register'),

]
