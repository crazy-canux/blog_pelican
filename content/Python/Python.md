Title: Python
Date: 2016-06-21 21:18:09
Tags: Python



# **Python概述**

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

# **python基本语法**

python源程序叫xxx.py

python中一切皆对象．

python大小写敏感．

python通过缩进和冒号:区分语法块，而不是大括号{}.

python中的表达式(条件/循环表达式等)不需要用小括号()括起来．

python标识符(变量，函数，参数，类等)由字母和下划线开头，还可以包含数字．不能是关键字．

python不支持方法或函数重载．

python不支持char和type类型．

python没有switch语句．

python支持多继承．

python不支持++/--自增和自减运算符．

python支持连续比较，a&lt;b&lt;c.

## lexical analysis

<https://docs.python.org/2/reference/lexical_analysis.html>

Logical lines and physical lines：

    # python通过行尾的令牌NEWLINE表示逻辑行
    expression
    # 以操作系统的换行符表示物理行．
    \n

encoding declarations:

    # python脚本中的第一行或第二行的
    coding[=:]\s*([-\w.]+)
    # 注释与正则表达式匹配将被作为编码申明处理．

[Deprecated] explicit line joining:

    # 多个物理行通过反斜线backslash续行进行显示换行
    # 推荐用隐式换行．
    if a == b \
           and c ==d: # 只有续行的最后一行可以有注释．反斜线的行不能注释.
        print 'more than one physical line.'

implicit line joining：

    # 在括号(parentheses),方括号(square brackets)，大括号(curly braces)中的表达式可以分割多个物理行而不需要显示换行．
    test_list = [
        'a', # 每一行都可以注释
        'b'
    ]

indentation:

    # 逻辑行的开头的空格和跳格用于缩进，python根据行的缩进级别区分语法块．
    # 缩进级别用于生成INDENT和DEDENT两个令牌
    pep8建议用四个空格表示一个缩进级别．

python2.7源代码格式:

    #!/usr/bin/env python2.7
    # -*- coding: utf-8 -*-

执行python代码：

    $ python mycode.py
    # OR
    $ chmod u+x mycode.py
    $ ./mycode.py

***

# **python注释**

单行注释：

    # comment

多行注释：

    """
    comment1

    comment2
    comment3
    """

***

# **python关键字**

    def lambda class import from
    if elif else while for continue break try except finally return pass
    global raise assert del yield with as
    and or not is in

    [New in python3] False None True nonlocal

    [Deprecated in python3] print(改为了内置print函数) exec(改为了内置exec函数)

***

# **python运算符和优先级**

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

# **python数据类型**

python中一切皆对象，每个对象都有身份(id()), 类型(type()) 和 值三个属性．

python中对象的类型和内存占用都是在运行时确定的．

is和is not可以判断两个变量是否指向同一个对象：

    a is b # 等价于 id(a) == id(b), 表示a和b是同一个对象
    a is not b # 等价于 id(a) != id(b), 表示a和b不是同一个对象

is和is not可以判断变量的类型:

    import types
    type(a) is types.IntType

## *垃圾回收*

Garbage Collector垃圾回收机制是引用计数为主，标记清除和分代收集为辅．

当对象被引用，包括对象在被创建，对象被作为参数传递给函数，对象成为容器对象的一个元素时，引用值增加．

当对象的引用被销毁，包括一个本地引用离开其作用域，对象的别名被del显示销毁，对象的别名被赋值给其它对象，对象被从一个窗口对象中移除，窗口对象本身被del显示销毁，引用值减少．

del语句会删除对象的一个引用．

## *变量和常量*

python是动态类型语言，变量不需要先申明，变量的类型和值在赋值的时候被初始化．

用全部小写表示变量：

    counter = 0
    miles = 100.03
    name = "canux"

用全部大写表示常量：

    PIE = 3.14

## *类型总结*

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

## 数据拷贝

浅拷贝:

    只拷贝顶层数据.

    对不可变对象不开辟新空间,相当于赋值操作;修改原数据,相当于定义了一个新的数据.拷贝的数据不变.
    a=10
    b=copy.copy(a)
    old_id  = id(a) == id(b)
    a=5 # 修改a相当于定义了新变量
    id(a) != old_id
    id(b) == old_id # id(b) 不变
    id(b) == 10

    对可变对象会在内存开辟新空间保存拷贝的数据;只拷贝第一层中的引用,原数据被修改,拷贝的对象也被修改.
    a=[1,2,3]
    b=copy.copy(a)
    id(a) != id(b)
    a[0]=5 # 改变a的数据
    b == a # b的数据也改变

    copy.copy()

