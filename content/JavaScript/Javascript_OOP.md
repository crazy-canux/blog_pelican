Title: Javascript_OOP
Date: 2017-03-15 09:36:32
Tags: Javascript, OOP



# OOP

javascript中一切都是对象.

javacript内置了Object/Array/Date/RegExp/Function类型.

# Object

创建Object实例:

    var obj = new Object();

    var obj = Object(); // new 可以省略

    var obj = ｛
        name: "value"
    };

    var obj = {
        "name": "value"
    }

添加属性:

    obj.attr = "value"

添加方法:

    obj.method =  methodName;
    function methodName() {};

    obj.method = function() {};

删除属性:

    delete obj.attr

访问对象属性:

    obj.property

访问对象方法:

    obj.method()

# Boolean

attribution:

    constructor
    prototype

method:

    toSource()
    valueOf()
    toString()

# Number

attribution:

    constructor
    prototype

    MAX_VALUE
    MIN_VALUE
    NaN
    NEGATIVE_INFINITY
    POSITIVE_INFINITY

method:

    valueOf()
    toString()

    toLocaleString()
    toFixed()
    toExponential()
    toPrecision()

# String

attribution:

    constructor
    prototype

    length

method:

    toSource()
    toString()
    valueOf()

    anchor()
    big()
    indexOf()
    replace()
    match()
    search()
    toLowerCase()
    toUpperCase()
    ...

# Function

attribution:

    Infinity
    java
    NaN
    Packages
    undefined

method：

    decodeURI()
    decodeURIComponent()
    encodeURI()
    encodeURIComponent()
    escape()
    eval()
    getClass()
    isFinite()
    isNaN()
    parseFloat()
    parseInt()
    String()
    unescape()

# Array

创建对象:

new都可以省略.

    var arr = new Array();

    var arr = new Array(size);

    var arr = new Array(element0, element1, ...);

    var arr = [];
    var arr = [1,2, "test"];

赋值:

    arr[index] = "value";

    // 字符串下标，不能直接通过数组对象访问，只能通过对象方法访问.
    arr["key"] = "value";

attribution:

    constructor
    prototype

    length // set或get数组中元素个数.

method:

    toSource()
    toString()
    valueOf()

    toLocaleString()

    join(separator) // 返回按照分隔符分隔的字符串
    concat() // 拼接

    push() // 往数组末尾添加元素,返回最新长度.
    pop() // 移除数组末尾元素,并返回

    unshift() // 在数组开头添加元素，返回最新长度.
    shift() //　移除数组开头元素并返回

    reverse() // 对数组逆序排序操作．
    sort(sortby) // 对数组顺序排序操作

    slice(start, end) // 取下标为start和end之间的元素，不包括start和end.

    splice(index, howmany, item1, ...) // 删除，插入，替换功能.
    splice(index, howmany) // 从index开始，获取howmany个元素
    splice(index, 0, item) // 从index插入item
    splice(index, 1, item) // 用item替换index的元素

# Date

创建对象:

    var date = new Date();

attribution:

    constructor
    prototype

method:

    toString()
    toSource()
    valueOf()

    Date()
    UTC()
    parse(datestring) // 返回datestring的epoch毫秒数

    toLocalString()
    toLocalTimeString()
    toLocalDateString(0)
    toUTCString()
    toGMTString()
    toDateString()
    toTimeString()

    get...

    set...

# RegExp

# Math

# Events
