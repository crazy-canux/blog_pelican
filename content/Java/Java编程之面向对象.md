---
layout: post
title: Java编程之面向对象
comments: true
date: 2016-04-03 10:49:07
updated:
tags:
- Java
categories:
- Java
permalink:
---

# 类(Class)

类是构造对象的模板或蓝图，由类构造对象的过程称为创建类的实例。

对象的三个主要特征：
1. 对象的行为
2. 对象的状态
3. 对象的标识

类之间的关系：
1. 依赖
2. 聚合
3. 继承

对象变量并没有实际包含一个对象，仅仅引用一个对象。

使用预定义类,java自带几千个类：

    <object-type> <object-name> = new <object>()

自定义类：

包含三个部分，域（field），构造器（constructor），方法（method）。

类名如果有多个单词组成，每个单词的首字母都要大写。

    class ClassName
    {
        field1
        field2
        ...
        constructor1
        constructor2
        ...
        method1
        method2
        ...
    }

匿名类：

匿名类还可以作为方法的参数。

    ClassName var = new ClassName; / 这是显示申明类 /
    new ClassName.Field;
    new ClassName.Method; / 这是匿名类 /

类设计技巧：
1. 一定要保证数据似有
2. 一定要对数据初始化
3. 不要在类中使用过多的基本类型
4. 不是所有的域都需要独立的域访问器或更改器。
5. 将职责过多的类进行分解。
6. 类名和方法名要能体现职责。

## 域(Field)

如果所有构造器方法都希望赋予相同的值，可以直接在申明时给域赋值。

域定义在类中，整个类都可以访问。

域存放在堆内存的对象中。

域随着对象的创建而创建，随着对象的消失而消失。

域都有默认初始化值，也可以手动初始化。

域：

域中的所有数据最好都是private。

    private type name;

用final修饰的是常量域,构造器必须初始化这个域,并且不能再修改。

    private final type name;

静态域：

用static修饰的是静态域,静态域属于类，不属于任何对象，是唯一的。

    private static type name;
    ClassName.name; # 通过类来访问

static和final修饰的是静态常量。

    private static final type name = value;
    ClassName.name; # 通过类来访问

初始化块：

在域中放初始化块，只要构造类对象就会在运行构造器方法之前运行初始化块。

    {
        var = val;
        ...
    }

    / 静态初始化块 /
    static
    {
        var = val;
        ...
    }

## 方法(Method)

java中所有的方法都要在类的内部定义。

方法有修饰符，返回值类型，方法名和参数组成。

一种特殊方法，如果方法没有返回值，return后面直接分号，用修饰符void代替返回值类型。

方法名如果有多个单词组成，首字母小写，后面的单词首字母大写。

    <decorate>... <type> <function_name>(<type> <argument>, ...)
    {
        statements;
        return <value>;
    }

    <decorate>... void <functionName>(<type> <arguments>, ...)
    {
        statements;
        return;
    }

对域进行读取的方法叫域访问器，用getFunction（）表示。

对域进行设置的方法叫域更改器，用setFunction（）表示。

方法的参数有显示参数和隐式参数，类对象（实例）就是隐式参数，用关键字this表示。

静态方法：

静态方法就是不面向对象的方法，也就是没有隐式参数this。

静态方法只能访问自身类中的静态域,不能访问非静态域。

    public static type name(arguments)
    {
        ...
    }
    ClassName.name(arguments); # 用类名来调用

方法参数：

java方法参数是值调用，不是引用调用。

一个方法不可能修改一个基本数据类型的参数的值。

一个方法可以改变一个对象参数的状态。

一个方法不能让对象参数引用一个新的对象。

参数数量可变的方法：

    public static double max(double... values)
    {
        ...
    }

## 构造器(Constructor)

1. 构造器与类同名
2. 每个类可以有多个构造器
3. 构造器可以有任意个参数
4. 构造器没有返回值
5. 构造器总是随new一起调用
6. 不要在构造器中定义与域重名的局部变量

重载：

多个构造器方法名字相同，参数不同，构成重载，编译器自动找匹配的构造器方法执行，找不到就编译错误。

推荐在构造器方法中对域进行初始化，避免使用默认的初始化。

当类没有提供任何构造器，系统会默认提供一个无参数的构造器，如果有至少一个构造器，而且没有提供无参数构造器，就不能用无参数的构造器初始化对象。

构造器方法的参数：

    / 在前面加个a和域区分开 /
    public ConstructorName(type aName)
    {
        ...
    }

    / 和域同名，但是引用域需要加this区别 /
    public ConstructorName(type name)
    {
        this.name = name;
    }

    / 一个构造器方法内部调用另外的构造器方法 /
    public ConstructorName(type name)
    {
        this("other argument", name);
    }

***

# 封装

一个源文件只能包含一个public修饰的公有类，而且文件名要和这个类同名。

编译器查找类的顺序：
1. 默认导入的包java.lang
2. 用import导入的其它包中的公有类
3. 当前包中的公有类，或导入的当前包的非共有类。

编译器找到一个以上的同名类就报错，因为类必须是唯一的。

编译器还会查看源文件，如果比类文件新就会自动编译源文件。