深拷贝:

    逐层拷贝数据,直到拷贝的所有引用都是不可变引用.

    深拷贝,一份数据改变,不影响另一份数据.

    copy.deepcopy()

## *Sequences序列类型*

sequence序列是指成员有序排列，可以通过下标偏移量访问，同时可以进行切片操作．序列是可迭代的．

sequence索引操作：

    seq[ind] # 获取下标为ind的元素，下标从0开始．
    seq[-1] # 取最后一个元素

sequence切片操作：

    seq[ind1:ind2] # 获取下标从ind1到ind2间的元素的集合．不包括ind2.
    seq[:ind2] # ind1缺省默认为０.
    seq[ind1:] # ind2缺省表示从ind1到最后一个元素

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

## *数字类型*

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

## *str*

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

    # 一个引号的情况,需要在引号内部空格表示和下一行有空格，续行符前的空格可有可无．
    a = 'This is a ' \
    'string'

    b = 'This is a \
    string'

    c = "This is a " \
    "string"

    d = "This is a \
    string"

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

Unicode: Universal Multiple-Octet Coded Character Set. 使用十六进制表示．加上前缀U+

ASCII: American Standard Code for Information

UFT-8: Unicode Transformation Format

python2因为比unicode出现要早，所以python2默认使用的是ASCII编码．

python3默认使用的是UTF-8编码．

    # 获取默认编码
    import sys
    print(sys.getdefaultencoding())

    a = u'测试'
    type(a) # unicode
    a # u'\u6d4b\u8bd5',　十六进制表示

    # str类型
    b = '测试'
    type(b) # str
    b # \xe6\xb5\x8b\xe8\xaf\x95

    # encode将unicode类型编码成str类型用于数据传输．
    encode([encoding[,errors]]) # 编码
    c = a.encode('uft-8')
    type(c) # str
    c # \xe6\xb5\x8b\xe8\xaf\x95

    # decode将str类型根据原来的编码类型解码成unicode类型进行阅读．
    decode([encoding[,errors]]) # 解码
    d = c.decode('utf-8') # 参数必须是原来的编码的类型
    type(d) # unicode
    d # u'\u6d4b\u8bd5'

    # python2默认ascii编码，所以encode和decode默认都是ascii. 不能处理中文
    u'测试'.encode() # UnicodeEncodeError

    # str+unicode, str会隐式的转换成unicode.
    '测' + u'试' -> '测'.decode() + u'试' # 因为decode默认是ascii不能解码中文,UnicodeDecodeError．
    '测'.decode('uft-8') + u'试'

    # 对非unicode进行encode编码，会先隐式解码成unicode再编码
    '测试'.encode('utf-8') # UnicodeDecodeError, 因为'测试'.decode()默认用ascii解码
    '测试'.decode('utf-8').decode('utf-8')

    # python2程序中出现字符串一定加前缀u.表示成unicode格式
    u'hello world'
    # 不要用str(), 用unicode().
    # 只在写入文件／数据库／网络时才调用编码函数encode().
    # 只在读回数据时才调用解码函数decode().
    # 始终使用utf-8编码．否则容易出现乱码．

可迭代对象转换成字符串：

    ''.join(('a', 'b')) # 可迭代对象的元素需要是str类型.
    ''.join(['a', 'b']) # 可迭代对象的元素需要是str类型.
    ''.join({'a': 'b'}) # 字典迭代键，可迭代对象的元素需要是str类型.

## *tuple*

tuple类型是不可变类型(immutable),是容器(container),是序列(sequence)通过索引访问．

元组是不可变类型，不能对元组的元素进行增删操作．

## *list*

list类型是可变类型(immutable),是容器(container),是序列(sequence)通过索引访问．

列表元素增删修改：

    # 除了使用内置方法还可以使用序列的索引．
    lst[index] = value
    del lst[index]

## *dict*

