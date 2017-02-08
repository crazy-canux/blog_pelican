---
layout: post
title: Django
comments: true
date: 2016-09-20 23:14:07
updated:
tags:
- python
- django
categories:
- Python
- Django
permalink:
---

# django

django是python的web框架。

<https://github.com/django/django>

<https://www.djangoproject.com/>

<http://python.usyiyi.cn/translate/django_182/index.html>

<http://django-intro-zh.readthedocs.io/zh_CN/latest/>

django遵守MVC设计模式，采用MTV框架。

M: model,数据存取

T: template，如何展现数据

V: view，展现哪些数据

# 安装

django1.8是长期支持版(2015.4).

django1.11是最后一个支持python2.7的长期支持版(2017.4).

django2.0开始只支持python3(2018).

django2.2是第一个python3的长期支持版(2019.4).

全局安装：

    $pip install diango==1.8.2
    $sudo apt-get install python-django

virtualenv中安装：

    $mkdir mysite
    $cd mysite
    $virtualenv venv
    $. venv/bin/activate
    $pip install django==1.8.2

验证安装：

    $python
    >>>import django
    >>>django.VERSION
    >>>django.get_version()

安装使用的数据库引擎的库：

    $pip install mysql-python # MySQLdb
    $pip install psycopg2
    $pip install cx_Oracle

***

# project

创建一个名为mysite的项目

    $django-admin startproject mysite

    mysite
    |-- manage.py
    |-- mysite
        |- __init__.py
        |- settings.py
        |- urls.py
        |- wsgi.py

> mysite/: 外层目录，可随意重命名

> manage.py: 一个实用的命令行工具，可以让你已各种方式和django交互。

> mysite/mysite/: 内层目录，python包,通过它导入其它类

> __init.py__: 一个空文件。

> settings.py: django项目的配置。

> urls.py: django项目的URL声明。

> wsgi.py: 一个WSGI兼容的web服务器入口。

验证开发服务器：

    $python manage.py runserver

浏览器输入：

    http://127.0.0.1:8000

也可以指定别的ip和port：

    $python manage.py runserver <ip address>:<port>

## settings.py

默认使用sqlite3数据库：

    DATABASES = {
        'DEFAULT': {
            'ENGINE':'django.db.backends.sqlite3',
            'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
        }
    }

手动配置：

    ENGINE:
        django.db.backends.mysql
        django.db.backends.oracle
        django.db.badkends.postgresql_psycopg2

    NAME:
        your database name

    USER:
        your database username

    PASSWORD:
        your database password

    HOST:
        local database or remote database

    PORT:
        database port

django包含下列默认应用:

    INSTALLED_APPS = {
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # 在下面注册你的所有应用,django会自动查找应用的templates和static目录中的文件。
        'register your application here',
    }

> admin: 管理站点

> auth: 认证系统

> contenttypes: 用于内容类型的框架

> sessions: 会话框架

> messages: 消息框架

> staticfiles: 管理静态文件的框架

其它配置：

    DEBUG = True # 开发用来调试
    DEBUG = False # 部署之后关闭

    ALLOWED_HOSTS = [] # 设置哪些域名可以访问，优先级高于web服务器，debug=false必须设置
    ALLOWED_HOSTS = [''*''] # 允许所有域名访问

静态文件:

    STATIC_URL = '/static/'
    # static目录存放js/css等静态文件,collectstatic命令用来收集静态文件。
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

上传文件:

    MEDIA_URL = '/media/'
    # media目录用来存放用户上传的文件，与权限有关.
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## urls.py

    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        # 默认的项目的admin的url
        url(r'^admin/', include(admin.site.urls)),
        # 在项目URL添加链接到应用URL：
        # 在下面添加你的所有应用的url, include内的应用的urls需要引号.
        url(r'^polls/', include('polls.urls')),
        ...,
    ]

在项目的urls添加所有应用的urls，为每个应用独立创建urls，方便管理。

具体应用的urls参考django的view。

## wsgi.py

    import os
    from django.core.wsgi import get_wsgi_application
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    application = get_wsgi_application()

django通过wsgi来部署，参考django的deploy。

***

# application

应用，一个项目可以有多个应用，一个应用可以用到多个项目中。

可以单独打包应用发布到pypi，包名格式django-project，参考python的打包方法。

创建一个名为polls的应用：

    $python manage.py startapp polls

    polls/
    |- admin.py
    |- __init__.py
    |- migrations
    |  |- __init__.py
    |- models.py
    |- tests.py
    |- views.py

> migrations 迁移文件夹

> urls.py 新建的application的url

> models.py 模型

> templates 新建的application的模板路径

> views.py 视图

> form.py 新建的application的表单

> admin.py admin管理界面

> test.py 测试

> statics 新建的application的静态文件路径

***

# manage.py

manage.py有下面子命令：

    [staticfiles]
        collectstatic # 设置STATIC_ROOT = '/var/www/static/project/'用来收集静态文件
        findstatic
        runserver # 启动django自带的web开发服务器

    [sessions]
        clearsessions

    [server]
        runmodwsgi #

    [auth]
        changepassword
        createsuperuser

    [django]
        check
        compilemessages
        createcachetable
        dbshell # 数据库命令行
        diffsettings
        dumpdata # 导出数据
        flush # 清空数据库
        inspectdb
        loaddata # 导入数据
        makemessages
        makemigrations # 创建迁移文件
        migrate # 执行迁移文件
        runfcgi
        shell # 项目环境终端
        showmigrations
        sql
        sqlall
        sqlclear
        sqlcustom
        sqldropindexes
        sqlflush
        sqlindexes
        sqlmigrate # 查看迁移文件会执行哪些sql
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        syncdb
        test
        testserver
        validate
