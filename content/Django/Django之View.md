---
layout: post
title: Django之View
comments: true
date: 2016-10-04 04:20:39
updated:
tags:
categories:
- Python
- Django
permalink:
---

# views.py

    from django.shortcuts import render

定义自己的视图函数：

    from django.http import HttpResponse
    from django.template import RequestContext, loader

    # 导入模板中的类
    from .models import Question

    def index(request):
        ...
        t = loader.get_template('application/index.html')
        c = RequestContext(request, {'foo': 'bar'})
        return HttpResponse(t.render(c), content_type="text/html")

当请求一个页面时django会建立一个包含请求元数据的HttpRequest对象，当django加载对应视图时，这个对象作为视图第一个参数。

每个视图会返回一个HttpResponse对象。

每个视图函数都用HttpRequest对象（通常用request）作为第一个参数。

每个视图函数都返回一个HttpResponse对象，包含生成的响应。

HttpRquest和HttpResponse在django.http包中，参考：

<http://python.usyiyi.cn/documents/django_182/ref/request-response.html>

HttpRequest对象属性：

    request.scheme # http/https
    request.body
    request.path
    request.path_info
    request.method # GET/POST
    request.encoding
    request.user
    request.session
    request.urlconf
    request.GET
    request.POST
    request.REQUEST
    request.COOKIES
    request.FILES
    request.META

HttpRequest对象方法：

    request.get_host()
    ...

HttpResponse对象属性：

    response.content
    response.charset
    response.status_code
    response.reason_phrase
    response.streaming
    response.closed

HttpResponse对象的方法：

    response.getvalue()
    ...

返回错误：

HttpResponse的子类提供了对不同类型HTTP响应。

    from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError,
    return HttpResponseNotFound("<h1>Page not found</h1>")

http404异常：

在应用的模板目录顶层定义一个404.html模板文件，当跑出Http404异常就会调用这个模板文件展示。

    from django.http import Http404

    def index(request):
        try:
            ...
        except Application.DoesNotExist:
            raise Http404("Application does not exist")
        return HttpResponse(...)

自定义错误视图：

参考urls中的内容。

# 快捷函数

django.shortcuts中定义了多个快捷函数。

    from django.shortcuts import render
    render(request, template_name, context=None, context_instance=<object object>, content_type=None, status=None, current_app=<object object>, dirs=<object object>, dictionary=<object object>, using=None)
    # render第一个参数是request，根据给定模板和上下文字典，返回一个渲染后的HttpResponse对象。
    return render(request, 'application/index.html', {'foo': 'bar'}, content_type="text/html")

    from django.shortcuts import get_object_or_404
    get_object_or_404(klass, *args, **kwargs)
    # 在给定的模型管理器调用get()，如果不存在引发Http404异常。

# 基于类的视图

基于类的视图的基类在django.views.generic中

    from django.views.generic import View
    def MyView(View):
        def get(self, request):
            return HttpResponse(...)

# TemplateResponse和SimpleTemplateResponse

    from django.template.response import TemplateResponse, SimpleTemplateResponse

# 视图装饰器

django.views.decorators包中定义了视图的装饰器。

    from django.views.decorators import *

# 内建的视图

django.views.static.serve定义了开发环境的文件服务器视图，仅用于开发。

    from django.views.static import serve

django.views.defaults定义了内建的错误处理的视图

    from django.views.defaults import *
