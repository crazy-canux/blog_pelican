Title: Python___builtin__
Date: 2016-08-15 11:16:29
Tags: Python, __builtin__



# \__builtin__

python的内置模块，所有python的内置功能都在这个模块中，不需要导入就可以使用。

包括内置类类型以及所属的内置方法，和内置函数.

> __builtins__ - 仅仅是__builtin__的一个引用．

> __builtin__ - Built-in functions, exceptions, and other objects.

***

# 内置函数

python2和python3共同的内置函数：

    compile(source, filename, mode[, flags[, dont_inherit]]) # 编译source返回一个code对象．
    # mode: exec用于模块 可以用exec执行，single用于单行申明，eval用于表达式 可以用eval()执行．
    module = "for i in xrange(10): print(i)"
    code = compile(module, '', 'exec')
    type(code) # code
    exec code
    expression = "3 * 4"
    code = compile(expression, '', 'eval')
    type(code) # code
    eval(code)

    format(value[, format_spec]) # 返回格式化后的字符串形式．

    eval(source[, globals[, locals]]) # 返回python表达式的结果，source可以是compile()的返回值，也可以是一个表达式．
    globals() # 返回当前作用域的全局变量组成的字典
    locals() # 返回当前作用域的局部变量组成的字典
    chr(i) # 返回整数ｉ对应的ASCII字符的str类型，0 <= i < 256.
    rd(c) # 返回字符c对应的ASCII整数.

    ## related to math
    bin(number) # 返回int/long的二进制的字符串形式
    oct(number) # 返回int/long的八进制的字符串形式．
    hex(number) # 返回int/long的十六进制的字符串形式.
    abs(number) # 返回int/long的绝对值
    round(number[, ndigits]) # 返回number四舍五入后的结果，ndigits表示小数点后的位数，默认是0.
    pow(x, y[, z]) # 返回x**y或(x**y) % z
    divmod(x, y) # 返回x/y 的　(商，余数) 组成的元组
    sum(sequence[, start]) # 返回数字序列sequence的所有元素加上start的和，start默认是０．

    ## related to object
    dir([object]) # 查看对象的信息
    callable(object) # 如果object是可调用的返回True
    delattr(object, name) # 删除对象object的属性name
    len(object) # 返回序列（str, tuple, list)或映射（dict)的长度
    hash(object) # 返回一个对象的散列(hash)值，有相同值的对象hash值相同.
    id(object) # 返回一个对象的ID, 用内存地址作为ID来表示唯一性. 也就是对象的身份．
    getattr(object, name[, default]) # 如果object.name存在,返回name的值，否则如果default存在，返回default,否则抛出异常AttributeError
    hasattr(object, name) # 和getattr一样，但是捕获了异常，object.name存在返回True,否则返回False.
    setattr(object, name, value) # 给对象的属性赋值，相当于object.name = value
    isinstance(object, class-or-type-or-tuple) # 如果object是class-or-type中指定的类或类型，返回True,否则返回False,　第二个参数可以是原则．
    issubclass(C, B-or-(B,A)) # 如果C是B或(B,A,...)中的类的子类，返回True,否则返回False.
    repr(object) # 返回object的标准字符串形式，eval(repr(object)) == object.
    vars([object]) # 没有参数等于locals()，有参数等于object.__dict__.

    ## related to iterable
    min(iterable[, key=func]) # 返回可迭代对象iterable中的最小元素
    min(a, b, c, ...[, key=func])  # 返回a,b,c...中的最小元素
    all(iterable) # 如果可迭代的参数iterable中所有的元素都不是0,False,''则返回True,iterable为空也返回True,否则返回False
    any(iterable) # 如果可迭代的参数iterable中所有的元素都是0,False,''则返回False,　否则返回True
    sorted(iterable, cmp=None, key=None, reverse=False) # 返回可迭代对象iterable的元素排序后组成的列表．

    ## related to iterator
    iter(collection) # 将可迭代对象（str, tuple, list, dict等）转换成迭代器,返回迭代器.
    iter(callable, sentinel) # 第一个参数需要是callable的，每次迭代到sentinel停止．
    next(iterator[, default]) # 返回迭代器iterator中的下一个元素，如果没有元素了，default指定内容返回该内容，否则抛出StopIteration异常．

    ## related to input
    input([prompt]) # 等于eval(raw_input(prompt))，根据prompt提示输入内容，返回输入的内容.

    ## related to file
    open(name[, mode[, buffering]]) # 返回一个file类类型的对象．

