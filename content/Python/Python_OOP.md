Title: Python_OOP
Date: 2016-06-21 21:18:09
Tags: Python, Encapsulation, Inheritance, Polymorphism



# **面向对象/OOP**

OOD: Object Oriented Design.

面向过程的设计支持任何语言，但是如果语言本身内置面向过程的结构，就会更容易编程．

OOP: Object Oriented Programming.

python内置OOP的结构，但是不必一定要使用类和OOP.

面向对象的两个主题就是类和类实例．

创建实例的过程叫实例化．

属性就是属于另一个对象的数据或函数元素．属性分为数据属性和函数属性．

***

# **类/Class**

类是现实世界的抽象的实体以编程的形式出现，实例是这些对象的具体化．

类是一种数据结构的定义，实例是申明了一个这种类型的变量．

类的定义：

新式类都必须继承一个父类，所有类的基类是object.

    class ClassName(object):
        """Doc string."""
        class_suite

类的初始化方法init(相当于构造器):

如果定义了\_\_init\_\_方法在实例化的时候会首先调用该方法，进行一些初始化的工作.

init方法的第一个参数必须是实例self,　而且不能有return语句．

init方法一般用来设置实例属性(也就是数据属性).

    class ClassName(object):
        def __init__(self, *args, **kwargs):
            pass

特殊方法new:

如果定义了\_\_new\_\_方法，会在init方法之前运行，并且返回一个实例，也就是\_\_init\_\_的self.

new方法的第一个参数必须是类cls. 并且需要返回一个实例．

new方法在object中被定义为staticmethod．

相当于析构器的特殊方法del:

\_\_del\_\_特殊方法要在实例对象的所有引用都被清除后才会执行．

不要在del中做与实例没有关系的事情，一般不建议实现该方法．

    class ClassName(object):

        def __new__(cls, *args, **kwargs):
            ...
            return ...

        def __del__(self, *args, **kwargs):
            ...

## 类属性

类属性分为数据属性和方法属性.

类的数据属性仅仅是定义的类的变量．

数据属性通常是静态变量, 也就是和类对象绑定, 与类的实例无关．

直接通过类名来访问类的数据属性．不建议通过实例来访问类的数据属性．

    class ClassName(object):
        CONST_VARIABLE = 'value'

        def __init__(self, *args, **kwargs):
            ClassName.CONST_VARIABLE = 'new'

    ClassName.CONST_VARIABLE = 'new value'

类的方法属性仅仅是一个作为类定义的一部分定义的函数, 与类的实例无关．

类中定义的方法的第一个参数是一个实例self．

方法属性必须绑定到一个实例才能被直接调用, 非绑定方法没有给出实例对象一般不能直接调用．

    class ClassName(object):
        def func(self, *args, **kwargs):
            pass

    ClassName.func() # TypeError: unbound method func() must be called with MyClass instance as first argument (got nothing instead)

    # 调用非绑定方法：
    ClassName.func(ClassName()) # 除非传入实例作为第一个参数self的值
    # 常用场景： 调用父类中的非绑定方法
    class ClassNmae(BaseClass):
        def __init__(self, *args, **kwargs):
            BaseClass.__init__(self, *args, **kwargs)
            ...

    # 调用绑定方法： 自动把实例作为self传入，不用显式传入．
    ClassName().func()

查看类的属性：

    dir(class) # 内建函数
    class.__dict__ # 通过类的特殊属性

类的特殊属性：

    class.__doc__ # 文档的特殊属性, 不会被继承.
    class.__name__ # class name
    class.__bases__ # 类的父类构成的元组
    class.__dict__ # 以字典的形式存储对象的属性
    # 新式类新增的三个特殊属性:
    class.__mro__ # 返回方法解析顺序的元组
    class.__subclasses__() # 返回子类的列表
    class.mro()

内置类的方法(BIM)的特殊属性:

    bim.__doc__
    bim.__name__
    bim.__module__ # __builtin__
    bim.__self__ # bim

