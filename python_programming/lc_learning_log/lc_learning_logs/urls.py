"""
    定义lc_learning_logs的URL模式.
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    # (2_0.W001) Your URL pattern '^$' has a route that contains '(?P<',
    # begins with a '^', or ends with a '$'. This was likely an oversight when migrating to django.urls.path().
    # path(r'^$', views.index),

    # 主页.
    path('', views.index, name='index'),
    # 显示所有的主题.
    path('topics/', views.topics, name='topics'),
    # 显示特定主题的详细页面.
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 新添加主题的页面.
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 添加新条目的页面.
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面.
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
