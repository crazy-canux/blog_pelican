Title: Python编程之面向对象
Date: 2016-06-21 21:18:09
Tags: Python, Inheritance,



# 面向对象

# 类/Class

# 封装/Encapsulation

# 继承/Inheritance

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
要在子类中调用父类的方法，需要调用内置的super()函数．

super()函数实际是一个构造器．

    super(type, obj) -> bound super object; requires isinstance(obj, type)
    super(type, type2) -> bound super object; requires issubclass(type2, type)
    uper(type) -> unbound super object
    class C(B):
        def meth(self, arg):
            super(C, self).meth(arg)
            ...

## 多继承/Multiple Inheritance

MRO: Method Resolution Order　决定访问的方法和属性的顺序．

MRO采用广度优先的顺序，先查找同胞兄弟，如果所有直接基类都没有就查找上一级的所有基类．

# 多态/Polymorphism