自定义的方法的特殊属性(UDM):

    '__doc__',
    '__name__',
    '__module__',
    '__self__',
    'im_class',
    'im_func',
    'im_self'

# **实例/Instances**

实例化：

    ins = ClassName()

## 实例属性

实例属性：

实例严格来说只有数据属性(方法属性应该属于类属性)，数据属性就是和某个实例相关联的数据值，这些值独立于其它实例或类，当一个实例被释放，相应的数据属性也被释放．通常通过init方法来设置实例的数据属性．

    class ClassName(object):
        DATA = "in class" # 类的数据属性

        def __init__(self, default="default", *args, **kwargs):
            self.default = default # 当前实例的数据属性

区别类的数据属性和实例的数据属性.

    obj1 = ClassName()
    print obj1.DATA # "in class", 当实例没有同名的数据属性，会访问类的数据属性．
    obj1.DATA = "in obj1" # 相当于给实例新建了一个数据属性，会覆盖类的数据属性．
    print obj1.DATA # "in obj1" 访问的是实例的数据属性，覆盖了类的数据属性．
    ClassName.DATA # "in class" 访问类的数据属性．

查看实例属性:

    dict(instance)
    instance.__dict__

实例的特殊属性：

    instance.__dict__ # 以字典的形式存储对象的属性
    instance.__class__ # 实例对应的类
    # instance没有__name__属性

***

# **封装/Encapsulation**

封装描述了对数据／信息进行隐藏的观念，对数据属性提供接口和访问函数．

默认情况下，数据属性和类属性都是public的．类所在的模块和导入了类的其它模块都可以使用．

    var # public
    def method_name(self):

一个下划线开头的属性是protected,能在类本身和子类使用，类的实例可以直接访问，不可以用from module import *导入．

用于把属性限制在一个模块中．

    _xxx # protected
    def _xxx(self):

双下划线开头的属性是private, 只能类本身使用，类的实例不能直接访问，子类和其它类都不能使用,子类也不能覆盖．

用于把属性限制在一个类中.

    __xxx # private
    def __xxx(self):

系统已经定义的特殊方法，也称魔法方法．

    def __xxx__(self): # 系统定义的名字

## Composition

类之间的关系只有两种继承和包含.

创建复合对象时可以通过composition组合来增加功能和代码的重用性．

当类之间有显著不同，并且较小的类是较大的类所需的组件时一般使用组合．

    from .company import Company
    from .home import Home
    class Emp(object):
        def __init__(self, *args, **kwargs):
            self.comp = Company(args)
            self.home = Home(kwargs)

***

# **继承/Inheritance**

利用类的两种方式就是包装和继承．

## 子类和派生

对于相同的类但是有不同的功能，可以通过derivation派生来实现．

通过使用一个已经定义好的类，扩展它或者修改，而不会影响系统中使用现存类的其它代码片段．

    class Father(object):
        def woman(self):
            ...

    class Mother(object);
        def man(self):
            ...

    class Child(Father, Mother):
        def child(self):
            ...

## 继承

继承描述了基类的属性如何遗传给派生类．

派生类（子类）继承自基类（父类）

python中的类需要继承一个或多个父类．

object类是所有类的父类．

子类继承了基类的属性和方法．

文档字符串\_\_doc\_\_是唯一的，不能继承．

一个类的\_\_bases\_\_属性可以查看它的父类组成的元组．不包括父类的父类．

    class.__bases__ # 类的父类构成的元组

实例调用方法时，默认调用的该对象的类的本身的方法，如果该类没有实现该方法才会调用父类的方法．

    class Parent(object):
        def foo(self):
            print "in parent."

    class Child(Parent):
        def foo(self):
            print "in child."

## 从内置类继承

