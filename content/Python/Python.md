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

python没有switch语句．

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

    [Deprecated in python3] print(改为了内置print函数) exec(改为了内置exec函数)

***

# python运算符和优先级

优先级从高到底：

    # 函数调用
    f(x)

    # 序列的切片
    seq[ind1:ind2:step]

    # 序列下标索引
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
    /    python2两个操作数都是整数时，结果是商舍去小数后的整数,也就是地板除; 只要有一个以上的浮点操作数,结果就是浮点数，也就是真正的除法．
    /    python3会自动转化成两个浮点数出发，结果永远是浮点数，永远是真正的除法．
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
    [Deprecated in python3] <>

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

    # [New] 序列的元素/字典的键/集合的元素 成员运算符, 优先级一样
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

* 不可变类型:immutable不可变类型就是变量的值是固定的，再次赋值就是重新创建了新的对象: 数字类型，字符串str，元组tuple，不可变集合frozenset.
* 可变类型:mutable可变类型就是变量的值是可以改变的: 列表list，字典dict，可变集合set.

存储模型：

* scalar标量/原子类型:只能容纳单个对象：数字类型，字符串str
* container容器类型:可以容纳多个对象：元组tuple，列表list，字典dict,集合set/frozenset.

访问模型：

* 直接存取:数字类型
* 索引访问:sequence序列是顺序访问：字符串str，元组tuple，列表list.
* 映射访问:mapping映射类型是映射访问,元素无序存放，通过唯一的key来访问：字典dict.

## 序列类型

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

sequence算术运算：

    seq * number # 序列重复number次
    sql1 + seq2 # 两个序列连接

sequence成员运算：

    obj in seq # obj在包含在序列中,返回True
    obj not in seq # obj不包含在序列中返回True

序列浅拷贝：

    浅拷贝就是创建了一个类型和原对象一样，内容是原来对象的元素的引用．
    a = ['name', ['money', 100]]
    b = a[:] #　通过切片操作来拷贝
    c = list(a) #　通过工厂函数来拷贝
    d = copy.copy(a) # 通过copy模块的copy函数
    ???

序列深拷贝:

    copy.deepcopy()
    ???

## 数字类型

数字类型是不可变类型(immutable),是标量(scalar),是直接存储的．

0b开头表示二进制

0开头表示八进制

0x开头表示十六进制

数字类型转换的关系是整数转换成浮点数，非复数转换成复数．

* int

    python3的int其实就包括了short, int, long三种长度的整型．

    python3的int不再需要用l/L来表示长整型．

* bool(int)

    bool类继承自int.

    bool类型只有True和False两个值．

* [Deprecated in python 3]long

    python2在整数值后面加l/L表示长整型．

* float

    python中的float其实就包括了单精度和双精度，相当于float和double都可以用．

* complex

    python中有复数类型．

## str

python2中str和unicode继承自basestring, basestring继承自object.

python3中unicode和basestring在python3中被废弃．str直接继承自object.

python3中不再需要u/U来表示unicode字符串．

str类型是不可变类型(immutable),是标量(scalar),是序列(sequence)通过索引访问．

字符串表示方法：

    'This is a string'
    "This is a string"
    """This is a string"""

字符串的续行：

下面都表示一个只有一行的字符串．

    # 一个引号需要在引号内部空格表示和下一行有空格，续行符前的空格可有可无．
    a = 'This is a ' \
    'string'

    b = "This is a " \
    "string"

    # 三引号续行符前的空格就表示和下一行有空格．
    c = """This is a \
    string"""

编译时字符串连接：

    foo = "hello" 'world'
    urllib.urlopen('http://' # protocol
    'localhost' # hostname
    ':8000' # port
    '/') # path

原始字符串：

    # 正常情况下在字符串中的特殊字符串(\加一个字符)表示特殊含义．是不可打印的．
    print '\n'
    # 如果需要表示正常含义需要转译(\用来转意)．
    print '\\n' # 需要转译．
    # 也可以使用原始字符串来表示正常含义．r''和R''都可以．
    print r'\n'
    open(r'C:\windows\test.txt')