python3新增的内置函数(New)：

    ascii(object) # 和repr()函数等效．
    exec(object[, globals[, locals]]) # python2中仅仅是一个特殊语句，python3才是内置函数．
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False) # python2中只是一个语句，python3才是内置函数．

python2.7中有，python3中被废弃的内置函数(Deprecated)：

    apply(object[, args[, kwargs]])
    coerce(x, y)
    cmp(x, y)
    execfile(filename[, globals[, locals]])
    intern(string)
    raw_input([prompt])
    reduce(function, sequence[, initial])
    reload(module)
    unichr(i)

***

# 内置常量

    False # 内置类型bool的实例
    True # 内置类型bool的实例
    None # types.NoneType
    NotImplemented
    Ellipsis
    __debug__

***

# object

object类是所有类的基类

    object.__dict__
    instance.__class__
    class.__bases__
    definition.__name__
    definition.__qualname__ # python3新增
    class.__mro__
    class.mro()
    class.__subclasses__()

***

# python2内置异常

BaseException(object) # 所有异常的基类, 继承自object.

    SystemExit
    KeyboardInterrupt
    GeneratorExit
    Exception
        StopIteration
        StandardError
            ...

        Warning
            DeprecationWarning
            ...

# python3内置异常

BaseException(object) # 所有异常的基类, 继承自object.

    SystemExit
    KeyboardInterrupt
    GeneratorExit
    Exception
        StopIteration
        StopAsyncIteration
        ArithmeticError
            ...
        ...

        Warning
            DeprecationWarning
            ...
***

python2数字类型(int, long, float, complex)是不可变类型．

python3数字类型(int, float, complex)是不可变类型．

# int

    int(x=0)
    int(x, base=10)

内置类类型int的内置方法和数据描述符

    bit_length() # 一个int类型的二进制形式的位数．
    conjugate() # 整数的共轭复数是自己

    denominator
    numerator
    imag
    real

# bool(int)

    bool(x)

内置类类型int的内置方法和数据描述符都是继承自基类int.

# (long)

python2中的重要的内置类型．

python3中被废弃．

    long(x=0)
    long(x, base=10)

内置类类型long的内置方法和数据描述符:

    bit_length() # 一个int类型的二进制形式的位数
    conjugate() # 长整型的共轭复数是自己

    denominator
    numerator
    imag
    real

# float

    float(x)

内置类类型float的内置方法和数据描述符：

    as_integer_ratio() # 返回一个整数对，相除的结果是该浮点数
    conjugate() # 浮点数的共轭复数是自己
    fromhex(string) # 将十六进制的字符转换成浮点型
    # float.fromhex('-0x1p-1074')
    hex() # 将浮点数转换成十六进制形式
    is_integer() # 如果浮点数是整数，返回true

    imag
    real

# complex

    complex(real[, imag])

内置类类型complext的内置方法和数据描述符：

    conjugate() # 返回一个复数的工軛复数

    imag
    real

***

python2序列包括str, list, tuple, bytearray, unicode, buffer, xrange.都是可迭代的．

python3序列包括str, list, tuple, bytearray, range, bytes, memoryview.都是可迭代的．

# (basestring)

python2中basestring是str类和unicode类的基类

python3中只有str类，没有unicode类，str直接继承自object类．

# str

字符串是不可变类型, 字符串是序列(可迭代)

    str(object='') # 把一个对象转换成字符串．

