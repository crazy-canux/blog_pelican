Title: Go
Date: 2018-01-01 10:49:21
Tags: Go



# Go概述

go语言表达能力强，简洁，清晰，高效．

go是一个快速的，静态的，强类型的，编译型语言．

go具有高并发和垃圾回收功能.

***

# Go基本语法

go源程序叫*.go

go大小写敏感

go程序都是由包组成，程序的入口是main包中的main函数，每个程序有且只有一个．

go中只有首字母大写的名称才能从包中导出．

go的类型在变量名后面．

go函数外的每个语句都必须以关键字开始.

go标识符(函数名／变量名／常量名／类型名／语句标号／包名)以字母或下划线开头，后面还可以包含数字．

go使用大括号{}表示一个代码块.

go使用分号;表示一个语句结束, 一般一行写多个语句才需要显示添加分号．

go的包名一般是小写的单个单词(文件所在的最后一层目录名).

go一般使用驼峰命名法.

go没有逗号操作符.

go中++/--是语句不是表达式．

go中大写字母开头的变量或函数是公有的，小写字母开头的是包私有的.

***

# Go注释

单行注释：

    // comment

多行注释：

    /* comment */

***

# Go关键字

    var const
    break continue for if else switch case default goto fallthrough
    func return defer
    package import
    range type struct map
    interface
    select go chan

***

# Go运算符和优先级

go中的运算都是从左到右结合．

    ^    #
    !    # 逻辑非

    *
    /    # 结果取整数
    %
    <<   # 位运算，左移
    >>   # 位运算，右移
    &    # 位运算，　按位与
    &^   #

    +
    -
    |    # 位运算,按位或
    ^    # 位运算,按位异或

    ==
    !=
    <
    <=
    >
    >=

    <- # chan运算符

    &&   # 逻辑与
    ||   # 逻辑或


***

# Go数据类型

## 变量

定义/申明变量:

通过关键字var在包或函数中申明/定义变量

全局变量必须使用var关键字．

没有初始化的变量在申明的时候赋予零值.

已经申明但没有使用的变量在编译时会报错．

通过等号给变量赋值就是定义变量.

大写字母开头的变量是public, 小写字母开头的是private变量.

申明变量:

    # 一个变量一种类型
    var varname Type

    # 多个变量一种类型
    var varname varname1 ... Type

定义(初始化)变量:

    # 定义的时候初始化
    var i, j int = 1, 2
    # 初始化使用表达式可以省略类型，从值中获取类型
    var i, j = true, "str"

    # 多个变量多种类型
    var (
        var1 Type1 = val1
        var2 Type2 = val2
        # 给类型取别名
        variable alias Type = value
        ...
    )

特殊变量：

    _  # 下划线是个特殊变量名，用于忽略一个值.

## 常量

定义常量：

通过关键字const在包或函数中定义常量．

    # 常量可以是bool, string, 数值
    const Pi float = 3.14
    const World = "China"
    const Truth = true
    # 定义多个常量
    const (
        Pi = 3.14
        ...
    )

枚举:

    # iota内置常量用来统计枚举中的行数
    const (
        con = val
        ...
    )

## bool

bool类型变量的零值是false.

bool类型是值传递．

    true
    false

## 数值类型

数值类型变量的零值是0.

数值类型是值传递.

有符号类型：

    int int8 int16 int32(rune) int64

无符号类型:

    uint uint8(byte) uint16 uint32 uint64 uintptr

int, uint, uintptr 在32位系统是32bit, 在64位系统是64bit

浮点类型：

    float32
    float64

复数类型：

    complex64
    complex128

## string

string类型变量的零值是"".

string类型是值传递.

go中的字符串都采用utf-8编码.

go中的字符串用双引号  或者　反引号

    # 单行字符串
    var str string = "hello"
    # 多行字符串(原样输出)
    var str string = `hello
                     world`

    var str = "hello" // 类型可以通过值确定

go中的字符串是不可变的, 修改字符串：

    # 使用类型转换
    var str string = "hello"
    c := []byte(str) # str转换成 []byte 类型
    c[index] = value # 重新赋值
    newString := string(c) # []byte 转换成 string

    # 使用索引运算
    s := "hello"
    s = "str" + s[1:]

字符串运算：

    s1 := "hello"
    s2 := "world"
    s3 := s1 + s2

遍历字符串：

    for index, value := range s {...}
    for index := range s {...}
    for _, value := range s {...}

## 结构体/struct

结构体就是字段的集合．结构体字段通过点操作符来访问．

结构体是值传递.

申明一个结构体类型：

    type StructName struct {
        var Type
        var1 Type1
        ...
    }

申明多个结构体类型:

    type (
        StructB struct {
            ...
        }

        StructB struct {
        }
    )

申明一个结构体类型的变量

    var s StructName