dict类型是可变类型(immutable),是容器(container),是映射(mapping)类型,是无序的,通过映射访问．

字典迭代键，字典的键必须是可哈希的，字典的键必须是不可变类型．列表/字典/可变集合等不可哈希对象不能用作字典的键．

所有不可变类型都是可哈希的，都可以作为字典的键．

可用内置函数hash()获取或判断是否能用作字典的键．

字典的键必须是唯一的，不能一个键对应多个值．有这种情况取最后一个赋值．

字典的键操作符：

    # 字典通过键操作符来读取元素的值
    dic['key']

键成员操作符:

    # 取代has_key()和keys()内置方法
    'key' in dic # 不推荐用 dic.had_key('key') 和 'key' in dic.keys()
    'key' not in dic

字典元素增删修改：

    dic['key'] = 'value'
    del dic['key']

## *Sets集合*

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

# **python控制流**

continue语句:表示立即终止本次循环，启动循环的下一次迭代．

break语句：表示结束当前循环块，跳转到后面的语句．

pass语句： 表示不做任何事情，NOP.

## *if条件语句*

    if condition:
        expression
    elif condition:
        expression
    else:
        expression

python中的三目运算：

    X if C else Y
    等效于
    if C:
        X
    else:
        Y

    # 三目运算符高于赋值运算符．
    a = b if c else d
    # 等效于
    a = (b if c else d)

## *while循环语句*

    while condition:
        expression

    # while执行完会执行else(包括while不执行)，break会跳过else．
    while condition:
        expression
    else:
        expression

## *for循环语句*

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

## *iterators迭代器*

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
            return self

        def next(self):
            if condition:
                ...
            else:
                raise StopIteration()

## *list comprehensions列表解析*

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

## *generator expressions生成器表达式*

Generator Expressions生成器表达式, 是列表解析的一个扩展．

列表解析的缺点就是要迭代整个对象用来创建列表，对大的对象来说性能差.

生成器表达式就是结合生成器和列表解析解决这个问题．

生成器表达式不必创建完整的列表，而是一边循环一边计算，返回一个生成器对象。

生成器就是一个迭代器对象，在每次调用next()方法时返回一个值．直到抛出StopIteration异常．

创建生成器的两种方法：

    # 使用列表解析的变种
    generator = (expression for item1 in iterable1 if condition1)

    # 任何使用yield的函数都称为生成器。
    参考yield函数部分．

***

# **python文件和输入输出**

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

***

# **python错误和异常**

参考内置的错误和异常.

BaseException是所有异常的基类． Exception是常规错误的基类.

错误和异常的检测和处理：

    try:
        try_suite
    except Exception0[ as reason]: # reason可以用于在except_suite中打印具体的异常信息，reason是一个Exception0类型的实例．
        except_suite
    except Exception1[ as reason]: # 可以有多个except用来捕获不同的异常，但是只有一个except会被执行.
        except_suite
    except (Exception2, Exception3)[ as reason]: # 也可以在一个except中同时检测多个异常．放入一个tuple中. reason是一个实例的元组．
        except_suite
    except Exception[, reason]: # 可以用Exception来捕获所有异常，而不用区分具体的异常．不推荐用逗号，应该用as代替．
        except_suite
    [Deprecated] except:    # 不推荐此用法，和上面一个等效
        except_suite
    ...
    else:    # 可选， 没有异常触发except时运行else,　except和else只能运行一个．
        expression
    finally:    # 可选，无论是否捕捉到异常都会执行的．
        expression

    # 也可以不对异常处理
    try:
        try_suite
    finally:
        finally_suite

    # 异常的参数
    reason.__clas__.__name__  # 就是异常类的名字
    print reason # 打印异常参数．

## *raise触发异常*

除了上面捕获解释器触发的异常，用户还可以用raise自己触发异常:

    raise [SomeException [, args [, traceback]]]

SomeException可以是字符串，内置异常，第三方库异常类，自定义异常类, 或实例.

    raise ExceptionClass[, args[, traceback]] # 类
    raise ExceptionClass(arguments)[, args[, traceback]] # 实例
    raise ExceptionClass, instance # [TODO]
    raise instance # 触发实例异常, raise reason 就是跑出一个ExceptionClass类型的instance.
    raise string # 触发字符串异常
    raise # 重新触发前一个异常，如果之前没有异常触发TypeError.