内置类类型str的内置方法：

    capitalize() # 字符串首字母大写, 返回新的字符串
    title() # 所有单词首字母大写，返回新的字符串
    lower() # 所有字符小写，返回新的字符串
    upper() # 所有字符大写，返回新的字符串
    swapcase() # 大写字符转换成小写，小写转化成大写
    translate(table [,deletechars]) #
    join(iterable) # 用字符串分割iterable,返回新的字符串
    replace(old, new[, count]) # 用new替换字符串中的前count个old, 返回替换后的字符串
    expandtabs([tabsize]) # 把字符串中的tab键替换为tabsize指定的宽度的新tab，默认是8,然后返回新的字符串
    format(*args, **kwargs) # 返回格式化后的字符串

    lstrip([chars]) # 如果字符串以chars开头,就删除开头chars，然后返回新的字符串, chars默认是空格．
    strip([chars]) # 删除开头和结尾的chars,如果有的话，然后返回新的字符串，chars默认是空格．
    rstrip([chars]) # 如果字符串以chars结尾，就删除结尾的chars,然后返回新的字符串，chars默认是空格．

    center(width[, fillchar]) # 以字符串为中心填充字符串，默认用空格填充,返回填充后的字符串
    zfill(width) # 用0填充字符串的左边，直到width长度，返回新的字符串
    ljust(width[, fillchar]) # 字符串左对齐，右边填充fillchar,默认空格，直到长度为width,返回新的字符串
    rjust(width[, fillchar]) # 字符串右对齐，左边填充fillchar，默认空格，直到长度为width,返回新的字符串

    count(sub[, start[, end]]) # 返回sub字符串在str[start:end]中出现的次数

    decode([encoding[,errors]]) # 解码,返回unicode类型
    encode([encoding[,errors]]) # 编码,返回str类型

    startswith(prefix[, start[, end]]) # 如果str[start:end]以prefix开头，返回true.
    endswith(suffix[, start[, end]]) # 如果str[start:end]以suffix结尾，返回true.
    isalnum() # 如果非空字符串，且元素都是字符或数字，返回True,否则返回False
    isalpha() # 如果非空字符串，且元素都是字符，返回True,否则返回False
    isdigit() # 如果非空字符串，且元素都是数字，返回True,否则返回False
    isspace() # 如果非空字符串，且所有元素都是空格，返回True,否则返回False
    istitle() # 如果非空字符串，且所有单词的首字母大写，返回True,否则返回False
    islower() # 如果非空字符串，且所有元素都是小写，返回True,否则返回False
    isupper() # 如果非空字符串，且所有单词都是大写，返回True,否则返回False

    splitlines(keepends=False) # 根据\n,\r,\r\n来拆分字符串，返回拆分后的列表，True表示保留换行符，默认是False．
    split([sep [,maxsplit]]) # 将字符串以从左到右的maxsplit个seq分割，返回分割后的列表，默认seq是空格，maxsplit是所有seq．
    rsplit([sep [,maxsplit]]) # 和split相反

    partition(sep) # 字符串根据从左往右根据第一个找到的seq分割，返回一个(head, seq, tail), 如果没有找到seq, 返回(str, '', '').
    rpartition(sep) # 字符串根据最后一个找到的seq分割，返回(head, seq, tail),如果没有找到seq,返回('', '', str)

    find(sub [,start [,end]]) # 在str[start:end]中从左往右查找sub,返回找到的第一个字符所在的下标,没找到返回-1
    rfind(sub [,start [,end]]) # 在str[start:end]中查找sub,返回最后一个sub的第一个元素的索引,没有找到返回-1

    index(sub [,start [,end]]) # 和find一样，但是没找到抛出异常ValueError．
    rindex(sub [,start [,end]]) # 和rfind一样，但是没找到抛出ValueError异常．

# (unicode)

python2中的内置类型，和str是兄弟类型．

python3中被废弃．

***

# tuple

元组是不可变类型, 元组是序列(可迭代)

    tuple()
    tuple(iterable) # 把可迭代对象转换成元组.

内置类类型tuple的内置方法：

    count(value) # 返回值为value的元素在元组中出现的次数
    index(value, [start, [stop]]) # 返回值为value的元素在元组tuple[start:stop]中的第一次出现的索引，没有该元素返回ValueError.

