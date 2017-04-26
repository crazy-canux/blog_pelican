Title: RobotFramework
Date: 2017-02-25 09:41:39
Tags: QA, RobotFramework



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
    Library    Selenium2Library
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
    ${ScalarVar}
    @{ListVar}
    &{DictVar}

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
    -L --loglevel level    # TRACE, DEBUG, INFO (default), WARN
    -W --consolewidth chars
    -C --consolecolors auto|on|ansi|off
    -K --consolemarkers auto|on|off

***