## *自定义异常和错误*

自定义异常需要继承一个标准异常或者第三方库的异常来实现一个类．

通过raise来触发自定义的异常．

    class MyError(Exception/StandardError/Warning):
        def __init__(self, msg):
            super(...).__init__(self, ...)
            ...
        ...

    raise MyError, args

## *assert断言*

断言语句等效assert表达式, 如果断言成功不采取任何措施，否则触发AssertionError异常．

    assert expression[, arguments]

可以提供一个异常参数和捕获AssertionError异常:

    try:
        assert expression, "If raise AssertionError, print this message."
    except AssertionError, e:
        print '%s: %s' % (e.__class__.__name__, e)

## *with上下文管理*

CMP: context management protocol.

with上下文管理仅用于支持上下文管理协议(CMP)的对象．

    with context_expr [as var]:
        with_suite

with语句执行时就执行上下文符号（with和as之间的内容）来获得一个上下文管理器．

上下文管理器调用__context__()方法来返回一个上下文对象．

上下文对象会调用__enter_()方法完成with语句块执行前的准备工作．返回值赋给as后面的var变量．

with语句块执行完毕后调用__exit__()方法，__exit__()有三个参数，如果没有异常都是None,否则是sys.exc_info()的三个返回值．

自定义上下文管理器:

    class CMPTest(object):
        def __init__(self):
            pass

        def __enter__(self):
            ...
            return self

        def __exit__(self, type, value, traceback):
            ...

父类实现了上下文管理协议，子类可以直接使用with.

***

# **python函数**

定义/申明一个函数:

python对函数的申明和定义是一起的．

函数必须先定义/申明才能引用/调用.

通过关键字def来定义一个函数.

def function_name(arguments)
        expression

函数引用：

引用一个函数名并不会执行函数内容．

    function_copy = function_name

    # 可以将函数作为参数传给另外一个函数，然后在另外一个函数调用该函数
    def fun_name(arg):
        print arg(10)
    fun_name(str)

函数调用:

调用一个函数才会执行函数内容.

    function_name(arguments)
    # 可以通过引用的副本来调用函数
    function_copy(args)

函数的返回值：

省略return表示返回None. 单个return表示返回None.其它表示返回一个对象．

    return
    return return_value

函数的实参：

位置参数，调用的时候通过先后顺序传递的参数,函数定义时需要放在前面．

默认参数，在函数定义时就已经初始化的参数，调用时可以不再赋值．

默认参数在函数定义时需要放在位置参数的后面．否则抛出SytaxError.

    def function_test(position_args, keyword_args, *args, **kwargs):
        pass

函数的形参：

位置参数，在函数调用时根据定义的参数的顺序来传递．

默认参数，在函数调用时如果没有传值则使用定义的默认值．

关键字参数，在函数调用时，根据定义时的参数名称来传值.

非关键字参数的传值不能在关键字参数后面．

    def func_test(arg1, arg2, arg3="val1", arg4="val2"):
        pass
    func_test(1, 2, 3, 4) # 位置参数
    func_test(1, 2) # 使用默认参数
    func_test(arg2=2, arg1=1) # 关键字传参

可变长度参数:

当函数参数不确定时，可以使用可变长度参数．

一个星号表示一个非关键字参数组成的元组(可以是其它序列，会自动转换成元组)．

两个星号表示一个关键字参数组成的字典．

函数定义时可变长度参数必须在位置参数和默认参数后面．而且关键字变长参数应该在最后.

    def func_test(position, default='value', *args, **kwargs):
        pass

调用可变长度参数时，可以把非关键字变长参数放到一个元组，把关键字变长参数放到一个字典．

也可以在元组和字典中放部分参数，另外一部分直接传递, 非关键字参数的传值不能在关键字参数后面．

    # 注意，函数定义的时候星号是必须的，函数调用的时候也需要星号．
    args = ('val1', 'val2')
    kwargs = {key1: 'val1', key2: 'val2'}
    func_test('position', 'default', *args, **kwargs)
    # 部分传递，多出来的非关键字参数属于变长非关键字参数，多出来的关键字参数属于变长关键字参数．
    func_test('position', 'default', 'non-keyword', key='keyword', *(1,2), **{3: 'three'})

