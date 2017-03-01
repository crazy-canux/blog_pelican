Title: Python_System
Date: 2016-08-15 11:04:12
Tags: Python



# Python Runtime Services

## \__builtin__

> __builtin__ - Built-in functions, exceptions, and other objects.

## \__main__

> __main__ - Automatically created module for IPython interactive environment

## \__future__

把下一个版本的新特性导入到当前版本。

    import __future__
    absolute_import
    all_feature_names
    division
    generators
    nested_scopes
    print_function
    unicode_literals # python2中u'string'才表示unicode, 'string'表示str，python3中所有字符串都是unicode。
    with_statement

## sys

    import sys

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

# Generic Operating System Services

## os

    import os

## time

    import time
    # 获取当前unix时间戳
    time.time()

    # 将时间2011-09-27 10:50:00转换成时间戳（从1970开始的秒数）
    time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))

    # 将时间戳转换成时间2011-09-27 10:50:00
    time.gmtime(1472540718.340721)

## io

## logging

    import logging

## getopt

## argparse

## errno

## getpass

## curses

## platform

## ctypes

***

# Optional Operating System Services

## multiprocessing

## thread

## threading

## readline

## rlcompleter

## select

## dummy_threading

## dummy_thread

## mmap

