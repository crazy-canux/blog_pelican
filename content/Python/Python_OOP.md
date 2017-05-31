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

类的初始化方法:

如果定义了\_\_init\_\_方法在实例化的时候会首先调用该方法，进行一些初始化的工作.

init方法的第一个参数必须是实例self,　而且不能有return语句．

init方法一般用来设置实例属性(也就是数据属性).

    class ClassName(object):
        def __init__(self, *args, **kwargs):
            pass

类似于构造器和解构器的方法:

如果定义了\_\_new\_\_方法，会在init方法之前运行，并且返回一个实例，也就是\_\_init\_\_的self.

new方法的第一个参数必须是类cls. 并且需要返回一个实例．

new方法在object中被定义为staticmethod．

\_\_del\_\_特殊方法要在实例对象的所有引用都被清除后才会执行．

不要在del中做与实例没有关系的事情，一般不建议实现该方法．

    class ClassName(object):

        def __new__(cls, *args, **kwargs):
            pass

        def __del__(self, *args, **kwargs):
            pass

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

方法属性必须绑定到一个实例才能被直接调用, 非绑定方法没有给出实例对象一般不能直接调用．

    class ClassName(object):
        def func(*args, **kwargs):
            pass

    ClassName.func() # TypeError: unbound method func() must be called with MyClass instance as first argument (got nothing instead)

    ClassName().func()

查看类的属性：

    dir(class) # 内建函数
    class.__dict__ # 通过类的特殊属性

类的特殊属性：

    class.__dict__ # 以字典的形式存储对象的属性
    class.__bases__ # 类的父类构成的元组
    class.__name__ # class name
    class.__doc__ # 文档的特殊属性, 不会被继承.
    class.__module__ # 类的定义所在的模块.

类的属性搜索顺序：[TODO]

访问类属性的时候解释器会搜索(__dict__)属性，如果没有找到就去基类的(__dict__)搜索．

## 实例属性

实例属性：

实例严格来说只有数据属性(方法属性应该属于类属性)，数据属性就是和某个实例相关联的数据值，这些值独立于其它实例或类，当一个实例被释放，相应的数据属性也被释放．通常通过init方法来设置实例的数据属性．

    class ClassName(object):
        DATA = "in class" # 类的数据属性

        def __init__(self, default="default", *args, **kwargs):
            self.default = default

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

## 静态方法

## 类方法

## 描述符

## 元类

***

# **封装/Encapsulation**

封装描述了对数据／信息进行隐藏的观念，对数据属性提供接口和访问函数．

python的类中的变量／常量和方法默认都是public的，类本身和子类都可以使用，也可以被import导入．

一个下划线开头的属性是protected,能在类本身和子类使用，类的实例可以直接访问，不可以用import导入．

双下划线开头的属性是private, 只能类本身使用，类的实例不能直接访问，子类和其它类都不能使用,子类也不能覆盖．

    xxx # public
    _xxx # protected
    __xxx # private
    __xxx__ # 系统定义的名字

***

# **继承/Inheritance**

继承描述了子类属性从祖先类继承这样一种方式．

派生类（子类）继承自基类（父类）

python中的类需要继承一个或多个父类．

object类是所有类的父类．

子类继承了基类的属性和方法．不能继承文档字符串．

__init__()构造器：

init方法在类的实例被创建之后调用，用来初始化新的实例．第一个参数必须是self实例．只能返回None.

    class ClassName(object):
        def __init__(self, *args, **kwargs):
            ...

python调用方法时，默认调用的该对象的类的本身的方法，如果该类没有实现该方法才会调用父类的方法．

要在子类中显示调用父类的方法，需要调用内置的super()方法．

super()方法实际是一个构造器．

    super(type, obj) -> bound super object; requires isinstance(obj, type)
    super(type, type2) -> bound super object; requires issubclass(type2, type)
    uper(type) -> unbound super object
    class C(B):
        def meth(self, arg):
            super(C, self).meth(arg)
            ...

## 多继承

MRO: Method Resolution Order　决定访问的方法和属性的顺序．

MRO采用广度优先的顺序，先查找同胞兄弟，如果所有直接基类都没有就查找上一级的所有基类．

***

# **多态/Polymorphism**

多态指出了对象如何通过他们共同的属性和方法来操作及访问，而不需要考虑他们具体的类．

多态表明了动态绑定的存在，允许重载及运行时类型确定和验证．

***
