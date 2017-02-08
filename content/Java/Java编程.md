---
layout: post
title: Java编程
comments: true
date: 2016-04-03 10:49:07
updated:
tags:
- Java
categories:
- Java
permalink:
---

# java概述

Java的三个体系:
1. J2SE: 标准版
2. J2EE: 企业版(包括J2SE)
3. J2ME: 微型版

Java的版本：
1. OpenJDK
2. Oracle JDK
3. IBM JDK

java命令:
1. java      运行程序
2. javac     编译器
3. jdb       调试器
4. jar       归档工具
5. javadoc   文档工具

java的ide:
1. eclipse(IBM)
2. netbeans(Oracle)

Java的架构：

![pic](/images/java.PNG)

***

# java基本语法

java源程序叫Xxx.java

java是强类型语言。

java大小写敏感。

java使用骆驼命名法.

包名全部小写.

类名/接口名,首字母大写,中间单词的首字母都大写.

变量名/类中的域名/类中的方法名,首字母小写,中间单词首字母都大写.

类中的构造器名,要和类名相同.

常量名全部大写.

java语句要用分号；结尾, 用{}表示一个代码块, import语句也需要分号;。

java程序以类的形式出现，类名单词首字母大写。

java源代码文件名要和公共类的名字相同。

java标识符：字母和下划线开头，可以包含数字，不能是关键字。

一个类要独立运行需要main函数。

# java注释

单行注释:

    // comment

    /* comment */

多行注释:

    /*
     * comment1
     * comment2
     */

# java关键字

## 数据类型

boolean, int, long, short, byte, float, double, char, class, interface

## 流程控制

if, else, for, do, while, switch, case, default, break, continue, return, try, catch, finally.

## 修饰符

public, protect，private，final，void， static， staticfp， abstract， transient， synchronized， volatile, native,

## 动作相关

package, import, throw, throws, extends, implements, this, super, instanceof, new.

## 保留字

true, false, null, goto, const.

# 数据类型

java有8种基本数据类型

## 整数类型

1. byte 1 字节

2. short 2字节

3. int 4字节

4. long 8字节，后缀为L

byte可以转换成short, short可以转换成int, int可以转换成long.

int和long都可以转换成浮点型.

## 浮点类型

1. float  4字节

2. double  8字节，后缀为F

float可以转换成double类型.

三个表示出错和溢出的浮点数:

正无穷

负无穷

NaN

## 字符类型

1. char 表示单个字符

char类型可以转换成int类型.

## 布尔型：

1. Boolean 两个值true和false表示真和假。

在java中整形值和布尔值不能转换。

## 进制：

前缀0b表示二进制

前缀0表示八进制

前缀0x表示十六进制

## 变量

也就是局部变量，和类中的域有区别。

局部变量定义在局部代码块中，只在所属区域有效。

局部变量存放在栈内存的方法中。

局部变量随着所属区域的执行而存在，随着所属区域结束而释放。

局部变量没有默认初始值，必须手动初始化。

    int <variable> = <value>

变量需要先申明类型,然后再初始化, 最后才能使用.

最好逐一申明每个变量.

变量的申明最好靠近第一次使用的地方.

## 常量:

使用final修饰的是常量，只能被赋值一次。

    final int <VAR> = <val>

# java运算符

## 算术运算

> +

> -

> *

> /    当除法两个操作数都是整数时结果是整数，否则是浮点数。

> &    求余数

## 自增运算/自减运算

>> ++n/--n    当前表达式n的值就要加1。

>> n++/n--    当前表达式n的值不变，下一个表达式n的值加1。

## 赋值运算

>> =

>> +=

>> -=

>> *=

>> /=

>> &=

## 关系运算

>> ==

>> !=

>> <

>> >

>> <=

>> >=

