Title: Python
Date: 2016-06-21 21:18:09
Tags: Python



# Python

<https://docs.python.org/2.7/index.html>

<http://python.usyiyi.cn/translate/python_278/index.html>

<https://docs.python.org/3.5/index.html>

<http://python.usyiyi.cn/translate/python_352/index.html>

***

# python概述

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

python2.7源代码格式:

    #!/usr/bin/env python2.7
    #

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

    if elif else pass
    while for continue break
    class import from
    and or not is in
    try except finally raise assert
    with as del
    def lambda return global yield
    [Deprecated in python3] print exec
    [New in python3] False None True nonlocal

***

# python数据类型

***

# python运算符

***

# python文件和输入输出

***

# python控制流

python没有switch。

***

# 函数

***

# 文档

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

# 模块和包

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

***

# 错误和异常

***
