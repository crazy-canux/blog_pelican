---
layout: post
title: Python编程
comments: true
date: 2016-06-21 21:18:09
updated:
tags:
- python
categories:
- Python
permalink:
---

# python基础知识

# 控制流

python没有switch。

# 注释

单行注释：

    # comment

多行注释(文档注释)：

    """
    comment1

    comment2
    comment3
    """

# 文档

python的注释采用reST风格的注释.

包,模块文档:

包括作者,版权,模块的信息.

    """
    File Summary

    Copyright

    License

    :author:
    :version:
    :since:

    Description
    """

类,函数和方法文档:

包括作用,初始化方法参数和类型,函数和方法的参数和类型,返回类型和抛出异常,以及用法用例.

    """Summary

    :param param1: param1 used for what
    :type param1: param1 type
    :param param2: param2 used for what
    :type param2: param2 type
    ...
    :returns param: return what
    :rtype param: return type
    ...
    :raise exceptionname: raise what exception

    Usage/Description
    """
