Title: Python总结
Date: 2016-06-21 21:18:20
Tags: Python



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

***

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

    with上下文仅用于支持上下文管理协议(CMP)的对象．
    可以在自己的类中添加__enter__和__exit__方法来实现上下文管理器．
    也可以直接使用标准库contextlib来实现．

        with open('log.txt', 'w') as logger:
            logger.write('test')

* iterator

    能直接用于for循环的对象为可迭代对象Iterable.
    能被next()内置函数调用并不断返回下一个值的对象为迭代器Iterator.
    所有的可迭代对象都可以使用iter()内置函数转变为迭代器．

# 类

python中的方法就是作为类的属性的函数．
python2中直接通过类名来调用方法，会得到一个unbound method的TypeError错误．
python3中直接通过类名来调用方法，会得到一个方法是一个函数，需要传一个实例作为参数的错误.

* property

    property(fget=None, fset=None, fdel=None, doc=None)内置函数，创建类的特性属性,通常在类内部通过@property装饰器来使用．

* staticmethod

    staticmethod(function)内置函数，将函数function转换成静态方法，通常在类内部通过@staticmethod装饰器来使用．
    静态方法是属于类的方法，但实际上并非运行在类的实例上．不接受第一个隐式的参数，不需要self实例作为第一个参数．
    装饰器@staticmethos有三个作用：
    1. python不必为我们创建的每个对象实例化一个绑定的方法．可以直接用类名调用方法，不用实例化一个对象．
    2. 提高代码可读性, 方法不依赖于对象的状态.
    3. 可以在子类中覆盖静态方法

        class Test(object):
            @staticmethod
            def test_sm(arguments):
                ...

        Test.test_sm is Test().test_sm
        Test.().test_sm is Test().test_sm

* classmethod

    classmethod(function)内置函数，将函数function转换成类方法，通常在类内部通过@classmethod装饰器来使用．
    类方法是直接绑定到类，而不是实例．接收一个类作为第一个隐式的参数，第一个参数是类本身cls．
    如果访问这个类，总是会被绑定到附着的类.
    类方法对于创建工厂方法最有用，以特定的方式实例化对象．

        class Test(object):
            @classmethod
            def test_cm(cls, arguments):
                ...

        Test().test_cm is Test.test_cm

* abstractmethod

    抽象方法是定义在基类中，可能有或没有任何实现的方法．
    可以用abc标准库的修饰器@abstractmethod实现．

* magicmethod

    魔法方法就是在类中用双下划线包围的方法．
    最基本的魔法方法是__init__方法．
    实例化一个类第一个被执行的魔法方法是__new__，最后一个被执行的是__del__．

* python的多继承

    MRO: Method Resolution Order.方法解析顺序.
    MRO使用广度优先搜索．字节点顺序从左往右．

# 函数和函数式编程

* lambda匿名函数

    lambda表达式等效一个函数，但是不需要像普通函数一样定义这个函数．

        lambda arguments:expression

* global全局变量

    global var　用来定义一个全局变量．

* closure闭包

    闭包就是根据不同的配置信息得到不同的结果.
    闭包最常见的应用是装饰器.

        def closure_out(x, y):
            def closure_in(z):
                return x + y + z
            return closure_in # 仅仅返回函数名

        c = closure_out(3, 4) # 返回的是函数closure_in
        print(c(5))

* decorator

    装饰器本质就是函数，这个函数接受其它函数作为参数，并将其以一个新的修改后的函数进行替换。

* list comprehension

    列表解析使用中括号，列表解析返回一个列表。

        list = [expression for item in iterable if condition]

* generator

    生成器不必创建完整的列表，而是一边循环一边计算，这种就是生成器。
    生成器就是对象，在每次调用next()方法时返回一个值．直到抛出StopIteration异常．

        # 最简单的创建生成器的方法，就是把列表解析的中括号改成下括号．
        generator = (expression for item1 in iterable1 if condition1
                        for item2 in iterable2 if condition2
                        ...
        )
        generator.next() # 获取下一个值

    任何使用yield的函数都称为生成器。

        def generator_test():
            yield 1
            yield 2
        g = generator_test()
        next(g) # 1
        next(g) # 2
        next(g) # StopIteration

# 多线程

* GIL

    GIL: Global Interpretror Lock. 全局解释器锁．

    python不建议使用多线程，用多进程代替．

* coroutine

    协程就是同时开启两个任务，但一次只顺序执行一个．
    如果执行的任务阻塞，就切换到下一个继续执行．节省时间．

# python的垃圾回收机制

GC: Garbage Collector.垃圾回收．

python的垃圾回收以引用计数为主，标记清除和分代收集为辅．

引用计数最大的问题是循环引用．

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

