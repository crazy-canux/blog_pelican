Title: PSL_Math
Date: 2016-08-12 16:56:45
Tags: Python, Math



# Numeric and Mathematical Modules

## random

    import random

    random()
    randint(a, b)
    randrange(start, stop=None, step=1, int=<type 'int'>, _maxwidth=...)
    seed([self,], a=None)

## fractions

## functools

函数式编程相关的模块

    import functools

    partial(func, *args, **keywords) # 返回functools.partial类型的对象, partial是functools内置的偏函数类类型.
    RED = partial(lambda content, color: color + str(content) + Fore.RESET, color=Fore.RED)
    RED("show me red") == lambda content, color: Fore.RED + str("show me red") + Fore.RESET
    相当于通过partial传一个参数给func，然后剩下的参数通过返回的偏函数传入．这样可以固化一部分参数．

    reduce(function, sequence[, initial]) # 如果initial存在，就把initial作为function的第一个参数，如果function有两个参数，就再从sequence取第一个元素作为function的第二个参数，然后调用function，返回的结果作为function的第一个参数，再继续从sequence获取元素作为参数，继续调用function, 直到sequence为空．
    reduce(lambda x,y: x+y, range(5))

    cmp_to_key(mycmp)
    total_ordering(cls)
    update_wrapper(wrapper, wrapped, assigned=('__module__', '__name__', '__doc__'), updated=('__dict__',))

    wraps(wrapped, assigned=('__module__', '__name__', '__doc__'), updated=('__dict__',))
    # example:
    def deco(func):
        @wraps(func):
        def wrapper(*args, **kwargs):
            """Docs for wrapper."""
            pass

    @deco
    def foo()
        """Docs for new function."""
        pass

    # 不用wraps被装饰的函数foo的属性其实是原来函数的属性，也就是wrapper的属性
    # 用了wraps被装饰的函数foo的属性就是foo自己的属性．
    print foo.__name__
    print foo.__doc__

## operator

操作符相关的模块

    import operator

## decimal

## itertools

    import itertools

## cmath

## math

## numbers

***

# TPL

相关的第三方库