类的路径要和包名匹配，需要设置类路径，类路径是所有包含类文件的路径的集合。

jar文件包含多个压缩形式的类文件和子目录。

用classpath当作类路径，linux/unix用冒号：隔开，windows用分号;隔开：

    export CLASSPATH=/class/path:.:/jar/path

    set CLASSPATH=c:\class\path;.;c\jar\path

可见性：
1. private, 仅对本类可见
2. default, 默认不用修饰符,对本包可见。
3. protected， 对本包和所有子类可见
4. public， 对所有类可见

# 继承

关键字extends表示继承,java中的所有继承都是公有继承。

已存在的类称为超类，基类，或父类。

新类称为子类，派生类，或孩子类。

    class SubClass extends Class
    {
        ...
    }

在子类中使用super来调用父类的同名的方法

    public type getFunction()
    {
        type var = super.getFunction();
        ...
    }

在子类构造器方法中使用super来调用父类同参数的构造器方法

该语句必须放在构造器的第一句，如果没有显示用super调用，默认调用父类的默认构造器

    public SubClass(arguments)
    {
        super(arguments);
        ...
    }

继承可以是多层继承，由一个公共类派生出来的所有类的集合称为继承层次。

java没有多继承，继承不能扩展多个类，一个子类只能继承一个父类，一个父类可以被多个子类继承。

不允许被扩展的类称为final类，用final修饰:

final类中的所有方法(不包括域)自动的成为final方法

    final class SubClass extends ClassName
    {
        ...
    }

类中的特定方法也可以被申明为final，子类就不能覆盖这个方法：

    class ClassName
    {
        ...
        public final type MethodName()
        {
            ...
        }
        ...
    }

将父类转换成子类：

只能在继承层次内进行转换，在转换之前应该使用instanceof检查能否检查。

只有父类转换成子类需要强制转换，子类对象引用父类可以直接引用。

    if (FatherObject instanceof SubClass)
    {
        SubClass = (SubClass) FatherObject;
        ...
    }

抽象类：

用abstract修饰的方法是抽象方法，包含抽象方法的类必须用abstract修饰为抽象类。

最基本的类可以作为抽象类，申明抽象方法，在子类中实现方法。

抽象类不能被实例化，但是可以引用非抽象子类的对象。

    abstract class ClassName
    {
        ...
        public abstract type methodName();
        ...
    }

Object类：

Object类是java中所有类的基类，如果一个类没有用extends明确父类，Object就是它的默认父类。

可以用Object类型的变量引用任何类型对象。

参考java.lang.Object的方法。

继承的技巧：
1. 将公共操作和域放在父类
2. 不要使用受保护的域
3. 使用继承实现"is-a"关系
4. 除非所有继承的方法都有意义，否则不要使用继承
5. 在覆盖方法时，不要改变预期的行为
6. 使用多态，而非类型信息
7. 不要过多的使用反射

# 多态

一个对象变量可以指示多种实际类型的现象被称为多态。

java中的对象变量是多态的。

编译器查看对象的申明类型和方法，列出该类中所有同名方法和父类中同名的public方法，再查看调用方法时提供的类型参数，如果找到完全匹配的就调用这个方法，这个过程叫重载解析。

如果是private方法，static方法，final方法，或者构造器方法，编译器可以准确的知道调用哪个方法，这个过程叫静态绑定。

虚拟机预先为每个类创建一个方法表，列出所有方法的签名和实际调用的方法。

***

# 接口(Interface)

接口用interface来定义。

接口中所有方法自动属于public，所以不用加public。

接口不能有域和方法，这些应该在实现接口的类中定义。

一个接口的例子，java8有1121个接口：

    public interface Comparable<T>
    {
        int compareTo(T other);
    }

怎样让类实现一个接口：
1. 用implements将类申明为实现给定的接口
2. 对接口中所有方法定义(在自定义类中实现接口中的方法)

        Class <Class_Name> implements <Interface_Name>
        {
            public int <Method_Name>(...)
            {
                ...
            }
        }

接口的特性：
1. 接口不是类，不能用new实例化一个接口。
2. 可以申明接口变量， Comparable x;
3. 接口变量必须引用实现了接口的类对象。
4. 检查一个对象是否实现了某个特定的接口，if (anObject instanceof Comparable) {...}
5. 接口像类一样可以用extends扩展。
6. 接口中不能用实例域和静态方法，但是可以有常量。
7. 一个类中可以实现多个接口，implements Interface1, Interface2。

***

# 包(Package)

标准java类库分布在多个包中，包方便类的管理。

使用包要确包类名唯一。

sun建议使用公司域名的逆序作为包名。

使用import导入包：

    import java.util.*;

只能用*导入一个包，不能用java.*导入所有包。

导入多个包，有类在使用时重名，写全路径：

    import java.util.*;
    import java.sql.*;
    java.util.Date deadline = new java.util.Date();
    java.sql.Date today = new java.sql.Date();

使用import导入包中的静态域和静态方法：

    import static java.lang.System.*;
    import static java.lang.System.out;

将类放入包中：

在类的源文件开头添加一行语句,源文件要放到包名对应的目录结构中。

    package package_name;

***

# 异常和错误
