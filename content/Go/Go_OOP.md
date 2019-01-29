Title: Go_OOP
Date: 2018-01-01 10:49:21
Tags: Go, OOP



# Go面向对象

golang通过方法和接口实现面向对象.

***

# 方法/method

go中没有类，但是可以为结构体定义方法．

方法就是一类带有特殊的　接收者参数　的函数．

只能为同一包内定义的类型的接收者申明方法，不能为其它包内定义的类型的接收者申明方法．

除了结构体还可以为非结构体申明方法，但是不能为内建类型申明方法．

方法有两种接收者,值接收者和指针接收者.

    type Vertex struct {
        ...
    }

值接收者:

值接收者操作的是值的副本.

    func (v Vertex) MethodName() rType {
        ...
    }

    var v Vertex
    v.MethodName() // 操作值的副本

    # 使用指针接收者来调用值接收者的方法，编译器会自动做类型转换
    vp := new(Vertex)
    vp.MethodName() // 指针被解引用为值,(*vp).MethodName(),操作的是指针指向的值的副本.

指针接收者：

指针接收者，调用方法的时候操作的是该指针指向的值.

    # 指针接收者的方法可以修改接收者指向的值
    func (v *Vertex) MethodName() rType {
        ...
    }

    vp := new(Vertex)
    vp.MethodName() // 操作实际的值

    # 使用值接收者来调用指针接收者的方法，编译器会自动做类型转换.
    var v Vertex
    v.MethodName() // (&v).MethodName() , 操作的是实际的值

***

# 接口/Interface

接口是引用类型.

接口类型是由一组方法签名定义的集合．

接口类型的值可以保存任何实现了这些方法的值．

某个类型实现了该接口的所有方法签名，就算实现了该接口,无需显示申明实现了哪个接口.

接口可以匿名嵌入其它接口，或嵌入到结构中．

一般只有一个方法的接口命名为MethodName + 'er'.

接口存储两个数据接口：

* iTable, 包含存储值的类型信息以及和该值关联的方法.
* 指向存储的值的指针.

定义接口：

    type IName interface {
        MethodName()
        ...
    }

    type SName struct {
        ...
    }

值接收者方法:

接口类型的值为值或指针都可以调用该方法.

    func (s SName) MethodName() {}

指针接收者方法:

接口类型的值必须为指针才能调用该方法.

    func (s *SName) MethodName() {
        ...
    }

    s := &SName{...}
    // i = &SName{...} //接口变量能保存实现了该接口的任意类型的对象
    i = s
    i.MethodName()

    # 接口类型为值时，调用失败
    var s SName
    i = s
    i.MethodName() // 调用失败

底层值为nil的接口值:

    var i IName
    var s SName
    i = s    # 接口值为nil

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

    // i.(type) 是固定写法
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

接口中可以嵌入其它接口，这样实现了该接口的对象就隐式包含嵌入接口的所有方法.

    type Interface interface {}

***

## 封装

小写字母开头的标识符（类型/属性/方法...)是未公开的，只能在当前包引用，不能在其它包引用。

可以通过创建工厂函数对外暴露未公开的标识符:

* 标识符才有公开或未公开属性，值没有
* 短变量声明操作符，有能力捕获引用的类型，并创建一个未公开的类型的变量；显示声明的变量不能引用未公开类型。

通过工厂函数返回未公开类型的值:

    # packageA
    type privateType  Type
    func New(args) privateType {
        return privateType(args)
    }
    # packageB
    import packageA
    func main() {
        b := packageA.New(args) // 返回一个值，而不是标识符
    }

公开类型的未公开属性:

    # packageA
    type Public struct {
        private Type
    }

    # packageB
    import packageA
    func main() {
        b := packageA.Public{
            private: value, // panic, 公开类型的未公开属性不能通过字面量直接赋值
        }
    }

类型嵌套中的未公开类型的公开属性会提升到外部类型:

    # packageA
    type inner struct { // inner private
        In Type  // In public
    }
    type Outer struct {
        inner
        Out Type
    }

    # packageB
    import packageA
    func main() {
        b := packageA.Outer{
            Out: value, // 外部类型中的未公开内部类型不能通过字面量直接赋值
        }
        b.In = value // 内部类型的公开属性提升到外部类型。
    }

## 多态

形式参数是接口的函数，叫做多态函数.

    func FuncName(iVar IName) {}

所有实现了接口的方法的实体类型，就可以作为参数传给多态函数.

## 继承

通过类型嵌套实现继承，外部类型可以访问内部类型的属性和方法

如果外部类型实现同名的属性或方法，就会覆盖内部类型的属性或方法（不过内部类型的属性和方法还在，可以通过内部类型访问）

内部类型实现的接口，也会自动提升到外部类型。只要内部类型实现了某接口，外部类型相当于也实现了该接口。

如果匿名字段实现了一个方法，那么包含这个匿名字段的结构也可以调用该方法.

    type Inner struct {
        in Type
    }

    func (i *Inner) InnerMethod() {}

    type Outer struct {
        Inner    // 只需要类型名称，不需要声明变量
        out Type
        ...
    }

    outer := Outer{}

    outer.Inner.InnerMethod() //始终可以访问内部类型的方法，即使外部类型实现同名方法
    outer.Inner.in // 同上

    outer.InnerMethod() //如果外部类型没有实现同名方法，就是内部类型方法，否则是外部类型方法
    outer.in // 同上

***

# 反射/reflact

反射就是检查程序在运行时的状态.

使用反射一般使用标准库reflect.

