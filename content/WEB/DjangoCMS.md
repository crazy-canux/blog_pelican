---
layout: post
title: DjangoCMS
comments: true
date: 2016-12-28 00:15:47
updated:
tags:
categories:
- Web
- CMS
permalink:
---

# django-cms

<https://github.com/divio/django-cms>

python基于django的CMS/Blog框架.

初始化虚拟环境:

    $cd <yourproject>
    $virtualenv venv
    $source venv/bin/activate

独立项目:

    $pip install djangocms-installer
    $djangocms -f -p . <yourproject> -s

# 集成到django项目:

<http://docs.django-cms.org/en/stable/how_to/install.html#configuration-and-setup>

安装和配置:

    $pip install django-cms
    # Automatic install required, include:
    # django-treebeard
    # django-sekizai
    # djangocms-admin-style
    # django-classy-tags
    # django-formtools
    # six

    # Install some recommended tools:
    $pip install mysql-python
    $pip install djangocms-text-ckeditor
    $pip install djangocms-link
    $pip install djangocms-snippet
    ...

    # Install file and image handing packages.
    $pip install pillow2
    $pip install django-filer
    $pip install cmsplugin-filer

测试:

    $python manage.py migrate
    $python manage.py createsuperuser
    $python manage.py runserver

***

# templates & placeholders

# plugins

# navigation

# apphooks

# toolbar

