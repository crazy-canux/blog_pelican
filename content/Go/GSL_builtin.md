Title: GSL_builtin
Date: 2018-01-01 10:49:21
Tags: Go, builtin



# builtin

go的builtin package.

## constants

    true
    false
    iota

# variables

pointer, slice, map, channel, func, interface的零值：

    nil

## functions

    # 分配并初始化各种类型的对象, 返回一个指针．
    new(Type) *Type

    # 分配并初始化一个Slice/Map/Channel的对象,返回相同类型的对象.
    make(t Type, size ...IntegerType) Type

    # 返回容量，　Array/ArrayPointer/Slice/Channel
    cap(v Type) int

    # 返回长度，　String/Array/ArrayPointer/Slice/Map/Channel
    len(v Type) int

    print(args ...Type)

    println(args ...Type)

complex:

    # 把两个浮点数构造成一个复数
    complex(r, i FloatType) ComplexType

    # 返回复数c的实部
    real(c ComplexType) FloatType

    # 返回复数c的虚部
    imag(c ComplexType) FloatType

slice:

    # 向切片末尾追加元素，返回新的切片．切片长度增加.
    # 如果长度超过底层数组长度，就创建了一个新的底层数组. 否则底层数组不变．
    # 在元素不超过1000的情况下，自动创建的底层数组容量翻倍.
    append(slice []Type, elems ...Type) []Type

    # 复制一个切片, 返回复制的元素的个数
    copy(dst, src []Type) int

map:

    # 从映射删除一个键值对
    delete(m map[Type]1, key Type)

chan:

    # 由发送者关闭一个双向或只发送的信道
    close(c chan<- Type)

error:

    # 停止当前go程的正常执行(断言函数)
    panic(v interface{})

    # 管理panic过程中的go程
    recover() interface{}

## types

    bool

    uint
    uintptr
    uint8/byte (0 - 255)
    uint16
    uint32
    uint64

    int
    int8 (-128 - 127)
    int16
    int32/rune
    int64

    float32
    float64

    complex64
    complex128

    string

文档类型:

    Type
    Type1
    IntegerType
    FloatType
    ComplexType

## error

interface:

    // go使用error值来表示错误状态，nil表示成功，非nil表示失败．
    type error interface {
        ERROR() string
    }

