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

实例化：

    ins = ClassName()

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

类的方法属性仅仅是一个作为类定义的一部分定义的函数, 与类的实例子无关．

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

    class.__bases__ # 类的父类构成的元组
    class.__dict__ # 以字典的形式存储对象的属性
    class.__name__ # class name
    class.__doc__ # 文档的特殊属性, 不会被继承.
    # 新式类新增的三个特殊属性:
    class.__mro__ # 返回方法解析顺序的元组
    class.__subclasses__() # 返回子类的列表
    class.mro()

类的属性搜索顺序：[TODO]

访问类属性的时候解释器会搜索(__dict__)属性，如果没有找到就去基类的(__dict__)搜索．

## 实例属性

实例属性：

实例严格来说只有数据属性(方法属性应该属于类属性)，数据属性就是和某个实例相关联的数据值，这些值独立于其它实例或类，当一个实例被释放，相应的数据属性也被释放．通常通过init方法来设置实例的数据属性．

    class ClassName(object):
        DATA = "in class" # 类的数据属性

        def __init__(self, default="default", *args, **kwargs):
            self.default = default # 实列的数据属性

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

## classmethod

要写一个只在类中运行，而不在实例中运行的方法,可以使用类方法．

通过classmethod装饰器来装饰该方法，并且方法的第一个参数是一个类cls.

    class ClassName(object):
        @classmethod
        def demo_cm(cls, *args, **kwargs):
            ...

    # 可以通过类来调用, 也就是可以直接调用非绑定方法．自动传入类作为第一个参数．
    ClassName.demo_cm(args, kwargs)
    # 也可以通过实例来调用, 自动传入类作为第一个参数
    ClassName().demo_cm(args, kwargs)

## staticmethod

有一些跟类有关的功能，但在运行时又不需要类和实例参与的情况需要用到静态方法．

通过staticmethod装饰器来装饰该方法，并且第一个参数不需要是类cls或实例self.

比如修改环境变量或修改其它类的属性，相当于是在类中定义的一个普通函数．

    class ClassName(object):
        @staticmethod
        def demo_sm():
            ...

    # 通过类调用, 可以直接调用非绑定方法,但是不会自动传入类．
    ClassName.demo_sm()
    # 通过实例调用,也可以通过实例调用．但是不会自动传入实例．
    ClassName().demo_sm()

***

# **封装/Encapsulation**

封装描述了对数据／信息进行隐藏的观念，对数据属性提供接口和访问函数．

python的类中的变量／常量和方法默认都是public的，类本身和子类都可以使用，也可以被import导入．

一个下划线开头的属性是protected,能在类本身和子类使用，类的实例可以直接访问，不可以用from module import *导入．

双下划线开头的属性是private, 只能类本身使用，类的实例不能直接访问，子类和其它类都不能使用,子类也不能覆盖．

    xxx # public
    _xxx # protected
    __xxx # private
    __xxx__ # 系统定义的名字

***

# **继承/Inheritance**

利用类的两种方式就是组合和继承．

## 组合

创建复合对象时可以通过组合来增加功能和代码的重用性．

当类之间有显著不同，并且较小的类是较大的类所需的组件时一般使用组合．

    from .company import Company
    from .home import Home
    class Emp(object):
        def __init__(self, *args, **kwargs):
            self.comp = Company(args)
            self.home = Home(kwargs)

## 子类和派生

对于相同的类但是有不同的功能，可以通过派生来实现．

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

## super

因为同名的方法子类会覆盖父类，在子类中调用父类的同名方法可以通过super内置函数．

super()方法实际是一个构造器．自动找到基类方法，同时传入self参数．

    super(type, obj) -> bound super object; requires isinstance(obj, type), obj是实例
    super(type, type2) -> bound super object; requires issubclass(type2, type), type2是类．
    super(type) -> unbound super object

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

***

# **多态/Polymorphism**

python不支持重载方法，但是可以通过对参数的判断，对不同的参数进行不同的处理．以此来实现重载的功能．

python可以重载操作符．

## 定制python类

python有一些可自定义的特殊方法集，它们中的一些有预定义的默认行为，一些没有，留到需要的时候去实现．

这些特殊方法是python中用来扩充类的方法．可以用来模拟标准类型或者重载操作符.

这些特殊方法都是用双下划线开头和结尾的．

可用来定制类的基本特殊方法：

    __init__(self, *args, **kwargs) # 构造器，带一些可选的参数
    __new__(cls, *args, **kwargs) # 构造器，带一些可选的参数，通常用来设置不可变数据类型的子类．
    __del__(self) # 解构器

    __str__(self) # 可打印的字符输出，str(), print
    __repr__(self) # 运行时的字符串输出，　repr(), ``
    __unicode__(self) # unicode字符串输出，　unicode()
    __nonzero__(self) # 为object定义False值，　bool()

    __cmp__(self, other)
    __rcmp__(self, other)
    __hash__(self)

    __call__(self, *args) # 表示可调用的实例
    __len__(self) # 长度，　len()

***

# 新式类的特性

## property