可以从内置类型继承子类，修改一些属性．

    class RoundFloat(float):
        def __new__(cls, val):
           return super(RoundFloat, cls).__new__(cls, round(val, 2))

    class SortedKeyDict(dict):
        def keys(self):
            return sorted(super(SortedKeyDict, self).keys())

## Multiple inheritance多重继承

python2.2之前的版本多重继承采用深度优先，从左至右，来获取在子类中使用的属性．

由于类，类型，内建类型的子类都重新架构，新的类采用MRO算法来查找子类中使用的属性．

MRO: Method Resolution Order, 方法解释顺序．采用广度优先，从左至右边，来获取在子类中的属性．

可以通过新式类的特殊属性查看子类的属性的查找顺序：

    class.__mro__ # 返回方法解析顺序的元组

多继承，mro和super的用法：

super每次只调用MRO中的第一个父类，和getattr的顺序一样．并且相同的父类只调用一次．

数据属性，普通方法属性，特殊方法属性都是按照MRO顺序来查找．

<https://github.com/crazy-canux/python/tree/master/python/multiple_inheritance>

***

# **多态/Polymorphism**

python不支持方法重载，但是可以通过对参数的判断，对不同的参数进行不同的处理．以此来实现重载的功能．

python可以重载魔法方法．

## magicmethod

python类有一些可自定义的特殊方法集，它们中的一些有预定义的默认行为，一些没有，留到需要的时候去实现．

这些特殊方法是python中用来扩充类的方法．可以用来模拟标准类型或者重载操作符.

这些特殊方法都是用双下划线开头和结尾的．也被称为魔法方法．

基本特殊方法：

    __init__(self, *args, **kwargs) # 构造器，带一些可选的参数
    __new__(cls, *args, **kwargs) # 构造器，带一些可选的参数，通常用来设置不可变数据类型的子类．
    __del__(self) # 解构器

    __str__(self) # 可打印的字符输出，str(), print
    obj = ClassName()
    print obj # 默认的类的__str__会调用__repr__, <test.RoundFloat object at 0x7f32a151be90>
    # 可以通过重写__str__或__expr__来改变打印的内容

    __repr__(self) # 运行时的字符串输出，　repr(), ``
    obj = ClassName()
    obj # 默认的打印对象的运行时的字符串，　<test.RoundFloat at 0x7fb715253e90>
    # 可以通过重写__repr__()改变打印的内容

    __unicode__(self) # unicode字符串输出，　unicode()
    __nonzero__(self) # 为object定义False值，　bool()
    __hash__(self)  # 返回对象hash值，　hash()

可调用对象的特殊方法：

    __call__(self, *args) # 表示可调用的实例, callable(object) 会返回true.

    class TestClass(object):
        def __call__(self, *args):
            print "Instance is callable after implement call method in class."
            print "Args come from instance invoke is: {}".format(args)

    tc = TestClass()
    callable(tc) # True
    tc()
    tc('arg1')

实例和类的检查相关特殊方法：

可以控制内置方法的反射(自省)行为．

    __instancecheck__(self, instance) # isinstance(instance, class)
    __subclasscheck__(self, subclass) # issubclass(subclass, class)

属性相关特殊方法：

    __getattr__(self, name) # getattr(), 仅当属性没有在实例／类／父类的__dict__中找到才会调用．
    __setattr__(self, name, value)
    __delattr__(self, name)

新式类的特殊方法：

    # 属性相关
    __getattribute__(self, name) # 总是被调用, 会覆盖__getattr__()

    # 描述符相关
    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)

    __slots__

    __metaclass__

with上下文管理特殊方法：

    __enter__(self) # return self, 需要返回self
    __exit__(self, exc_type, exc_value, traceback)

对象比较特殊方法：

    __cmp__(self, other) # cmp()
    __lt__(self, other)
    __le__(self, other)
    __eq__(self, other)
    __ne__(self, other)
    __gt__(self, other)
    __ge__(self, other)