字符串编码解码:

    # 程序中出现字符串一定加前缀u.
    u'hello world'
    # 不要用str(), 用unicode().
    # 只在写入文件／数据库／网络时才调用编码函数encode().
    # 只在读回数据时才调用解码函数decode().

可迭代对象转换成字符串：

    ''.join(('a', 'b')) # 可迭代对象的元素需要是str类型.
    ''.join(['a', 'b']) # 可迭代对象的元素需要是str类型.
    ''.join({'a': 'b'}) # 字典迭代键，可迭代对象的元素需要是str类型.

## tuple

tuple类型是不可变类型(immutable),是容器(container),是序列(sequence)通过索引访问．

元组是不可变类型，不能对元组的元素进行增删操作．

## list

list类型是可变类型(immutable),是容器(container),是序列(sequence)通过索引访问．

列表元素增删修改：

    # 除了使用内置方法还可以使用序列的索引．
    lst[index] = value
    del lst[index]

## dict

dict类型是可变类型(immutable),是容器(container),是映射(mapping)类型,是无序的,通过映射访问．

字典迭代键，字典的键必须是可哈希的，字典的键必须是不可变类型．列表/字典/可变集合等不可哈希对象不能用作字典的键．

所有不可变类型都是可哈希的，都可以作为字典的键．

可用内置函数hash()获取或判断是否能用作字典的键．

字典的键必须是唯一的，不能一个键对应多个值．有这种情况取最后一个赋值．

字典的键操作符：

    # 字典通过键操作符来读取元素的值
    dic['key']

键成员操作符:

    # 取代has_key()内置方法
    'key' in dic
    'key' not in dic

字典元素增删修改：

    dic['key'] = 'value'
    del dic['key']

## 集合

集合是一组无序排列的值，不能进行索引和切片操作，也不能进行键操作，只能通过for循环迭代集合元素．

集合分为可变集合和不可变集合.

集合运算符：

    'element' in st 是成员
    'element' not in st 不是成员
    == 等于
    != 不等于
    <  严格子集
    <= 非严格子集, 等效于issubset()
    > 严格超集
    >= 非严格超集, 等效于issuperset()
    | 联合, OR操作，等效于union()内置方法
    & 交集, AND操作，等效于intersection()内置方法
    - 差补或相对补集, 等效于difference()内置方法
    ^ 对称差分或异或, XOR操作，等效于symmetric_difference()内置方法

    仅用于可变集合的运算符：
    |= 等效于update()内置方法
    &= 等效于intersection_update()内置方法
    -= 等效于difference_update()内置方法
    ^= 等效于symmetric_difference_update()内置方法

集合运算返回结果的类型与左操作数的类型相同，左边是可变集合，结果就是可变集合，否则是不可变集合．

### frozenset

frozenset类型是不可变类型(immutable),是容器(container).

### set

set类型是可变类型(mutable)，是容器(container).

***

# python控制流

continue语句:表示立即终止本次循环，启动循环的下一次迭代．

break语句：表示结束当前循环块，跳转到后面的语句．

pass语句： 表示不做任何事情，NOP.

## if条件语句

    if condition:
        expression
    elif condition:
        expression
    else:
        expression

python中的三目运算：

    X if C else Y

## while循环语句

    while condition:
        expression

    # while执行完会执行else，break会跳过else．
    while condition:
        expression
    else:
        expression

## for循环语句

for循环可以用于遍历序列，字典的键 和 文件的行，集合，列表解析，生成器表达式.

for循环会自动调用迭代器的next()方法，捕获StopIteration异常结束循环．

用for迭代可变对象的时候，不应该改变可变对象的元素的值．

    for condition:
        expression

    # for执行完成会执行else, break会跳过else.
    for condition:
        expression
    else:
        expression

    # 字典有两种写法
    for loop in dic.keys()
    等效于
    for loop in dic

    # 文件有两种写法
    for loop in open('file', 'r').readlines():
    等效于
    for loop in open('file','r'):

## 迭代器

Iterable: 能直接用于for循环的对象为可迭代对象Iterable.

