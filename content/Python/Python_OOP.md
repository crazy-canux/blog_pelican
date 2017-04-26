Title: Python_OOP
Date: 2016-06-21 21:18:09
Tags: Python, Encapsulation, Inheritance, Polymorphism



# 面向对象/OOP

***

# 类/Class

***

# 封装

python的类中的变量／常量和方法默认都是public的，类本身和子类都可以使用，也可以被import导入．

一个下划线开头的属性是protected,能在类本身和子类使用，类的实例可以直接访问，不可以用import导入．

双下划线开头的属性是private, 只能类本身使用，类的实例不能直接访问，子类和其它类都不能使用,子类也不能覆盖．

    xxx # public
    _xxx # protected
    __xxx # private
    __xxx__ # 系统定义的名字

***

# 继承

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

# 多态

***
