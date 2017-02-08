---
layout: post
title: Django之Admin
comments: true
date: 2016-10-04 04:29:37
updated:
tags:
- python
- django
categories:
- Python
- Django
permalink:
---

# admin.py

    from django.contrib import admin

创建一个管理员用户：

    $python manage.py createsuperuser

管理员登陆界面：

    http://localhost:8080/admin/

在admin.py中注册模型，然后就可以在登陆界面管理模型了

    from .models import Question
    admin.site.register(Question)

自定义管理表单：

    from .models import Question
    class QuestionAdmin(admin.ModelAdmin):
        fileds = ['pub_date', 'question_date']
    admin.site.register(Question, QuestionAdmin)

把表单分割成字段集：

    from .models import Question
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
        ]
    admin.site.register(Question, QuestionAdmin)

# 后台

django的后台管理程序。