容器类型相关特殊方法:

    __len__(self) #　len()
    __getitem__(self, key) #
    __setitem__(self, key, value) #
    __delitem__(self, key) # del
    __reversed__(self) # reversed()
    __iter__(self) # iter()
    __contains__(self, item)
    __missing__(self, key)

<https://github.com/crazy-canux/python/blob/master/python/magicmethod/container.py>

数值类型相关特殊方法：

    __add__(self, other)
    __sub__(self, other)
    __mul__(self, other)
    __div__(self, other)
    __truediv__(self, other)
    __floordiv__(self, other)
    __mod__(self, other)
    __divmod__(self, other)
    __pow__(self, other[, module])
    __lshift__(self, other)
    __rshift__(self, other)
    __and__(self, other)
    __xor__(self, other)
    __or__(self, other)

    __rxxx__(self, other)

    # 原位运算必须返回self.
    __ixxx__(self, other) # self += other -> self = self + other

    __neg__(self)
    __pos__(self)
    __abs__(self)
    __invert__(self)

    __complex__(self)
    __int__(self)
    __long__(self)
    __float__(self)

    __oct__(self)
    __hex__(self)

    __index__(self)
    __coerce__(self, other)

## Delegation & Wrapping

Wrapping包装就是对一个已经存在的对象增加，删除或修改已经存在的功能．

Delegation授权(代理)是Wrapping包装的一个特性,用于简化处理相关命令性功能，最大化重用代码．

实现delegation的关键在于覆盖__getattr__()特殊方法．通过调用内置函数getattr()得到一个对象的默认行为．

    class Wrapper(object):
        def __init__(self, obj):
            self.__data = obj

        def __getattr__(self, attr):
            return getattr(self.__data, attr)

***

# 新式类的特性

随着类和类型的合并，所有类对应的内置函数都是工厂函数，调用工厂函数实际上就是类型实例化．

属性相关的可定制特殊属性：

旧式类和新式类都有__dict__属性用字典的方式存储属性，但是字典占用大量内存．

新式类定义了一个新的属性__slots__用于取代__dict__属性, 是一个类的特殊变量属性．

    __slots__

属性相关的特殊方法：

    __getattribute__(self, name) # 新式类新增，总是被调用, 会覆盖__getattr__()

# metaclass

元类用来定义某些类是如何被创建的．改变类的默认行为和创建方式．

大多数情况下不需要创建元类，一般使用系统的元类的默认方式．

在执行类定义的时候，解释器必须知道这个类的元类；

先查找类属性__metaclass__，如果存在就以此作为元类；

如果没有定义，就向上查找父类中的__metaclass__;

如果父类也没有就查找__metaclass__全局变量．

如果都没有这个类就是一个传统类．就以types.ClassType作为元类．

在执行类定义时候检查元类，元类传递三个参数到构造器：

    类名
    从基类继承数据的元组, __bases__
    类的属性字典, __dict__

元类相关的可定制属性：

    __metaclass__

定义一个元类：

    class MetaClassName(type):
        def __new__(cls, name, bases, dicts):
            super(MetaClassName, cls).__init__(name, bases, dicts)
            # 在这里做一些你希望使用该元类的类在定义时做的操作

    class ClassName(object):
        __metaclass__ = MetaClassName # 指定元类
        ...

<https://github.com/crazy-canux/python/tree/master/python/metaclass>

## abstractmethod

抽象方法，类似于java的interface.

最简单的抽象方法：

    # 如果子类没有实现同名的该方法，就会抛出异常．
    def base_method(self):
        raise NotImplementedError

或者使用abc标准库来实现：

<https://github.com/crazy-canux/python/tree/master/python/psl/myabc.py>

# descriptors

研究描述符之前先搞清楚普通对象访问属性的优先级．