>> instanceof(检查是否是类的对象）

## 逻辑运算(boolean运算符)

>> && (AND短路)

>> || (OR短路)

>> ! (NOT)

## 位运算

>> & (AND)

>> | (OR)

>> ^ (XOR)

>> ~ (非)

>> a<<b (a左移b位),地位补0。

>> a>>b (a右移b位)，高位是符号位。

>> >>> (无符号右移，高位始终补0)

## 三目运算：

>> x?y:z

***

# 枚举类型

变量的值只在一个有限的集合内，可以定义枚举类型。

定义枚举类型:

    enum <enum_name> { val1, val2, ..., valN };

申明枚举类型

    <enum_name> <variable> = <enum_name>.varX

***

# 数组

数组就是一个容器，存储相同数据类型的集合。

数组大小不能改变，只能改变数组元素的大小。

## 一维数组

申明数组两种方法：

    int[] array; // 推荐
    int array[];

使用new初始化数组：

需要用new创建一个数组,n可以是变量,也可以是0.

数字数组初始化为0,布尔类型初始化为false，对象类型初始化为null（包括String类型）。

    int[] array =  new int[n];

直接初始化数组：

    int[] array = new int[]{<val1>, <val2>, ...};
    int[] array = {<val1>, <val2>, ...};

创建并初始化匿名数组,可以直接将匿名数组赋值给别的数组:

    new int[]{<val1>, <val2>, ...};

用for访问数组元素，下标从0开始,下标不能越界:

    for (int i = 0; i < n; i++)
        array[i] = <value>;

使用for each访问数组元素：

    for (int <variable> : array)
        System.out.println(<variable>)

length函数求数组长度：

    array.length

数组拷贝：

将一个数组变量拷贝给另一个数组变量，两个变量引用同一个数组,

也就是说任意改变一个元素的值，另一个数组的对应元素值也改变。

    int[] array1 = array;

将一个数组所有值拷贝给一个新数组：

java.util.Arrays.copyOf()仅仅是把一个数组的所有值拷贝给另一个数组。

    int[] array1 = Arrays.copyOf(array, array.length);

数组排序：

    Arrays.sort(array); / 优化的快速排序 /

## 多维数组：

申明二维数组：

    double[][] arrays;

用new初始化数组：

    double[][] arrays = new double[m][n];

直接初始化：

    double[][] arrays = {｛...｝，｛...｝, ...}；

访问数组元素：

    for (double[] row : arrays)
        for (double col : row)
            System.out.println(col)

参考java.util.Arrays类。

***

# 字符串(java.lang.String)：

java字符串就是unicode字符序列。

任何一个java对象都可以转换成字符串。

java没有字符串类型，而是用标准库中预定义的类Spring。

每个用双引号""括起来的字符串都是Spring类的一个实例。

不能修改java字符串中的字符，所以String类对象是不可变字符串。

子串:

String类的substring方法可以获取子串

    String greeting = "hello";
    String s = greeting.substring(0, 3);

substring(start, end)，下标从0开始，从start到end，但是不包括end。

拼接:

java可以用+连接两个字符串。

    String expletive = "Expletive";
    String PG13 = "deleted";
    String message = expletive + PG13;

字符串比较:

equals函数比较相等,相等返回true,s和t可以是字符串变量也可以常量:

    s.equals(t)

equalsIgnoreCase函数比较字符串是否相等，不区分大小写：

    s.equalsIgnoreCase(t)

length函数返回字符串长度：

    s.length()

空串：

    if (s.length() == 0)
    if (s.equals(""))

Null:

    if (str == null)

判断一个字符串既不时空串又不是null，先判断是否为null，对null调用方法会出现错误：

    if (str != null && str.length() != 0)

String类的方法:

参考java.lang.String。

## 用StringBuilder构建字符串:

构建一个空字符串构建器:

    StringBuilder builder = new StringBuilder();

修改内容:

    builder.append(String str)
    builder.append(char c)
    builder.delete(int startIndex, int endIndex)
    builder.insert(int offset, String str)
    builder.insert(int offset, Char c)

构建新字符串：

    String completeString = builder.toString();

参考 java.lang.StringBuilder 类的方法。

## 用StringBuffer构建字符串缓冲区

参考 java.lang.StringBuffer 类的方法。

***

# 输入输出：

## 标准输出流：System.out

输出控制流的方法：

    System.out.print();
    System.out.println();

参考 java.io.PrintStream 的方法。

## 标准输入流：System.in

导入Scanner类：

    import java.util.Scanner;

构造Scanner对象，然后和System.in关联：

    Scanner in = new Scanner(System.in);

输入控制流的方法：

    String name = in.nextLine(); / 读取输入的下一行内容 /
    String firstName = in.next(); / 读取输入的下一个单词 /
    int age = in.nextInt(); / 读取一个整数 /
    double number = in.nextDouble(); / 读取一个浮点数 /
    boolean test = in.hasNext(); / 检测输入中是否还有其他单词 /
    boolean test = in.hasNextInt(); / 检测输入中是否还有其他int类型 /
    boolean test = in.hasNextDouble(); / 检测输入中是否还有其他double类型 /

参考 java.util.Scanner 的方法。

## 控制台输入System.console()

返回一个Console类型对象：

    Console cons = System.console();

Console类型对象的方法：

    String username = cons.readLine("User name: ");
    char[] password = cons.readPassword("Password: ");

参考 java.io.Console 的方法。

## 文件输出（读）：

    Scanner in = new Scanner(Paths.get(“myfile.txt”));

## 文件输入（写）：

    PrintWriter out = new PrintWriter(“myfile.txt”));

