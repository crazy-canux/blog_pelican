Title: Python
Date: 2016-06-21 21:18:09
Tags: Python



# Python概述

<https://docs.python.org/2.7/index.html>

<http://python.usyiyi.cn/translate/python_278/index.html>

<https://docs.python.org/3.5/index.html>

<http://python.usyiyi.cn/translate/python_352/index.html>

python是一门优雅而健壮的语言.

继承了编译语言(静态语言)的强大性和通用性.

同时也借鉴了脚本语言(动态语言)的易用性．

python特点：

* 高级
* 面向对象
* 可升级
* 可扩展
* 可移植性
* 易学
* 易读
* 易维护
* 健壮性
* 高效的快速原型开发工具
* 内存管理器
* 解释性和编译性

***

# python基本语法

python源程序叫xxx.py

python中一切皆对象．

python大小写敏感．

python中的语句不需要分号;结尾, 语句通过反斜线\续行.

python通过缩进和冒号:区分语法块，而不是大括号{}.

python中每个物理行表示一个逻辑行,如果多个逻辑行放在一个物理行使用分号;隔开,但是python中尽量不要使用分号.

python中的表达式(条件/循环表达式等)不需要用小括号()括起来．

python标识符(变量，函数，参数，类等)由字母和下划线开头，还可以包含数字．不能是关键字．

python不支持方法或函数重载．

python不支持char和type类型．

python中类型都有对应的类的实现，类型也是类．

python支持多继承．

python不支持++/--自增和自减运算符．

python支持连续比较，a&lt;b&lt;c.

python2.7源代码格式:

    #!/usr/bin/env python2.7
    # -*- coding: utf-8 -*-

执行python代码：

    $ python mycode.py
    # OR
    $ chmod u+x mycode.py
    $ ./mycode.py

***

# python注释

单行注释：

    # comment

多行注释：

    """
    comment1

    comment2
    comment3
    """

***

# python关键字

    def lambda class import from
    if elif else while for continue break try except finally return pass
    global raise assert del yield with as
    and or not is in
    [New in python3] False None True nonlocal

    [Deprecated in python3] print exec

***

# python运算符和优先级

优先级从高到底：

    # 函数调用
    f(x)

    # 序列的切片
    seq[ind1:ind2:step]

    # 下标索引
    seq[index]

    # 属性运算.
    object.attribute

    # 算术运算符
    **   幂运算，乘方运算符, 等效内置函数pow(), 优先级高于单目运算符

    # 位运算(只能用于整数)
    ~    按位取反
    # 单目运算符．
    +expr    # 结果符号不变
    -expr    # 对结果符号取负

    # 算术运算符, 优先级一样
    *
    /    两个操作数都是整数时，结果是商舍去小数后的整数,也就是地板除; 只要有一个以上的浮点操作数,结果就是浮点数，也就是真正的除法．
    //   地板除，结果总是舍去小数部分．
    %

    # 算术运算符, 优先级一样
    +
    -

    # 位运算(只能用于整数), 优先级一样．
    <<   左移位运算
    >>   右移位运算

    # 位运算(只能用于整数)
    &    按位与

    # 位运算(只能用于整数), 优先级一样
    ^    按位异或
    |    按位或

    # 关系运算, 优先级一样
    <
    >
    <=
    >=

    # 关系运算, 优先级一样
    ==
    !=
    [Deprecated] <>

    # 赋值运算符和增量赋值
    =
    +=
    -=
    *=
    /=
    %=
    **=
    <<=
    >>=
    &=
    |=
    ^=

    # [New] 对象运算符, 优先级一样
    is
    is not

    # [New] 序列成员运算符, 优先级一样
    in
    not in

    # boolean逻辑运算符
    not    逻辑非

    # boolean逻辑运算符, 优先级一样
    and    逻辑与
    or     逻辑或

***

# python数据类型

python中一切皆对象，每个对象都有身份(id()), 类型(type()) 和 值三个属性．

python中对象的类型和内存占用都是在运行时确定的．

python通过引用计数进行垃圾回收．

del语句会删除对象的一个引用．

is和is not可以判断两个变量是否指向同一个对象：

    a is b # 等价于 id(a) == id(b), 表示a和b是同一个对象
    a is not b # 等价于 id(a) != id(b), 表示a和b不是同一个对象

is和is not可以判断变量的类型:

    import types
    type(a) is types.IntType

## 变量和常量

python是动态类型语言，变量不需要先申明，变量的类型和值在赋值的时候被初始化．

用全部小写表示变量：

    counter = 0
    miles = 100.03
    name = "canux"

用全部大写表示常量：

    PIE = 3.14

