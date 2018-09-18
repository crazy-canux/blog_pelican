Title: GSL_oop
Date: 2018-01-01 10:49:21
Tags: Go, GSL, reflect



# reflect

## constants

const:

    const (
        SelectSend
        SelectRecv
        SelectDefault
    )

## functions

    // 将src拷贝到dst, 直到src被耗尽或dst被装满.
    func Copy(dst, src Value) int

    // 判断两个值是否深度一致
    func DeepEqual(a1, a2 interface{}) bool

## Kind

表示Type类型值表示的具体分类.

    type Kind uint

    const (
        Invalid Kind = iota
        Bool
        Int
        ...
        Uint
        ...
        Float...
        Complex...
        Array
        Chan
        Func
        Interface
        Map
        Ptr
        Slice
        String
        Struct
        UnsafePointer
    )

method:

    func (k Kind) String() string

## StringHeader

## SliceHeader

## StructField

## StructTag

## ChanDir

## SelectDir

## SelectCase

## Method

## Type

用来表示一个go类型.

interface:

    type Type interface {
        Kind() Kind
        Name() string
        PkgPath() string
        String() string
        Size() uintptr
        ...
    }

functions:

    // 返回接口中保存的值的类型
    func TypeOf(i interface{}) Type

    // 返回类型t的指针的类型
    func PtrTo(t Type) Type

    // 返回类型t的slice的类型
    func SliceOf(t Type) Type

    // 返回一个键类型为key, 值类型为elem的map类型
    func MapOf(key, elem Type) Type

    // 返回元素类型为t, 方向为dir的chan类型
    func ChanOf(dir ChanDir, t Type) Type

## Value

为go值提供反射接口.

struct:

    type Value struct {}

functions:

    // 返回一个接口i保存的具体值的Value
    func ValueOf(i interface{}) Value

    // 返回一个类型typ的零值的Value
    func Zero(typ Type) Value

    ...

methods:

    // 如果v是否持有值，如果v是Value零值，返回false.
    func (v Value) IsValid() bool

    func (v Value) IsNil() bool

    // 返回v持有值的分类，如果v是Value零值，返回Invalid
    func (v Value) Kind() Kind

    // 返回v持有的值的类型Type.
    func (v Value) Type() Type

    ...

***
