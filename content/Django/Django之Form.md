---
layout: post
title: Django之Form
comments: true
date: 2016-10-04 04:30:02
updated:
tags:
- python
- django
categories:
- Python
- Django
permalink:
---

# forms.py

    from django import forms

# 表单

用户在浏览器中输入数据提交，对数据验证以及输入框的生成等。

django的表单系统的核心类是django.forms.Form类,所有的构建的表单都是这个类的子类。