普通对象访问(set/get/delete)属性的优先级：

    obj.__dict__['attr'] # 先访问实例对象
    obj.__class__.__dict__['attr'] # 再访问类对象
    obj.__class__.__base__.__dict__['attr'] # 接着访问基类的对象,不包括metaclass.
    __getattr__ # 如果实现了的话，优先级最低

descriptors描述符是python新式类的最关键的新特性．

描述符是具有绑定行为的对象属性，属性访问被描述符协议中的方法覆盖．

任何实现了下面三个描述符协议方法中的一个的新式类都是描述符.这三个特殊方法充当描述符协议．

描述符相关的特殊方法：

    __get__(self, obj, type=None) # 返回一个属性的值
    __set__(self, obj, value) # 设置一个属性的值，返回None
    __delete__(self, obj) # 属性的引用递减，返回None

描述符是数据property，class，staticmethod，classmethod, 以及super的机制．

data descriptor:定义了__get__和__set__的对象是数据描述符, 主要用于数据属性．

non data descriptor:仅仅定义了__get__的对象是非数据描述符，主要用于方法属性．

如果实例的字典(obj.__dict__)具有与数据描述符相同名称的条目，则数据描述符优先。

如果实例的字典(obj.__dict__)具有与非数据描述符相同名称的条目，则字典条目优先。

    class DescriptorName(object):
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, typ):
            print '__get__', instance, typ
            return self.name

        def __set__(self, instance, value):
            print '__set__', instance, value
            self.name = value

    class TestClass(object):
        name = DescriptorName('canux')

    tc = TestClass()
    print tc.name # __get__(tc, type(tc))被调用
    print TestClass.name # __get__(None, TestClass)被调用
    tc.__dict__['name'] = 'test' # 无效
    tc.name = 'test' # __set__被调用
    TestClass.name = 'test' # 仅仅是重新定义类的属性，覆盖了描述符
    # 此时tc.__dict__有同名属性，如果定义了__set__
    print tc.name # __get__被调用，属性已经修改
    print TestClass.name # __get__被调用,属性已经修改
    # 如果没有定义__set__，就是调用的tc.__dict__里面的．

描述符访问属性的优先级：

    数据描述符(__set__, __get__)
    # 对于访问实例属性obj.__getattribute__调用方式：type(obj).__dict__['attr'].__get__(obj, type(obj))
    # 对于访问类属性class.__getattribute__调用方式：ClassName.__dict__['attr'].__get__(None, ClassName)
    instance.__dict__
    非数据描述符(__get__)
    __getattr__ # 如果实现了的话，在描述符中优先级最低

描述符是由__getattribute__特殊方法调用，覆盖该方法可以防止描述符自动调用.

obj.__getattribute__和class.__getattribute__的调用方式不同．

描述符的三个特殊方法一般是通过属性访问自动调用．

函数和方法的描述符：

在属性访问期间函数包括了__get__方法用于绑定方法．因此函数和方法是非数据描述符．

    class TClass(object):
        def __get__(self, obj, typ=None):
            return types.MethodType(self, obj, typ)


        def tmethod(self, args):
            return args

    class Foo(object):
        @Tclass
        def bar(self):
            print 'in bar'

    obj = TClass()
    TClass.__dict__['tmethod'] # function __main__.f
    TClass.tmethod # unbound method TClass.tmethod
    obj.tmethod # bound method TClass.tmethod of <__main__.TClass object at 0x7f8a4f084c10>

    obj.function(*args) -> function(obj, *args)
    Class.function(*args) -> function(*args)

## property

property属性是一种有用的特殊类型的描述符． 也是descriptor的主要用途．

    property(fget=None, fset=None, fdel=None, doc=None) # 返回一个property类型的对象

通过上面的descriptor的普通方式实现纯pytho写的property:

    class Property(object):
        def __init__(self, fget, fset, fdelete):
            self.fget = fget
            self.fset = fset
            self.fdelete = fdelete

        def __get__(self, obj, typ=None):
            return self.fget(obj)

        def __set__(self, obj, val):
            self.fset(obj, val)

        def __delete__(self, obj):
            self.fdelete(obj)

    class Foo(object):
        def fget(self):
            print 'fget called'

        def fset(self, val):
            print 'fset called'

        def fdelete(self):
            print 'fdelete called'

        bar = Property(fget, fset, fdelete)