函数的属性：

通过小数点来调用函数的属性．

内置函数的特殊属性(BIF)：

    function_test.__doc__
    function_test.__name__
    function_test.__module__ # __builtin__
    function_test.__self__ # None

自定义函数的属性(UDF)：

    dir(function_test)
    '__doc__',
    '__name__',
    'func_closure',
    'func_code',
    'func_defaults',
    'func_dict',
    'func_doc',
    'func_globals',
    'func_name'

偏函数:

    from functools import partial
    partial(func, *args, **keywords) # 一个偏函数的类

变量作用域:

python搜索一个标识符先从局部作用域开始搜索，如果没有找到就在全局作用域找，否则抛出NameError异常．

    # 当在函数外部和内部都定义了同一个变量，局部变量会覆盖全局变量
    var = 'global'
    def func_test(*args, **kwargs):
        var = 'local'
        print var
    func_test() # local

    # 如果在函数内部使用一个不在函数内部定义的变量，就会在函数外部查找．
    var = 'global'
    def func_test(*args, **kwargs):
        print var
    func_test() # global

    # 在函数内部不能修改外部变量,只能引用.
    var = 'global'
    def func_test(*args, **kwargs):
        var += 'local'
        print var
    func_test() # UnboundLocalError: local variable 'var' referenced before assignment

    # 如果需要在局部引用全局变量需要使用global关键字
    var = 'global'
    def func(*args, **kwargs):
        global var
        var = 'local'
        print var
    func() # local
    print var # local # 全局变量在局部被修改．

## *Functional Programming函数式编程*

python涉及到函数式编程主要有几个内置函数和lambda匿名函数．

    [Deprecated]apply() # function(*args, **keywords)
    reduce() # 推荐使用from functools import reduce, 而不是直接使用内置方法.
    filter() # 参考__builtins__
    map() # 参考__builtins__

## *lambda匿名函数*

lambda匿名函数就是一个只有一行表达式，不需要通过def来命名的函数.

lambda匿名函数返回一个可调用的函数对象．

lambda匿名函数支持通过def定义的函数的所有功能．

lambda匿名函数中不能有return语句, expression的结果就是函数返回值．

    lambda [arg1[, arg2, ...argN]]: expression
    lambda *args, **kwargs: expression
    lambda : expression

lambda不能是一个申明：

    # 因为在python2中print是一个关键字，所以下面的申明不是合法的lambda表达式．
    lambda : print 'not working'

## *内嵌函数*

可以在函数内部定义函数，内部函数不能在外部函数以外的地方调用．

    def outer(*args, **kwargs):
        expression
        def inner(arg): # 内嵌函数的参数不能是外部函数的参数．内部函数必须完全独立．
            expression
        inner(args)

    def outer(*args, **kwargs):
        filter(lambda arg: expression, sequence)
        map(lambda arg: expression, sequence)
        functools.reduce(lambda arg: expression, sequence)

可以在函数内部内嵌匿名函数，匿名函数可以使用外部函数的参数:

    def foo(x, y):
        bar = lambda :x + y
        print bar()
    foo(4,3)

递归：

    在函数中调用函数本身是一种递归方法
    def fib(n):
        if n in[0, 1]:
            val = 1
        else:
            val = fib(n-1) + fib(n-2)
        return val

## *closure闭包*

在一个内部函数里对在外部作用域的变量进行引用，内部函数被认为是closure.

定义在外部函数内的但由内部函数引用的变量称为自由变量．

当自由变量是一个函数时，闭包就是一个装饰器，decorator是closure最常见的应用．

    def outer(free):
        def clos(*args, **kwargs):
            print free
            print args, kwargs
        return clos

    # 调用外部函数，返回一个内部函数的引用,　传入外部函数的就是自由变量,返回的内部函数就是闭包.
    first_clos = outer(1)

    # 调用closure
    first_clos(*args, **kwargs)

## *decorator装饰器*

装饰器分为函数(方法)装饰器和类装器．函数中再定义函数是函数装饰器，函数中再定义类是类装饰器．

函数装饰器修饰函数和类中的方法，类装饰器修饰类．类装饰器参考OOP．

装饰器本质是一个函数，可以让其它函数在不做修改的情况下增加额外的功能．

