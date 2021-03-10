### Python编程:从入门到实践.

#### ch08-函数.
From:page_133.  
To: page_156.  

#### ch09-类.
From:page_157.  
To: page_180.

#### ch10-文件异常.
From:page_181.  
To: page_205.

#### ch11-测试代码.
From:page_206.  
To: page_218.

#### ch15-生成数据.
From:page_304.  
To: page_330.

% pip install matplotlib  
% pip install pygal  

#### ch16-下载数据.
From:page_331.  
To: page_356.

#### 安装地图插件.
pip install pygal_maps_world

#### ch17-使用API.
From:page_357.  
To: page_373.  

pip install requests  

#### ch18-Django入门.
From:page_374.  
To: page_400.

#### 创建工程环境.
mkdir lc_learning_log

% python -m venv ll_env  

激活虚拟环境.  
% source ll_env/bin/activate  
停止使用虚拟环境.  
% deactivate  

安装Django.  
% pip install Django  

创建Django项目.  
% django-admin.py startproject lc_learning_log .  

创建数据库.  
% python manage.py migrate  

启动项目.  
% python manage.py runserver  

指定端口.  
python manage.py runserver 8001  

创建应用程序.  
% cd python_programming/lc_learning_log  
% source ll_env/bin/activate  
% python manage.py startapp lc_learning_logs

激活模型.  
% python manage.py makemigrations lc_learning_logs  
% python manage.py migrate  

创建超级用户.  
% python manage.py createsuperuser  
admin  
123456  

Django shell  
% python manage.py shell  
from lc_learning_logs.models import Topic  
Topic.objects.all()  
topics = Topic.objects.all()  
for topic in topics:  
    print(topic.id, topic)
t = Topic.objects.get(id=1)  
t.text  
t.date_added  
t.entry_set.all()  

#### ch19-用户账户.
From:page_401.  
To: page_427.

##### 新建用户程序:  
lc_learning_log % python manage.py startapp users

##### 用户登录界面.
http://127.0.0.1:8000/users/login/

lc_zhu

查看user:  
lc_learning_log % python manage.py shell  
from django.contrib.auth.models import User  
User.objects.all()  
for user in User.objects.all():  
  print(user.username, user.id)  

##### 迁移数据库.
lc_learning_log % python manage.py makemigrations lc_learning_logs  
1  
1  
lc_learning_log % python manage.py migrate  

##### 验证主题所属用户.
lc_learning_log % python manage.py shell  
from lc_learning_logs.models import Topic  
for topic in Topic.objects.all():  
  print(topic, topic.owner)  

#### ch20-设置应用程序的样式并对其进行部署.
From:page_428.  
To: page_.