通过装饰器@property来实现：

    class Person(object):
        def __init__(self):
            self._email = None

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, value):
            m = re.match('\W+@\W+\.\W+', value)
            if not m:
                raise Exception('email not valid')
            self._email = value

        @email.deleter
        def email(self):
            del self._email

<https://github.com/crazy-canux/python/tree/master/python/descriptor>

***

# super

super只能用于新式类．

因为同名的方法子类会覆盖父类，在子类中调用父类的同名方法可以通过super内置函数．

super()方法实际是一个构造器．自动找到基类方法，同时传入self参数．

    super(type, obj) -> bound super object; requires isinstance(obj, type), obj是实例
    super(type, type2) -> bound super object; requires issubclass(type2, type), type2是类．
    super(type) -> unbound super object

对于单继承, super用来调用父类同名方法．

    class Child(Parent):
        def foo(self):
            Parent.foo(self) # 可以手动调用父类同名的方法，调用非绑定方法，传入self参数．

    class Child(Parent):
        def __init__(self, *args, *kwargs):
            super(Child, self).__init__(*args, **kwargs) # init方法也会被覆盖．
            ...

        def foo(self, *args, **kwargs):
            super(Child, self).foo(*args, **kwargs) # super(type, obj)返回type类的基类的对象．
            ...

对于多继承，super用法参考上面的多继承．

super()返回的对象有一个用于调用Descriptor的定制__getattribute__()方法．

    super(B, obj).method() ->
    obj.__class__.__mro__ ->
    A.__dict__['method'].__get__(obj, B)

<https://rhettinger.wordpress.com/2011/05/26/super-considered-super/>

# classmethod

要写一个只在类中运行，而不在实例中运行的方法,可以使用类方法．

通过classmethod装饰器来装饰该方法，并且方法的第一个参数是一个类cls.

类方法通常用于替代类构造函数．

    class ClassName(object):
        @classmethod
        def demo_cm(cls, *args, **kwargs):
            ...

    # 可以通过类来调用, 也就是可以直接调用非绑定方法．自动传入类作为第一个参数．
    ClassName.demo_cm(args, kwargs)
    # 也可以通过实例来调用, 自动传入类作为第一个参数
    ClassName().demo_cm(args, kwargs)

描述符相关：

    obj.function(*args) -> function(type(obj), *args)
    Class.function(*args) -> function(Class, *args)

# staticmethod

有一些跟类有关的功能，但在运行时又不需要类和实例参与的情况需要用到静态方法．

通过staticmethod装饰器来装饰该方法，并且第一个参数不需要是类cls或实例self.

比如修改环境变量或修改其它类的属性，相当于是在类中定义的一个普通函数．

    class ClassName(object):
        @staticmethod
        def demo_sm():
            ...

    # 可以直接调用非绑定方法,但是不会自动传入类．
    ClassName.demo_sm()
    # 也可以通过实例调用．但是不会自动传入实例．
    ClassName().demo_sm()

描述符相关：

    obj.function(*args) -> function(*args)
    Class.function(*args) -> function(*args)

***

# Class Decorators

类装饰器比函数装饰器更灵活，高内聚，封装性等优点．

类装饰器用于装饰一个类.

    def deco_name(cls):
        class WrapperName(cls, ...):
            def __init__(self, *args, **kwargs):
                cls.__init__()
                ....__init__()
                ...
        return WrapperName

    @deco_name
    class ClassName(object):
        def __init__(self, *args, **kwargs):
            ...
        ...

<https://github.com/crazy-canux/python/blob/master/python/decorator/class_decorator.py>

***