***

# java控制流

由{}括起来的若干简单语句构成块作用域。

不能在嵌套的两个块中申明同名的变量。

## if条件语句

条件语句if - else if - else:

    if (condition)
    {
        statement；
    }; / if 只有一条语句，{}可以省略 /

    if (condition)
    {
        statement;
    }
    else
    {
        statement;
    }; / else与最近的if构成一组 /

    if(condition)
    {
        statement;
    }
    else if (condition)
    {
        statement;
    }
    else
    {
        expression;
    };

## switch条件语句

条件语句switch-case, variable只能是 byte， short， int，char的常量表达式或枚举常量，也可以是字符串字面量。

default不管在哪里都是最后运行。

从第一个匹配的case开始执行，直到遇到break停止。

编译时加javac -Xlint:fallthrough会给出没有break的警告。

不提倡使用switch-case语句。

    switch (variable)
    {
        case value1:
            statement1;
            break;
        …
        case valueN:
            statementN;
            break;
        default:
            statement;
            break;
    }

## while循环语句

循环语句while,条件为真进入循环。

    while (condition)
    {
        statement;
    }

## do while循环语句

循环语句do – while,先执行一次，再判断条件为真，进入循环。

    do
    {
        statement;
    }
    while (condition)

## for循环语句

循环语句for,init最先执行且只执行一次，condition为真进入循环，执行statement1，然后再执行statement，最后在condition-statement1-statement之间循环。

for循环体内申明和定义的变量不能在外部使用，除非在外部申明和定义。

    for (init; condition; statement) {
        statement1;
    }

## 中断控制流程语句

break语句:

只能用于循环语句，跳出循环，不能用于选择语句。

continue语句：

只能用于循环语句，继续下一次循环，不能用于选择语句。

带标签的break语句：

标签放在希望跳出的最外层循环/选择块 之前， 标签需要紧跟一个冒号。

带标签的break语句可以用于任何语句。

    label:
    {
        ...
        break label;
    }

***

# 文档

java文档采用javadoc风格.

由源文件生成一个html格式的文档。

从下面特性中抽取信息：
1. 包package
2. 公有类与接口
3. 公有的和受保护的构造器及方法
4. 公有的和受保护的域

文档注释方式：

    /**
    * summary, javadoc will automatic detect this line as summary.
    * @param
    * <em>...</em>
    * <code>...</code>
    * <strong>...</strong>
    * <img>...</img>
    * ...
    */

类的注释放在import后面，类定义前面。

方法的注释放到方法前面。

域的注释放到域前面，只需要注释静态常量域。

    package <packageName>;

    import java.util.*;

    /**
     * Class comment
     * @author
     * @version
     * @since
     * @deprecated
     * @see
     * @link
     */
    public Class Comment
    {
        /**
         * Just for public static final field.
         */
        public static final NAME = VALUE;

        /**
         * public Constructor/Method comment
         * @param
         * @return
         * @throws
         */
         public type name(param)
         {
             ...
         }
    }

包注释：

包注释需要在包目录添加单独的文件,有两种方法。

提供一个package.html文件，<body>...</body>之间的会被javadoc提取。

提供一个package-info.java，/**...*/之间的会被javadoc提取。

总注释：

可以为所有源文件提供一个总结性的注释：

提供一个overview.html文件，在<body>...</body>之间的会被javadoc提取。

***

# 打包

## jar文件

用jar命令打包， 可以包含图像，声音，源代码等文件，并进行压缩。

    jar cvf JarFile.jar File1 File2 ... # 将指定文件压缩归档到JarFileName这个jar包。
    jar cvfm JareFile.jar manifest.mf File ... # 根据清单文件mainfest.mf压缩归档。
    jar uvfm JarFile.jar mainfest-additions.mf # 更新已有jar包。

运行jar包：

    java -jar JarFile.jar

## Java Web Start

jws是一项通过internet发布应用程序的技术。

JWS程序需要打包一个或多个jar文件，然后创建一个JNLP格式的描述符文件，将这些文件放到web服务器。

JWS特性：
1. 通过浏览器发布，下载到本地就可以启动，不再需要浏览器。
2. 应用程序不在浏览器窗口内，显示在浏览器外的一个属于自己的框架中。
3. 应用程序不使用浏览器的java实现，浏览器只是在加载应用程序描述符时启动一个外部应用程序。
4. 数字签名用用程序可以被赋予访问本地机器的任意权限，未签名的应用程序只能在沙箱中运行。

## applet

applet是一种包含在html网页中的java应用程序。

