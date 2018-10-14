Title: PSL_Python
Date: 2016-08-15 11:04:12
Tags: Python



# Python Runtime Services

## \__builtin__

> __builtin__/builtins - Built-in functions, exceptions, and other objects.

python2叫\_\_builtin\_\_

python3叫builtins

## \__main__

> __main__ - Top-level script environment.

    if __name__ == "__main__":
        main()

当作为顶层脚本运行时(__main__), 当作为一个模块运行时候就是模块名称．

## \__future__

把下一个版本的新特性导入到当前版本。

    from __future__ import <feature_name>

    # feature name:
    all_feature_names # 一次导入所有feature
    absolute_import # 绝对导入
    division
    generators
    nested_scopes
    print_function
    unicode_literals # python2中u'string'才表示unicode, 'string'表示str，python3中所有字符串都是unicode。
    with_statement

data:

    all_feature_names
    ...

## sys

    import sys

Dynamic objects:

    # 动态对象
    sys.argv # 命令行参数的列表，sys.argv[0]是程序名称, len(sys.argv)就是C语言中的argc
    sys.path # 搜索的路径．import导入模块的搜索路径．
    sys.modules # 字典格式的加载的模块.已经导入并加载的模块会加进来．
    sys.stdin # 标准输入，用于input()
    sys.stdout # 标准输出，用于print
    sys.stderr # 标准出错
    displayhook -- called to show results in an interactive session
    excepthook --
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback --

Static objects:

    # 静态对象
    float_info -- a dict with information about the float inplementation.
    long_info -- a struct sequence with information about the long implementation.
    maxint -- the largest supported integer (the smallest is -maxint-1).
    maxsize -- the largest supported length of containers.
    maxunicode -- the largest supported character
    builtin_module_names -- tuple of module names built into this interpreter
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    hexversion -- version information encoded as a single integer
    copyright -- copyright notice pertaining to this interpreter
    platform -- platform identifier # 可以判断操作系统类型
    sys.platform # 'win32', 'linux2', 'darwin'
    executable -- absolute path of the executable binary of the Python interpreter
    prefix -- prefix used to find the Python library
    exec_prefix -- prefix used to find the machine-specific Python library
    float_repr_style -- string indicating the style of repr() output for floats
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!

functions:

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

data:

    flags # 命令行的状态，-d debug, -v verbose

## sysconfig

## future_builtins

## warnings

python的警告模块，只警告，不中断程序运行．

    import warnings

functions:

    warn(message[, category[, stacklevel]])

## contextlib

编写上下文管理器的模块．

    import contextlib

## abc

实现抽象方法．

    import abc

classes:

    # abc.ABCMeta
    ABCMeta

    # abc.abstractproperty
    abstractproperty

functions:

    abstractmethod(funcobj)

## atexit

## traceback

For python stack traces. 追踪python的堆栈信息．

    import traceback

functions:

    extract_stack(f=None, limit=None)
    extract_tb(tb, limit=None)
    format_stack(f=None, limit=None)
    format_tb(tb, limit=None) # 格式化后返回字符串
    print_stack(f=None, limit=None, file=None)
    print_tb(tb, limit=None, file=None) # 直接打印stacktrace信息
    ...

## gc

garbage collector：python的垃圾回收模块．

    import gc

## inspect

从运行的python对象获取有用的信息．

    import inspect

classes:

functions:

    classify_class_attrs(cls)
    stack(context=1)
    isgenerator()
    isgeneratorfunction() # 检查一个函数是否是生成器

data:

## site

## user

## fpectl

***
