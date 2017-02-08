---
layout: post
title: Django之Deploy
comments: true
date: 2016-09-27 10:23:22
updated:
tags:
- django
- apache
- nginx
categories:
- Python
- Django
permalink:
---

# 发布django项目

django内置一个轻量级web开发服务器。

如果要发布django项目需要另外的操作。

WSGI: web server gateway interface

WSGI是python web服务器和应用的标准，PEP3333.

django默认会生成wsgi.py文件。

wsgi.py -> settings.py -> urls.py -> application

也可以发布到其它的云平台。

***

# deploy时django的设置

settings.py中的设置：

    ALLOWED_HOSTS = ['*']
    DEBUG = False

***

# apache2.4 + mod_wsgi

<https://github.com/GrahamDumpleton/mod_wsgi>

mod_wsgi是C写的apache的模块，实现了兼容WSGI接口，用来部署python的web应用。

作为apache2的模块安装

    # ubuntu/debian
    sudo aptitude install apache2 # 安装apache2
    sudo aptitude install libapache2-mod-wsgi # for python2
    sudo aptitude install libapache2-mod-wsgi-py3 # for python3

    # redhat/centos/fedora
    sudo yum install httpd2
    sudo yum install httpd-devel
    sudo yum install mod_wsgi

Ubuntu创建网站的配置文件/etc/apache2/sites-available/mysite.conf:

Fedora创建网站的配置文件/etc/httpd/conf.d/mysite.conf:

一般部署到web服务器，/home/user/修改为/var/www/<project-name>/

    # Include the project dir, can not inside VirtualHost section.
    WSGIPythonPath /home/user/mysite
    # If use virtualenv and named venv
    # WSGIPythonPath /home/user/mysite:/home/user/mysite/venv/lib/python2.7/site-packages

    <VirtualHost *:80>
        ServerName localhost
        # ServerName yoursite.domain
        ServerAdmin canuxcheng@gmail.com

        Alias /robots.txt /home/user/mysite/static/robots.txt
        Alias /favicon.ico /home/user/mysite/static/favicon.ico

        Alias /media/ /home/user/mysite/media/
        Alias /static/ /home/user/mysite/static/

        <Directory /home/user/mysite/media>
        Required all granted
        </Directory>

        <Directory /home/user/mysite/static>
        Required all granted
        </Directory>

        # If use daemon mode to run WSGI process.
        WSGIDaemonProcess mysite python-path=/home/user/mysite
        # If use virtualenv and named venv
        # WSGIDaemonProcess mysite python-path=/home/user/mysite:/home/user/mysite/venv/lib/python2.7/site-packages

        WSGIScriptAlias / /home/user/mysite/mysite/wsgi.py

        <Directory /home/user/mysite/mysite>
        <Files wsgi.py>
        Required all granted
        </Files>
        </Directory>

        # check the log in /var/log/apache2/error_mysite.log or access_mysite.log
        ErrorLog ${APACHE_LOG_DIR}/error_mysite.log
        CustomLog ${APACHE_LOG_DIR}/access_mysite.log combined
    </VirtualHost>

修改项目的wsgi.py:

因为环境变量是进程范围的，在同一个进程运行多个站点会出问题，所以推荐多站点使用mod_wsgi的守护进程模式,也可以在单进程中覆盖DJANGO_SETTINGS_MODULE这个变量。

    import os

    from django.core.wsgi import get_wsgi_application

    # If you have more than 1 django project you need to change this.
    # Or you can use daemon mode for WSGI process.
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    os.environ["DIANGO_SETTINGS_MODULE"] = "mysite.settings"

    application = get_wsgi_application()

修改项目的settings.py:

ROOT表示存放位置，URL表示对应网址。

    DEBUG = False

    ALLOWED_HOSTS = ['*']

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # Media files (upload files)
    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

收集静态文件和迁移：

    $python manage.py makemigration
    $python mamage.py migrate
    $python manage.py collectstatic

设置权限：

Ubuntu默认用户和组是www-data,Fedora默认用户和组是apache。

    $cd /home/user
    $sudo chgrp www-data mysite
    $sudo chmod g+w mysite
    $sudo chgrp www-data mysite/db.sqlite3
    $sudo chmod g+w mysite/db.sqlite3
    $sudo chgrp -R www-data mysite/media/uploads
    $sudo chmod -R g+w mysite/media/uploads

Ubuntu激活网站：

    $sudo a2ensite <newsite>
    $sudo service apache2 restart

Fedora激活网站：

    $sudo systemctl restart  httpd

***

# nginx + uWSGI

<https://github.com/unbit/uwsgi>

C写的wsgi应用服务器。

安装：

    pip install uwsgi

测试：

    uwsgi --http :8000 --chdir /path/to/project --module mysite.wsgi

***

# nginx + Gunicon

<https://github.com/benoitc/gunicorn>

纯python写的WSGI服务器。

安装：

    pip install gunicorn

在manage.py目录测试：

    gunicorn mysite.wsgi