***

# (xrange)

python2的重要的内置类型．

python3中被废弃．

xrange是不可变类型，是序列（可迭代）

xrange和range功能一样，但是返回的是xrange类型的可迭代对象．

xrange比range更轻量级，更快，内存使用更高效．

    xrange(stop)
    xrange(start, stop[, step])

# (buffer)

python2中的内置类型．

python3中被废弃．

***

# list

列表是可变类型, 列表是序列(可迭代)

    list()
    list(iterable) # 把可迭代的对象转换成列表．

内置类类型list的内置方法：

    append(object) # 在列表结尾追加对象
    count(value) # 返回value在列表中出现的次数
    extend(iterable) # 将可迭代对象iterable的元素依次追加到列表
    index(value, [start, [stop]]) # 从左往右在list[start:stop]中寻找value,返回第一个找到的元素的索引，否则返回ValueError异常．
    insert(index, object) # 在list[index]前面插入object.
    pop([index]) # 删除list[index],默认是最后一个元素，如果列表为空或索引越界，抛出IndexError异常．
    remove(value) # 删除第一个出现的value．
    reverse() # 翻转列表
    sort(cmp=None, key=None, reverse=False) # 默认对列表中的元素从小到大排序，reverse=True,则从大到小．

***

# dict

字典是可变类型, 字典是映射类型（mapping), 字典可以迭代键．字典是无序的．

    dict()
    dict(mapping) # dict(one=1, two=2)
    dict(iterable) # dict([(1, 'one'), (2, 'two')]), dict([[1,1], [2,2]]), dict(([1,1], [2, 2])), dict(((1,1), (2,2))),
    dict(**kwargs) # dict({1:"one", 2:"two"})

内置类类型dict的内置方法：

    clear() # 清空字典所有元素
    copy() # 返回字典的一个浅拷贝
    fromkeys(S[,v]) # 返回以S的元素为键，v为值的新字典，v默认为None.
    get(k[,d]) # 如果键k在字典里面，返回dict[k], 否则返回d, d默认为None.
    has_key(k) # 如果键k在字典里面，返回True,否则返回False.
    pop(k[,d]) # 从字典中删除键k的键值对，返回dict[k], 如果不存在返回d,如果没有指定d,抛出KeyError异常．
    popitem() # 从字典中删除随即的键值对，返回该键值对组成的元组，如果字典为空，抛出KeyError异常．
    setdefault(k[,d]) # 如果键k在字典中存在，等效于get(k[,d]), 否则就插入D[k]=d键值对．
    update([E, ]**F) #
    keys() # 返回字典的键组成的列表．
    values() # 返回字典的值组成的列表．
    items() # 返回一个列表，每个元素是字典的键和值组成的元组．
    iteritems() # 返回字典的键值对组成的迭代器，next()每次返回一个一对键值组成的元组．
    iterkeys() # 返回字典的键组成的迭代器．
    itervalues() # 返回字典的值组成的迭代器．
    viewitems() # 返回键和值组成的可迭代对象
    viewkeys()　# 返回键组成的可迭代对象
    viewvalues() # 返回值组成的可迭代对象

***

# frozenset

不可变集合frozenset是不可变类型

    frozenset()
    frozenset(iterable)

不可变集合和可变集合共同的内置方法：

    copy()
    difference([others, ...])
    intersection([others, ...])
    isdisjoint()
    issubset()
    issuperset()
    symmetric_difference()
    union()

# set

可变集合set是可变类型

    set()
    set(iterable)

set除了有frozenset的所有方法还有自己特有的方法：

    add()
    clear()
    difference_update()
    discard()
    intersection_update()
    pop()
    remove()
    symmetric_difference_update()
    update()

***

# (file)

python2中的内置类型．

python3中被废弃．

文件类型可以迭代文件的所有行．

    file(name[, mode[, buffering]])

