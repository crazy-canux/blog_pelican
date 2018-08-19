Title: Testing RobotFramework
Date: 2017-02-25 09:41:39
Tags: Testing, QA, RobotFramework



# Robot Framework

<https://github.com/robotframework/robotframework>

<https://github.com/robotframework/QuickStartGuide>

支持python和java的API.

Robot Framework is a generic test automation framework for acceptance testing and acceptance test-driven development (ATDD).

Install:

    $ pip install robotframework

Modular:

* Test Data
* Robot Framework(test data syntax)
* Test Libraries(test library API) + Test Tools
* System under Test(system interface)

Use:

    $ robot --version
    $ robot [options] data_sources

会生成三个文件：

* output.xml
* log.html
* report.html

***

# setting table

    *** Settings ***
    # 前三个是加载外部文件
    Library    Selenium2Library # 需要在sys.path路径里面
    Resource    ${RESOURCES}/common.tsv
    Variables    ${RESOURCES}/common.py
    Documentation    Docs
    Metadata    Version    2.0
    Suite Setup
    Suite Teardown
    Force Tags
    Default Tags
    Test Setup
    Test Teardown
    Test Template
    Test Timeout

# Test Case table

<https://github.com/robotframework/HowToWriteGoodTestCases>

test case:data_sources就是test cases files.robotframework测试用例可以使用带参数的简单表格语法，也可以是不带参数的关键字表格,也可以是数据驱动测试用例.

Test Cases由keywords和可能的arguments组成．

    *** Test Cases ***
    Test Case Name
        [Documentation]    Docs
        [Tags]
        [Setup]
        [Teardown]
        [Template]
        [Timeout]
        ...

Test Case分类：

* Workflow tests
* higher-level tests
* Data-driven tests

# Keywords table

key word:测试用例使用关键词创建,关键词的2个来源是库关键字和用户关键字．

    *** Keywords ***
    Keyword name
        [Documentation]    docs
        [Tags]
        [Arguments]
        [Return]
        [Teardown]
        [Timeout]

Keywords分类：

* Library keywords
* User keywords

# Variables

variables:测试用例中可能变化的数据定义成变量．

    *** Variables ***
    ${ScalarVar}    first one    second one
    @{ListVar}     one    two
    &{DictVar}     key=value    key1=value1

变量类型：

* scalar variables标量
* list variables列表
* dictionary variables字典

# Organizing test cases

test suites:测试用例的集合叫测试套件．每个包含测试用例的输入文件组成一个测试套件．

test setup/suit setup: 在测试之前执行某些关键词．

test teardown/suit teardown: 在测试之后执行某些关键词．

    *** Settings ***
    Suite Setup    Action/Keyword
    Test Setup
    Suite Teardown    Action/Keyword
    Test Teardown

tags:给测试用例设置标签，以便给他们自由的元数据．

给测试套件加标签：

    *** Settings ***
    Force Tags    quickstart # 这个是case的强制的tag.
    Default Tags    example smoke # 这个是case的默认的tag.

自定义标签注意多个标签之间用四个空格区分．

给单个case加标签：

    # 自定义的tag名字多个单词最好用-连接，不要用空格．
    [Tags]    Your-tags1    tag2 # 这个是自定义的tag.

***

# Libraries

内置标准库和第三方库，自定义库都可以作为keywords.

robotframework的强大之处在于可以根据自己的需要开发自己的库．

## standard(build-in libraries)

* BuiltIn

    内置标准库，默认唯一自动加载的库．其它的库都需要手动加载．

        # Comment关键字用来注释．
        Comment    this is comment
        # Evaluate关键字用来调用python程序．
        ${var}    Evaluate    random.randint(1000, 999)    random
        # Import Library关键字用来导入python模块．
        Import Library    mytest.py

* Collections

* DateTime

* Dialogs

* Easter

* OperatingSystem

* Process

* Remote

* Screenshot

    用于测试过程中的截屏．

        # Take Screenshot关键字用来截屏
        Take Screenshot

* String

* Telnet

* XML

## External

* selenium2library

    用于web自动化测试．提供了丰富的定位器，包括id,name, xpath, css.

    <https://github.com/robotframework/Selenium2Library>

    Install:

        $ pip install robotframework-selenium2library

## other

***

# Tools

robot framework相关的工具．

## build-in tools

* Rebot

* Testdoc

* Libdoc

* Tidy

## editors

* RIDE

    robot framework的IDE.

    <https://github.com/robotframework/RIDE>

    Install:

        # Only wxPython 2.8.12.1 with Unicode support is officially supported
        $ pip install robotframework-ride

    Usage:

        # 添加windows的桌面：
        # C:\Python27\python.exe -c "from robotide import main; main()"
        # C:\Python27\Lib\site-packages\robotide\widgets\robot.ico
        > ride.py
        $ ride.py
        # F5搜索关键字

## build

## other

***

# robot command

    $ robot tests.robot
    $ robot -t/--test [test cases] tests.robot
    $ robot -t My*test*case* tests.robot # 例如case叫My test case just for test.
    $ robot -s/--suite [test suites] tests.robot
    $ robot -i/--include [tags] tests.robot
    $ robot -i My-test-tag tests.robot # 例如tag叫My-test-tag.
    $ robot -e/--exclude [tags] tests.robot
    -d --outputdir dir # 存放output, log, report文件的路径.
    -o --output file
    -l --log file
    -r --report file
    -W --consolewidth chars
    -C --consolecolors auto|on|ansi|off
    -K --consolemarkers auto|on|off
    -L --loglevel level    # 格式LOGLEVEL:DEFAULT, 可选TRACE, DEBUG, INFO (default), WARN, NONE
    # DEFAULT是log file中默认显示的日志级别
    -b --debugfile # 存放debug log的文件．
    -T --timestampoutputs # 表示所有在outputdir里面的文件都自动加时间戳．
    -P --pythonpath path * # 指定PYTHONPATH, 可以指定正在开发的库用来测试，而不需要安装到site-packages.

***

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

关键字跑出异常，该关键字状态就是failed,否则就是pass.

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

同名的默认方法会先调用，然后调用自定义的方法．

可以实现的方法有：

    start_suite(name, attribute)/end_suite(name, attribute) # test suite开始/结束的时候调用
    start_test(name, attribute)/end_test(name, attribute) # test case开始/结束的时候调用
    start_keyword(name, attributes)/end_keyword(name, attribute) # keyword开始/结束的时候调用
    close() # 相当于teardown.
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