## 类型总结

更新模型：

* immutable不可变类型就是变量的值是固定的，再次赋值就是重新创建了新的对象: 数字类型，字符串，元组，不可变集合
* mutable可变类型就是变量的值是可以改变的: 列表，字典，可变集合

存储模型：

* scalar标量/原子类型就是只能容纳单个对象：　数字类型，字符串
* container容器类型就是可以容纳多个对象：　元组，列表，字典, 集合

访问模型：

* 直接存取：数字类型
* sequence序列是顺序访问：字符串，元组，列表
* mapping映射类型就是元素无序存放，通过唯一的key来访问：字典

sequence序列是指成员有序排列，可以通过下标偏移量访问，同时可以进行切片操作．序列是可迭代的．

sequence索引操作：

    seq[ind] # 获取下标为ind的元素，下标从0开始．

sequence切片操作：

    seq[ind1:ind2] # 获取下标从ind1到ind2间的元素的集合．不包括ind2.
    seq[:ind2] # ind1缺省默认为０.
    seq[ind1:ind2:step] # 以步长为step来切片
    seq[:ind2:step]
    seq[::step] # ind1缺省为０，ind2缺省为整个序列长度．
    seq[::-1]  # 翻转序列
    seq[::-step]  # 以步长为step翻转序列．

sequence运算：

    seq * number # 序列重复number次
    sql1 + seq2 # 两个序列连接

sequence成员运算：

    obj in seq # obj在包含在序列中,返回True
    obj not in seq # obj不包含在序列中返回True

## 数字类型

0b开头表示二进制

0开头表示八进制

0x开头表示十六进制

数字类型转换的关系是整数转换成浮点数，非复数转换成复数．

* int

    python3的int其实就包括了short, int, long三种长度的整型．

* bool(int)

    bool类继承自int.

    bool类型只有True和False两个值．

* [Deprecated in python 3]long

    在整数值后面家L表示长整型．

* float
    python中的float其实就包括了单精度和双精度，相当于float和double都可以用．

* complex

    python中有复数类型．

## str

python2中str和unicode继承自basestring.

unicode在python3中被废弃．

## tupple

## list

## dict

## frozenset

## set

***

# python文件和输入输出

***

# python控制流

python没有switch。

***

# python函数

***

# python错误和异常

***

# python文档

文档注释:

python的文档注释采用reST风格的注释.

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

***

# python模块和包

模块就是一个python程序的源文件．模块是用来组织python代码的方法．

包就是把多个模块放在一个目录中，然后必须加上\_\_init\_\_.py文件．包是用来组织模块的．

import关键字导入模块/包：

    import module
    import package
    # 包可以多层嵌套
    import package.subpackage
    import package.subpackage.module

from-import关键字导入模块/包中的属性：

    from module import function/method/variable
    from package.module import function/method/variable
    from package.subpackage.module import function/method/variable

from-import关键字导入包中的的包/模块：

    from package import subpackage/module
    from package.subpackage import sub-subpackage/module

as关键字可以给模块/包/属性取别名：

    import module/package/package.subpackage as alias
    from module/package.module/package.subpackage.module import function/method/variable as alias
    from package/package.subpackage import module/subpackage/sub-subpackage alias

模糊导入：

    from package.module import *
    # 需要在__init__.py中添加__all__列表来定义需要导入的属性．否则导入什么取决于操作系统的文件系统．

import书写顺序：

* 标准库模块
* 第三方库模块
* 自定义模块

模块和包的路径搜索顺序：

1. 先搜索当前目录.(会覆盖同名的标准库), 其实是在运行过程中动态添加到sys.path中原来''的位置．
2. 没有的话再搜索sys.path,按照这个列表的顺序搜索找到第一个，然后加载该模块.
3. 没搜到抛出ImportError异常．

修改搜索路径sys.path：

* sys.path.append(os.path.abspath(..))
* sys.path.insert(0, os.path.abspath(..)) # 插入在第一个,会覆盖当前路径(sys.path原来的第一个'')和sys.path的所有路径.

模块被加载时顶层的代码会被执行，一般包括全局变量，类和函数的申明．

一个模块无论被导入(import)多少次，但是只被加载一次．除非用reload()函数．

名称空间的覆盖顺序：
* 局部名称空间,在执行期间是变化的．local()函数可查看．
* 全局名称空间,不变的．global()函数可查看．
* 内建名称空间,python最先加载，在__builtins__模块中．

大多数模块是被导入，通常这些模块代码都放在类或函数中，主函数用来放单元测试代码．极少数模块是直接运行，这些模块的主函数用来做入口．

    if __name__ == "__main__":
        main()

