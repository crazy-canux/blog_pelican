Title: Go_OOP
Date: 2018-01-01 10:49:21
Tags: Go, OOP



# Go面向对象

***

# 方法/Method

go中没有类，但是可以为结构体定义方法．

方法就是一类带有特殊的　接收者参数　的函数．

只能为同一包内定义的类型的接收者申明方法，不能为其它包内定义的类型的接收者申明方法．

除了结构体还可以为非结构体申明方法，但是不能为内建类型申明方法．

    type Vertex struct {
        ...
    }

    func (v Vertex) MethodName() rType {
        ...
    }

    v.MethodName()
    (*Vertex).MethodName(&v)

指针接收者：

指针接收者的方法被调用，接收者既可以是指针也可以是值, 编译器会自动做类型转换.

对于非指针接收者，编译器也会自动做类型转换，而不必显示传值还是指针．

    # 指针接收者的方法可以修改接收者指向的值
    func (v *Vertex) MethodName() rType {
        ...
    }

## 封装

public: 包内的通过首字母大写，可以被其它包导入．

private: 包内的通过首字母小写，只能在包内使用.

## 继承

如果匿名字段实现了一个方法，那么包含这个匿名字段的结构也可以调用该方法.

## 多态

包含该匿名字段的结构也可以实现自己的同名方法来覆盖匿名字段的方法.

***

# 接口/Interface

接口类型是由一组方法签名定义的集合．

接口类型的值可以保存任何实现了这些方法的值．

某个类型实现了该接口的所有方法签名，就算实现了该接口,无需显示申明实现了哪个接口.

接口可以匿名嵌入其它接口，或嵌入到结构中．

一般只有一个方法的接口命名为MethodName + 'er'.

定义接口：

    type IName interface {
        MethodName()
        ...
    }

    type SName struct {
        ...
    }

    func (s *SName) MethodName() {
        ...
    }

    var i IName

    s := &SName{...}
    i = s

    // 接口变量能保存实现了该接口的任意类型的对象
    i = &SName{...}
    i.MethodName()

底层值为nil的接口值:

    var i IName
    var s SName
    i = s    # 接口值为nil
    i.MethodName()

空接口：

所有类型都实现了空接口.

指定了零个方法的接口值被称为空接口,一般用来处理未知类型的值.

当接口储存的类型和对象都为nil，接口才为nil

以空接口为参数的函数可以接收任意类型的值作为参数.

如果一个函数返回空接口就可以返回任意类型的值.


    # 空接口可以保存任何类型的值
    var i interface{}
    # 空接口作为形参
    func FuncName(i interface{}) {}

指针的类型断言/comma-ok断言：

断言接口值i保存了具体类型Type, 并将底层类型为Type的值赋予变量t.

    只返回一个值，断言失败会触发panic.
    t := i.(Type)

    返回两个值，断言成功返回true, 失败返回false.
    t, ok := i.(Type)

指针的类型选择/switch测试：

    switch TypeValue := i.(type) {
    case Type1:
        ...
    case Type2:
        ...
    ...
    default:
        ...
    }

嵌入接口:

接口中可以嵌入其它接口，这样实现了该接口的对象就隐式包含嵌入接口的方法.

***

# 反射/reflact

反射就是检查程序在运行时的状态.

使用反射一般使用标准库reflect.

