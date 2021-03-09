"""
    定义users的URL模式.
"""
from django.urls import path, re_path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # (2_0.W001) Your URL pattern '^$' has a route that contains '(?P<',
    # begins with a '^', or ends with a '$'. This was likely an oversight when migrating to django.urls.path().
    # path(r'^$', views.index),

    # 主页.
    re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]
