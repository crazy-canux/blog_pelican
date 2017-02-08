---
layout: post
title: Python总结
comments: true
date: 2016-06-21 21:18:20
updated:
tags:
- python
categories:
- Python
permalink:
---

# python项目结构

.
|-- AUTHORS.rst
|-- README.rst
|-- CONTRIBUTING.rst
|-- LICENSE
|-- project    项目源代码目录
    |-- __init__.py 包文件
    |-- tests      用来存放测试相关的文件
        |-- __init.py__.py 包文件
|-- bin        //用来存放将被setup.py安装的二进制脚本
|-- data       //用来存放其它类型文件
|-- etc        //用来存放配置文件
|-- tools      用来存放与工具相关shell脚本
|-- docs       用来存放文档
|-- scripts    用来存放安装相关的脚本
|-- examples   用来存放使用本包相关的例子
|-- setup.py   标准安装脚本
|-- setup.cfg
|-- MANIFEST.in

# python的可用接口

1. python内置函数

c/c++实现的，不需要导入就可以使用的。

2. python标准库

python实现的，需要导入才能使用的。

3. python外部库

需要安装和导入才能使用的。

外部库是对python代码的补充。

4. python框架

需要安装和导入才能使用的。

python代码是对外部库的补充。

***

# 控制流

* with as上下文管理

* 迭代器

# 类

* 静态方法

* 类方法

* 抽象方法

# 函数和函数式编程

* lambda与匿名函数

* global变量

* 装饰器

    装饰器本质就是函数，这个函数接受其它函数作为参数，并将其以一个新的修改后的函数进行替换。

* 列表表达式

    使用中括号，列表表达式返回一个列表。

        list = [expression for item in iterable if condition]

* 生成器表达式

    不必创建完整的列表，而是一边循环一边计算，这种就是生成器。

    使用小括号,生成器表达式返回一个生成器。

        generator = (expression for item1 in iterable1 if condition1
                        for item2 in iterable2 if condition2
                        ...
        )
        generator.next() # 获取下一个值

* 生成器与yield

    任何使用yield的函数都称为生成器。

* 协程

* 协程与yield

***

# 编码

## python2

python2中的str和unicode是两种不同的类.

str存储的是已经编码的字节序列，输出时看到的每个字节用16进制表示，以\x开头，每个汉字占用三个字节长度。

unicode存储的是编码前的字符，输出时看到的以\u开头，每个汉字占用一个长度。

str类型可以通过decode()方法转化为unicode对象。

unicode可以通过encode()方法转化为str对象。

    S.encode([encoding[,errors]])
    S.decode([encoding[,errors]])

encode把str类型的S编码成encoding,S必须是unicode，如果不是,python2默认先S.decode('ascii'),用ascii编码把S解码成unicode，如果S原来不是ascii而是utf-8就会报错，需要显示调用S.decode('utf-8')先把S按照utf-8解码成unicode再编码。

decode把str类型的S解码成unicode，S原来的编码用encoding指定,如果S原来是utf-8,S.decode('utf-8')按照utf-8把S解码成unicode。

    unicode(string[, encoding[, errors]])

unicode把str类型的string按照encoding解码成unicode。

如果文件中出现中文需要指定utf-8,默认是ascii：

    # -*- coding: utf-8 -*-

获取默认的encoding，python2系统默认是ascii:

    import sys
    print sys.getdefaultencoding()

## python3

python3的str和bytes是两种不同的类。

    S.encode(encoding='utf-8', errors='strict')
    B.decode(encoding='utf-8', errors='strict')

获取默认的encoding，python3系统默认是utf-8:

    import sys
    print(sys.getdefaultencoding())