Iterator: 能被next()内置函数调用并不断返回下一个值的对象为迭代器Iterator,迭代完成后抛出StopIteration异常．

file，enumerate和reversed内置类类型的工厂函数返回的都是迭代器类型．

创建迭代器的3种方法：

    # 通过内建函数iter()
    iter()

    # 通过工厂函数
    file()
    enumerate()
    reversed()

    # 自定义类，需要实现 __iter__() 和　next() 两个方法
    class TestIterator(object):
        def __iter__(self):
            ...

        def next(self):
            ...

## 列表解析

List Comprehensions列表解析,来自函数式编程语言Haskell.

列表解析使用中括号，列表解析返回一个列表。

    lst = [expression for item in iterable]
    # 嵌套if
    lst = [expression for item in iterable if condition]
    # 嵌套for
    lst = [expression for item in iterable for item1 in iterable1]

    [x ** 2 for x in range(10)]
    等效于,python2的内置函数map(), filter()都是函数式编程的应用．
    map(lambda x: x**2, range(10))

    [(x+1, y+1) for x in range(10) for y in range(10)]

## 生成器表达式

Generator Expressions生成器表达式, 是列表解析的一个扩展．

列表解析的缺点就是要迭代整个对象用来创建列表，对大的对象来说性能差.

生成器表达式就是结合生成器和列表解析解决这个问题．

生成器表达式不必创建完整的列表，而是一边循环一边计算，返回一个生成器对象。

生成器就是一个迭代器对象，在每次调用next()方法时返回一个值．直到抛出StopIteration异常．

创建生成器的两种方法：

    # 使用列表解析的变种
    generator = (expression for item1 in iterable1 if condition1)

    # 任何使用yield的函数都称为生成器。
    def generator_test():
        yield 1
        yield 2

    g = generator_test() # 返回生成器类型的迭代器．

generator类类型:

    generator.next()
    generator.close() # 在生成器内部抛出GeneratorExit异常
    generator.send(arg)
    generator.throw(typ[,val[,tb]])

***

# python文件和输入输出

python2使用open()内置函数打开文件，返回file类类型的对象，出错返回IOError异常.

file类类型对象是迭代器，同时也是上下文管理器．

python3废弃了file类类型，open()内置函数返回IO流．

    # python2
    open(name[, mode='r'[, buffering=-1]])

    mode
    r: 读，文件必须存在
    w: 写，文件不存在则创建，否则先清空文件再写入．
    a: 追加，文件存在就追加到文件结尾,否则就创建．
    t: text模式，这个是默认模式．不用指定．
    rb/wb/ab: 二进制读写．
    r+/w+/a+: 以读写模式打开文本文件．
    rb+/wb+/ab+: 以读写模式打开二进制文件．
    U: 提供通用换行符支持，文件必须存在

    buffering
    0: 不缓冲
    1: 只缓冲一行数据
    <0: 使用系统默认缓冲机制
    >1: 使用给定值作为缓冲区大小

通用换行符UNS:

Universal Newline Support.

如果是二进制文件读写rb/wb/ab，不会有换行符的问题，如果是文本文件建议用rU/wU/aU来读写.

    # UNS会把
    \r\n
    \r
    \n
    # 都被替换为
    \n

文件可以使用with上下文管理器，并且迭代文件的行:

    with open('file', 'rU') as f:
        for line in f:
            ...

标准文件:

系统默认的三个标准文件: sys.stdin, sys.stdout, sys.stderr.

    # python2的关键字print会把语句打印到sys.stdout,并默认在语句结尾加换行符.
    print expression
    print expression, # 可以避免默认加换行符

    # 内置函数input()会从sys.stdin接受输入
    a = input()

# python错误和异常

## 上下文管理

with as上下文管理

with上下文仅用于支持上下文管理协议(CMP)的对象．
可以在自己的类中添加__enter__和__exit__方法来实现上下文管理器．
也可以直接使用标准库contextlib来实现．

    with open('log.txt', 'w') as logger:
        logger.write('test')

***

# python函数


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
    # python3中在函数内部不支持模糊导入．只能在模块层使用．

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