定义结构体变量:

    # 列出全部字段
    var s = StructName{val, ...}
    s := StructName{val, ...}

    # 使用val: 可以仅列出部分字段, 未列出的字段使用默认值
    var s = StructName{
        var: val,
        ...
    }
    s := StructName{
        var: val,
        ...
    }

    # 给字段赋值
    s.var1 = value

结构体指针:

    type StructName struct {
        var Type
        var1 Type1
    }

    var s = &StructName{}
    s := &StructName{}

    (*s).Var1 = val1
    s.Var1 = val1 // go允许隐士间接引用

    s := StructName{val, val1}
    p := &s
    # 原本应该通过(*p).var来访问，go允许隐式间接引用．
    p.var = p.var1

## 指针/pointer

指针的零值为nil.

go的指针保存了值的内存地址, go没有指针运算．

通过指针实现引用传递.

申明一个指针变量：

    var point *int

&操作符会生成一个指向其操作数的指针(保存变量的地址)：

    point = &variable

*操作符表示指针指向的数值(读写该地址保存的值：

    *point = value

## 数组/array

数组通过下标来访问．数组不能改变大小（长度）

数组是值传递．

数组的属性有类型和长度,只有长度和类型都相同的才是同类型数组,才能相互赋值.

数组长度和容量相同．

申明数组:

    var ArrayName [number]Type

定义数组：

    var ArrayName = [number]Type{}

    ArrayName := [number]Type{val, val1, ...}
    ArrayName := [number]Type{index: value, ...} // 给指定索引赋值,其余为零值
    ArrayName := []Type{val, ...} // 容量也可以由初始化的元素个数决定.

    ArrayName := [number]*Type{0: new(int), 1: new(string), ...} // 指针数组

数组元素赋值：

    ArrayName[0] = val

    *ArrayName[0] = val // 指针数组

数组赋值（值传递）：

    # 只有类型和长度相同的数组才能赋值
    # 非指针数组赋值，会另外开辟地址空间.
     # 修改newArray的值，不会改变ArrayName的值
     newArray = ArrayName

    # 指针类型的数组赋值，指向的是相同的地址.

多维数组(嵌套数组):

    doubleArray := [2][4]int{[4]int{1, 2, 3, 4}, [4]int{5, 6 7, 8}}

遍历数组：

    for index, value := range a {
        fmt.Println('%d, %d\n', index, value)
    }

    # 只要索引, 去掉,value即可
    for index := range a {...}
    # 只要值，用_忽略索引
    for _, value := range a {...}

## 切片/slice

切片的零值是nil, nil切片的长度和容量都是０，且没有底层数组．

切片传递的是地址(引用传递),修改切片的元素值其实就是修改底层数组的对应的元素的值,共享该元素的其它切片的值也相应改变．

切片的属性包括指向底层数组的指针，切片的长度，切片的容量.

切片不存储数据，只是描述数组的一段,因此切片不指定大小（长度）.

    # 表示切片类型
    []Type

申明切片:

    var SliceName []Type

定义切片：

    // 通过字面量定义
    var SliceName = []Type{}
    SliceName := []Type{val, val1, ...}

    SliceName := []Type{index: value}   // 索引就表示长度和容量

    // 通过make函数创建切片
    var SliceName = make([]type, len, cap)
    SliceName := make([]Type, len, cap)

通过切片定义新切片:

    切片的操作返回新的切片。
    NewS := SName[i:j]
    cap(SName) = k
    NewS 长度和容量：
    len = j-i
    cap = k-i
    NewS 无法访问指向的底层数组第一个元素之前的元素。
    也不能访问超出长度之后的索引,但是可以通过append增加切片长度之后访问.
    NewS[index] //当index >= j编译器报错 ，超出了NewS 的长度，无法访问。

三索引操作:

    NewS := SName[i:j:k]
    三索引表示容量， i:j 表示长度， i:k 表示容量.
    容量不能超过可用容量(也就是SName的容量).

切片操作：

    # 半开区间，不包括最后一个下标
    s[low:high]
    s[:high] // low=0, default
    s[low:] // high=max, default
    s[:] // s[0:max], default

    s[:0] // 把切片的长度变为０（清空切片)
    s[:4] // 扩展为４
    s[2:] // 扩展为 arrayname[2:4]

二维切片：

    [][]Type

遍历切片：

    # 切片遍历和数组相同
    for index, value := range s {
        ...
    }
    for index := range s {...}
    for _, value := range s {...}

slice作为函数参数:

    切片作为函数参数，传递的其实是值,函数会使用和切片相同的底层数组创建一个新的切片来操作.
    所以函数内部修改了切片的值,作为参数的切片的值也被修改了.

## 映射/map

映射的零值是nil, 既没有键，也不能添加键．

map是引用传递．是存储键值对的无序集合.

map是无序的，只能通过key索引，没有下标操作.

map的key需要支持==或!= 运算，不能是函数，映射，切片

申明:

    // 申明值为nil的空映射，不能用于存储键值对.
    var MapName map[keyType]ValueType

定义映射：

    var MapName = map[keyType]ValueType{}
    var MapName = map[keyType]ValueType{
        key: value,
        ...
    }

    MapName := map[keyType]valueType{}
    MapName := map[KeyType]ValueType{
        "key": value,
        ...
    }

    # 通过make定义map
    var MapName = make(map[keyType]ValueType, cap)
    MapName := make(map[keyType]ValueType, cap)

映射操作：

    m[key] = value

    value = m[key]
    # 若key在m中ok为true, 否则为false, 且value是对应类型的零值
    value, ok := m[key]

遍历映射：

    for key, value := range m {...}
    for key := range m {...}
    for _, value := range m {...}

map作为函数参数:

    不会创建该映射的副本，该函数对映射的修改就是对原始参数指向的映射的修改.

## 类型转换

go中兼容的类型才能转换，而且必须显示转换．

    ValueA [:]= TypeA(ValueB)

    floatA := float64(uint64Var)

***

# Go控制流

go控制流的左大括号不能另起一行．

## for循环

go只有for可以循环．

    for i := 0; i < 10; i++ {
        sum += i
    }

for循环有三种模式：

for循环后面没有小括号，代码块必须要大括号．

    for init; condition; statement {
        ...
    }

for循环的初始化语句init和后置语句statement可以省略,相当于while．

    for condition {
        ...
    }

无限循环, 相当于for(;;)：

    for {
        ...
    }

## if条件语句

if后面的小括号不要，但是代码块需要大括号．

    if condition {
        ...
    } else if condition {
        ...
    } else {
        ...
    }

## switch条件语句

go中的switch-case的variable无需为常量，且取值可以不是整数．

go中的只执行匹配的case，相当于默认在每个case后面加了break语句．

case匹配到的语句如果只有一行可以和case语句写在同一行

    switch variable {
    case value1:
        ...
    case value2: expression
    default:
        ...
    }

多个条件可以放到一个case:

    switch variable {
        case value1, value2, ...: expression
        case valuen: fallthrough
        defalut:
            ...
    }

没有条件的switch-case

    switch {
    case condition:
        ...
    ...
    }

如果不需要默认的break,需要添加fallthrough:

fallthrough不会判断后面的case的condition,而是直接执行后面所有的case.

    switch variable {
    case val1:
        ...
        fallthrough
    ...
    }

## label

golang的label不需要缩进:

    LabelName:

## break

break用于跳出for/switch/select循环.

    break

break也支持label:

break的label可以跳出外层循环.

    break [tag]

    label:
    for i := 0; i < 1000; i++ {
        for j :=0; j < 1000; j++ {
            if j < i {
                break label // 跳出最外层循环.
            }
        }
    }

## continue

continue语句只能在for循环中使用

    continue

continue也支持label:

continue的label可以从外层循环继续执行.

    continue [tag]

    next:
    for outer := 2; outer < 3000; outer++ {
        for inner :=2; inner < outer; inner++ {
            if outer%inner == 0 {
                continue next // 并非继续内存循环，而是从外层循环继续执行.
            }
        }
    }

## goto

goto跳转语句，跳转到指定标签运行．

标签区分大小写.

    Label:
        expression

    ...
    goto Label
    continue LABEL
    break LABEL
    ...

***

# Go函数

函数的零值是nil.

函数是引用类型.

大写字母开头的函数是public, 小写字母开头的是private.

创建函数：

    func FuncName(var Type, var1 Type1) rType {
        ...
        return ...
    }

多值返回：

    func FuncName(var Type) (rType, rType1, ...) {
        ...
        return ...
    }

命名返回值(必须用括号)：

    // 一般return后面不带返回值，否则需要返回定义的所有变量
    func FuncName(var Type) (rvar rType, rvar1 rType) {
        ...
        rvar = ...
        rvar1 = ...
        return
    }

多个变量类型相同时保留最后一个的类型即可：

    func FuncName(var, var1 Type) (rvar, rvar1 rType) {
        ...
        return ...
    }

变量作用域：

    函数内部定义的变量是局部变量
    函数外定义的变量是全局变量．
    局部变量优先使用．

形式参数：

    形式参数的作用域范围和函数体中的局部变量一致．

返回值：

    函数返回值的作用域范围和函数体中的局部变量一致．

实际参数：

    实际参数可以是值传递，也可以是引用传递．

指针参数：

    # 实参必须是指针才能调用该函数
    func FuncName(v *Type) rType {
        ...
    }

函数中短变量申明(局部变量):

    # 在函数内部，明确值的类型的情况下可以用 := 代替var关键字定义变量
    func FuncName() {
        variable := value
        var1, var2, ... := val1, val2, ...
    }

重复申明短变量：

    本次申明与已申明的变量在同一作用域．
    在初始化中与已申明的变量类型相同才能赋值．
    本次申明中至少另有一个变量是新申明的．

defer关键字：

defer会将函数推迟到外层函数返回之后执行.

推迟调用的函数其参数会立即求值，然后压入defer栈中,外层函数返回后按照后进先出的顺序调用．

    func FuncOut() {
        ...
        defer FuncName()
        ...
    }

函数也是值，也可以传递，可以用作函数的参数或返回值：

    func FuncName(variable func(Type, ...) rType) rType {
        ...
    }

    FuncName := func(variable Type, ...) rType {
        ..
    }

匿名函数:

    func(<arguments>) (returns) {}()

可变参数:

    func FuncName(vars ...Type) rType {}
    FuncName(vars..)

closures/闭包:

init函数:

    # 每个包中可以有任意个init函数.
    # 这些init函数会在main函数执行之前调用.
    # init函数不能有参数和返回值
    func init() {}

***

# Go文件和输入输出

go的标准库fmt实现了类似于C语言的printf和scanf格式化I/O函数.

还有io和bufio标准库可用

## 输入

输入的本质就是从Stdin读取

fmt:

    var input string
    fmt.Scan*(&input)

bufio.Reader:

    inputReader := bufio.NewReader(os.Stdin)
    inputReader.Read*()

## 输出

输出的本质就是往os.Stdout写

fmt:

    fmt.Print*()

os.File:

    os.Stdout.Write*("hello")

bufio.Writer:

    outputWriter := bufio.NewWriter(os.Stdout)
    outputWriter.Writer*()
    outputWriter.Flush()

## 文件

标准库os.File结构的指针用来表示文件句柄

标准库bufio提供了带缓冲的操作

读文件

    readFile, err := os.Open("filename")
    readFile.Read*()

    inputReader := bufio.NewReader(readFile)
    inputReader.Read*('\n')

写文件

    writeFile, err := os.Create("filename")
    writeFile.Write*()

    outputWriter := bufio.NewWriter(outputFile)
    outputWriter.Write*("string")
    outputWriter.Flush()

***

# Go错误和异常

go的标准库errors实现了用于错误处理的函数.

内置函数panic是断言函数，会触发一个异常，用于终止当前的线程(会在defer执行完之后终止线程)

内置接口定义了error接口类型, error类型都有一个Error方法.

    type error interface {
        Error() string
    }

定义错误:

    var errName error = errors.New("error message.")

    err := errors.New("error message.")

    err := fmt.Errorf(format string, a ...interface{})

panic:

相当于抛出一个异常，在运行完defer之后,返回到调用者继续运行defer，直到最外层的defer执行完毕，终止程序.

    panic(v interface{})
    panic("ERROR: command not found")

recover:

只能用于defer修饰的函数，用于接收panic调用中传递过来的错误值,没有panic返回nil.

当前函数的后面不会被执行，recover捕获异常之后会返回到调用者继续执行.

相当于catch一个异常.

    recover() interface{}
    defer func() {
        if err := recover(); err != nil {
            fmt.Println(e)
            // "ERROR: command not found"
        }
    }()

总结：

1. 在包内部，总是应该从panic中recover．
2. 总是向包的调用者返回错误值，而不是panic.

***

# Go包

创建包：

包名一般和所在路径的最后一层目录一致．一般是小写的单个单词.

同一个目录中的代码文件使用同一个包名．

    package pkg1

单个导入:

    import "pkg1"
    import "pkg2"
    # 导入时创建别名
    import alias "pkg"

组合导入:

    import (
        "pkg1"
        "pkg2"
        ...
    )

包内的函数名首字母大些才能被其它包导入，否则就是私有的．

命名导入:

    import (
        alias "pkg" # 给包取别名
    )

导入副作用：

只执行导入包中的init函数并初始化全局变量，不导入其它内容．

编译时不检查该导入是否使用.也不能通过包名调用其中的导出函数.

    import _ "path/pkg"

    import (
        _ "path/pkg"
    )

go包查找顺序:

    $GOROOT/src/... # 安装golang的路径里面的标准库
    $GOPATH

***

# Go文档

通过注释编写文档，godoc会自动识别．对包，函数，类型，全局变量都可以.

    // this is documents
    func Fucntion() {}

    /*
        This is documents
    */
    type St struct {}

也可以给包写一段文字较多的文档，通过在包内创建doc.go.

这段文档会显示在所有其它文档之前．

    # vim doc.go
    /*
        This docs for package
        ...
    */
    package pkg # 使用和包一样的名字.

***