常用于插入日志，性能测试，事务处理，缓存，权限校验等场景．

装饰器是用来装饰函数的包装，返回一个修改后的函数对象．将其重新赋值给原来的标识符，并永久失去对原始函数对象的访问．

符号@是装饰器的语法糖.

不带参数的装饰器：

    def deco_name(func):
        def wrapper_name(*args, **kwargs): # 抽象出相同的部分进行包装
            """Docs for wrapper_name."""
            print func.__name__ # 抽象出来的部分在这里实现
            print args, kwargs # 可以引用func传入的参数
            return func(*args, **kwargs) # 最后调用新增加的功能
        return wrapper_name # 返回包装函数的引用.

    # 增加新功能,装饰后返回包装函数的一个引用,赋值给原来的foo．此时包装函数wrapper_name并不会执行
    @deco_name
    def foo(*args, **kwargs):
        """Docs for foo."""
        print 'call foo'
    # 等效于
    foo = deco_name(foo)

    # 调用装饰后的函数,　调用的是装饰后的新的函数．
    foo(*args, **kwargs)

带参数的装饰器:

    def deco_name(arg):
        def deco_inner(func):
            def wrapper_name(*args, **kwargs):
                """Docs for wrapper_name."""
                print arg # 通过装饰器的参数arg来做一些判断
                print func.__name__
                print func.__doc__
                print args, kwargs
                return func(*args, **kwargs)
            return wrapper_name
        return deco_inner

    # deco_name(arg)(foo) -> deco_inner(foo) -> wrapper_name
    @deco_name(arg="value")
    def foo(*args, **kwargs):
        """Docs for foo."""
        pass

    # wrapper_name(*args, **kwargs)
    foo(*args, **kwargs)

装饰器的属性：

    foo.__name__ #  wrapper_name, 并非foo
    foo.__doc__ # "Docs for wrapper_name.", 并非foo的doc.
    # 可以通过import functools.wraps来修饰wrapper_name改变这一属性．

<https://github.com/crazy-canux/python/blob/master/python/psl/myfunctools.py>

多层装饰器：

    @foo
    @bar
    def func(*args, **kwargs):
        ...

    func = foo(bar(func))

<https://github.com/crazy-canux/python/blob/master/python/decorator/function_decorator.py>

## *yield生成器*

生成器generator的另一种实现就是yield函数．有yield的函数返回的就是一个生成器．

yield函数能记住上一次返回时在函数体中的位置，迭代生成器会跳转至该函数中间，而且上次调用的所有局部变量保持不变．

yield函数和普通函数执行顺序不一样，普通函数顺序执行，遇到return或最后一行语句返回．

yield函数遇到yield语句返回，下次执行从上次返回的yield语句开始继续执行．遇到return语句抛出StopIteration异常．

生成器通常用于迭代一个巨大的数据集．

    def gena():
        yield 'first'
        yield 'second'
    g = gena()
    type(g) # generator
    g.next() # first
    g.next() # second
    g.next() # StopIteration

generator类类型,是一个迭代器，可以用for循环迭代:

    __iter__()
    generator.next()
    generator.close() # 在生成器内部抛出GeneratorExit异常要求生成器退出．
    generator.send(arg) # 将值回送给生成器．
    generator.throw(typ[,val[,tb]]) # 在生成器抛出异常

***

# **python模块和包**

名称空间：

* 局部名称空间
* 全局名称空间
* 内建名称空间

python解释器最先加载内建名称空间，也就是\_\_builtins\_\_模块．

然后加载执行模块的全局名称空间，在模块执行时是活动名称空间．

最后加载局部名称空间，在执行期间是不断变化的．

名称空间和变量的作用域是有区别的．

变量／函数／方法先从局部名称空间开始查找，在找全局名称空间，最后查找内建名称空间．

如果都没找到就抛出NameError异常．

无限制名称空间，可以通过属性运算小数点来指定名称空间．

    module.var
    module.function()
    module.method()

搜索路径:

搜索路径在不同的操作一同一般不同.

搜索路径通过两个变量来设置

1. shell的环境变量PYTHONPATH．
2. python解释器的变量sys.path列表里.

在代码里修改搜索路径sys.path

