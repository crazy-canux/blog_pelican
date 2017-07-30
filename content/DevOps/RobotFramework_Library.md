Title: RobotFramework Library
Date: 2017-02-25 09:41:39
Tags: QA, RobotFramework, Library



# Library

robotframework的灵活就在于可以自己开发第三方库，实现和自己业务相关的关键字．

在robot中导入的这个库必须在sys.path路径里面．

库API的三种类型： 静态库, 动态库, 混合库.

以Selenium2Library为例：

    Selenium2Library
    |-- docs
    |-- tests
    |-- Selenium2Library
        |-- __init__.py
        |-- keywords/*.py
        |-- ...
    |-- setup.py
    |-- ...

    $ pip install robotframework-selenium2library
    # C:\Python27\Lib\site-packages\Selenium2Library
    # /usr/local/lib/python2.7/dist-packages/Selenium2Library
    # 通过ride导入该库后，可以用F5查看关键字的帮助.

    # __init__.py
    # 一个类继承所有关键字所在的类．rf通过导入这个类导入所有关键字．
    from .keywords import *
    from .utils import LibraryListener
    ...

    __version__ =  1.0.0

    class Selenium2Library(keywords):
        """docs."""

        ROBOT_LIBRARY_SCOPE = 'GLOBAL'
        ROBOT_LIBRARY_VERSION = __version__

        def __init__(self, ...):
           """docs"""
           self.ROBOT_LIBRARY_LISTENER = LibraryListener()
           ...

# Static librarty API

使用一个模块或一个类，方法直接映射到关键字名称．静态API是最基本最常用的．

robotframework在类和模块中寻找关键字对应的方法，会忽略单下划线或双下划线开头的方法．

robotframework在类中寻找关键字对应的方法，不区分大小写，会自动忽略空格和下划线．

robotframework测试库实现为类时，基类中的方法也被识别为关键字．

robotframework测试库实现为模块时，导入的模块的命名空间的可能函数也被识别为关键字．此时要防止导入的库中的方法成为关键字．

# dylamic library API

可以在运行时动态确定要实现的关键字的名称以及执行方法．

# hybird library API

静态和动态都有的方式．

# 测试库范围

要确保一个测试用例对状态的更改不会影响其它用例．

测试库可以控制何时使用类属性创建新库．

    ROBOT_LIBRARY_SCOPE
    # Global: 只有一个instance创建，并且所有test cases共享．
    # TEST CASE: 为每个test case创建一个instance.
    # TEST SUITE: 为每个test suite创建一个instance.

# 测试库版本

    ROBOT_LIBRARY_VERSION

# 指定文档格式

    ROBOT_LIBRARY_DOC_FORMAT
    # reST: 需要安装docutils模块
    # ROBOT: 默认的html格式
    # TEXT:　纯文本格式

***

# Listener

Listener监听器接口允许外部监听器获取关于测试执行的通知．

可以实现的方法有：

    start_suite(name, attribute)/end_suite(name, attribute) # test suite开始/结束的时候调用
    start_test(name, attribute)/end_test(name, attribute) # test case开始/结束的时候调用
    start_keyword(name, attributes)/end_keyword(name, attribute) # keyword开始/结束的时候调用
    close() # 当整个test结束调用
    log_message(message) # 当执行的keyword写log的时候调用
    message(message) # 当framework写system log的时候调用
    ...

<http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface-methods>

    # librarylistener.py
    # rf的外部监听程序

    from robot.api import logger
    ...

    class LibraryListener(object):
        """docs"""
        # version 2 for rf>=2.1
        # version 3 for rf>=3.0
        ROBOT_LISTENER_API_VERSION = 2