文件类型的内置方法和数据描述符：

    close()
    fileno()
    flush()
    isatty()
    x.next()
    read([size])
    readinto()
    readline([size])
    readlines([size])
    seek(offset[, whence])
    tell()
    truncate([size])
    write(str)
    writelines(sequence_of_strings)
    xreadlines()

***

python3中新增的内置类类型．

# filter

python2中的内置函数：

    filter(function or None, sequence) # 对sequence序列中的所有元素调用function，返回所有function结果为True的结果结果组成的列表／元组／字符串．

python3中的内置类类型：

# range

python2中的内置函数：

    range(stop) # 返回[0, 1, stop-1]
    range(start, stop[, step]) # 返回[start, start+n*step... ], n>=1,start+n*step<stop.

python3中的内置类类型：

# zip

python2中的内置函数：

    zip(seq1 [, seq2 [...]]) # 返回一个列表，元素是序列中相同下标元素组成的元组，只取到所有序列的最小的下标．
    zip((1,2,3),(4,5,6),(7,8)) -> [(1, 4, 7), (2, 5, 8)]

python3中的内置类类型：

# map

python2中的内置函数：

    map(function, sequence[, sequence, ...]) # 将序列中相同下标的元素作为参数传给function，返回所有的结果组成的列表．
    # map(lambda x,y,z: str(x)+str(y)+str(z), "test", (1,2,3), [0,9,8,7,6]) -> ['t10', 'e29', 's38', 'tNone7', 'NoneNone6']
    # map(None, "test", (1,2,3)) -> [('t', 1), ('e', 2), ('s', 3), ('t', None)]

python3中的内置类类型：

***

bytes, bytearray, memoryview都是python3中的binary sequence序列类型

# bytes

python2:

python2中是str类型的别名．

python3中是内置类类型:

    bytes(iterable_of_ints)
    bytes(string, encoding[, errors]) -> bytes
    bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
    bytes(int) -> bytes object of size given by the parameter initialized with null bytes
    bytes() -> empty bytes object

内置方法：

    capitalize()
    ...

# bytearray

python2:

bytearray表示可变字节数组类型．

bytearray是可变类型，是序列（可迭代）

    bytearray(int)
    bytearray(iterable_of_ints)
    bytearray(string, encoding[, errors])
    bytearray(bytes_or_bytearray)
    bytearray(memory_view)

内置方法和数据描述符：

    append(int)
    capitalize()
    ...

# memoryview

python2:

    memoryview(object)

内置方法和数据描述符：

    tobytes(...)
    tolist(...)
    ...

***

# enumerate

python2:

enumerate是一个内置的类类型，有next()内置方法，是迭代器．

    enumerate(iterable[, start]) # 返回一个可迭代的enumerate类型的迭代器，生成一个元组序列，包含从start 开始的索引，默认是０，和从iterable取出的值．
    a = enumerate([1,2,3])
    for i,item in a:
        print(i, item)
    type(a) # enumerate
    a.next()

# reversed

python2:

reversed是一个内置类类型，有next()方法，是迭代器．

    reversed(sequence) # 反转sequence序列的元素的值，返回反转后的reversed类型的迭代器．
    a = reversed((1,2,3))
    for i in a:
        print(i)
    type(a) # reversed
    a.next()

# type

python2:

    type(object) # 返回object对象的类型, 也就是对象的类型．
    type(name, bases, dict) #

内置方法和数据描述符：

    mro() # 返回一个类型的method resolution order

# slice

python2:

    slice(stop)
    slice(start, stop[, step])

内置方法和数据描述符：

    indices(len) -> (start, stop, stride)
    start
    step
    stop

***

# super

    super(type, obj) # 返回type类的基类对象，用来调用基类中的方法．
    super(type)
    super(type, type2)

# property

    property(fget=None, fset=None, fdel=None, doc=None) # 创建类的特性属性,通常在类内部通过@property装饰器来使用．

# classmethod

    classmethod(function) # 将函数转换成类方法，通常在类内部通过@classmethod装饰器来使用．

# staticmethod

    staticmethod(function)  # 将函数转换成静态方法，通常在类内部通过@staticmethod装饰器来使用．