* sys.path.append(os.path.abspath(..))
* sys.path.insert(0, os.path.abspath(..)) # 插入到最前面，也就是在sys.path的第一个''(当前路径)的前面．

所有导入并加载的模块会存放在sys.modules中，导入模块时的搜索顺序

1. 先搜索当前目录.(会覆盖同名的标准库), 其实是在运行过程中动态添加到sys.path中第一个''的位置．
2. 没有的话再搜索sys.path,按照这个列表的顺序搜索找到第一个，然后加载该模块.
3. 没搜到抛出ImportError异常．

## *module模块*

模块就是一个python程序的源文件．模块是用来组织python代码的方法．

把其他模块中属性附加到你的模块中的操作叫做导入(import).

那些自我包含并且有组织的代码片断就是模块( module ).

## *package*

包就是把多个模块放在一个目录中，然后必须加上\_\_init\_\_.py文件．包是用来组织模块的．

    # 包支持模糊导入.
    [Deprecated] from package.module import * # 会导入包里面所有的变量，函数，类．

在__init__.py导入属性，导入时可以省略模块名：

    robot/__init__.py
    from robot.run import run, run_cli

    test.py
    from robot import run, run_cli # 可以省略属性所在的模块名
    run()
    run_cli()

    等效:
    test.py
    from robot.run import run, run_cli # 通过包名和模块名直接导入．
    run()
    run_cli()

在__init__.py定义__all__变量来决定导入哪些属性．

    from robot.run import run, run_cli
    __all__ = [run, run_cli]

    from robot import * # 仅仅导入__all__指定的属性

## *import导入模块和包*

如果模块第一次被导入，就会被加载并执行．也就是说模块被加载时顶层的代码会被执行，一般包括全局变量，类和函数的申明．

一个模块无论被导入(import)多少次，只在第一次导入时被加载一次．除非用reload()函数．

import导入顺序(中间空一格)：

* 标准库模块
* 第三方库模块
* 自定义模块

import关键字导入模块/包：

    import module
    import package
    # 包可以多层嵌套
    import package.subpackage
    import package.subpackage.module

from-import关键字导入模块中的属性：

    from module import function/method/variable
    from package.module import function/method/variable
    from package.subpackage.module import function/method/variable

from-import关键字导入包中的的包/模块到当前的名称空间：

    from package import subpackage
    from package...subpackage import sub-subpackage
    from package import module

as关键字可以给模块/包/属性取别名：

    import module/package/package.subpackage as alias
    from module/package.module/package.subpackage.module import function/method/variable as alias
    from package/package.subpackage import module/subpackage/sub-subpackage alias

相关的内置函数:

    locals()
    global()
    [Deprecated] reload() # 推荐用from imp import reload(), 重新导入一个已经导入的模块．

模块的特殊属性：

    __name__ # 模块的特殊属性
    # 如果模块直接运行，也就是作为top-level脚本运行．值为__main__.
    # 如果作为module,也就是(import/python -m)，值为模块名称.
    # 一般用来做单元测试.
    if __name__ == "__main__":
        main()

# *PEP0328*

多行导入：

    # 通过续行符
    from module import a, b, c, \
        d, e, f

    # 通过分成两行导入
    from module import a, b, c
    from module import d, e, f

    # PEP328建议使用分组导入
    from module import (a, b, c,
        d, e, f)

    # 不推荐使用模糊导入．
    [Deprecated] from module import *

绝对导入：

默认采用绝对导入，也就是通过完整的包路径来导入，避免和标准库模块冲突．

默认的包路径就是sys.path或PYTHONPATH.

只有import没有from的一定是绝对导入．

    import package/module

相对导入： [TODO]

小数点开头表示相对导入，一个小数点表示当前的包，两个小数点表示上一层的包，以此类推．

相对导入一定是import-from结构．

相对导入的优先级低于绝对导入，也就是先去sys.path中查找，然后根据当前模块的相对位置查找．

    from . import package/module
    from .foo import bar
    from ..foo import bar
    from ...foo import bar

***

# **python文档**

文档注释:

python的文档注释采用reST风格的注释.

包/模块文档:

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

类/函数/方法文档:

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

文档的特殊属性:

    __doc__ # 函数/类/方法的特殊属性，用来表示文档的属性
    # 文档字符串不能被子类继承．

***

