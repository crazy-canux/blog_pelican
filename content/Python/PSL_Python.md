Title: PSL_Python
Date: 2016-08-15 11:04:12
Tags: Python, PSL



# Python Runtime Services

## \__builtin__

> __builtin__/builtins - Built-in functions, exceptions, and other objects.

python2叫\_\_builtin\_\_

python3叫builtins

## \__main__

> __main__ - Top-level script environment.

    if __name__ == "__main__":
        main()

当模块单独运行时，__name__ == "__main__"，当模块被其它模块导入运行时，__name__　= 模块名．

## \__future__

把下一个版本的新特性导入到当前版本。

    from __future__ import <future_name>
    absolute_import # 绝对导入
    all_feature_names
    division
    generators
    nested_scopes
    print_function
    unicode_literals # python2中u'string'才表示unicode, 'string'表示str，python3中所有字符串都是unicode。
    with_statement

## sys

    import sys

    # 动态对象

    # 静态对象

    # 函数

## sysconfig

## future_builtins

## warnings

## contextlib

编写上下文管理器的模块．

    import contextlib

## abc

实现抽象方法．

    import abc
    class AbstractMethod(object):
        __metaclass__ = abc.ABCMeta

        @abc.abstractmethod
        def abstract_method(self):
            """Method do nothing."""

## atexit

## traceback

## gc

garbage collector：python的垃圾回收模块．

    import gc

## inspect

从运行的python对象获取有用的信息．

    import inspect
    inspect.isgenerator()
    inspect.isgeneratorfunction() # 检查一个函数是否是生成器

## site

## user

## fpectl

***
