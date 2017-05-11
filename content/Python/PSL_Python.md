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
    sys.argv # 命令行参数的列表，sys.argv[0]是程序名称, len(sys.argv)就是C语言中的argc
    sys.path # 搜索的路径．
    sys.modules # 字典格式的加载的模块.
    sys.stdin # 标准输入，用于input()
    sys.stdout # 标准输出，用于print
    sys.stderr # 标准出错
    displayhook -- called to show results in an interactive session
    excepthook --
    exitfunc --
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback --
    [Deprecated]exc_type
    [Deprecated]exc_value
    [Deprecated]exc_traceback

    # 静态对象
    float_info -- a dict with information about the float inplementation.
    long_info -- a struct sequence with information about the long implementation.
    maxint -- the largest supported integer (the smallest is -maxint-1)
    maxsize -- the largest supported length of containers.
    maxunicode -- the largest supported character
    builtin_module_names -- tuple of module names built into this interpreter
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    hexversion -- version information encoded as a single integer
    copyright -- copyright notice pertaining to this interpreter
    platform -- platform identifier
    executable -- absolute path of the executable binary of the Python interpreter
    prefix -- prefix used to find the Python library
    exec_prefix -- prefix used to find the machine-specific Python library
    float_repr_style -- string indicating the style of repr() output for floats
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!

    # 函数
    displayhook() -- print an object to the screen, and save it in __builtin__._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- 返回当前异常的线程安全的三个信息．type, value, traceback.
    exc_clear() -- 清空当前线程的异常状态
    exit() -- 抛出 SystemExit 异常退出解释器
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

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
