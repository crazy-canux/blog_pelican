Title: Summary
Date: 2016-04-02 16:06:14
Tags: C, Summary



# C标准

ISO C89(ANSI C89) -> ISO C99 -> ISO C11

ANSI C 和 ISO C是对通用C语言的接口的定义。

符合这种标准的实现为C语言标准库,也叫libc。

Unix/Linux的POSIX包含libc。

Linux的glibc包含libc及其扩展.

Windows的msvcrt包含libc及其扩展.

其它和C相关的标准：

BSD

System V

XPG

SUS

# glibc

Linux的标准C库glibc

遵循ISO C11 和 POSIX.1-2008, 还包括一些其它标准。

关于ISO C 和 POSIX参考另外两篇博文。

# msvcrt

windows的标准c库msvcrt.

***

# C注释

单行注释：

    // comment

    /* comment */

多行注释：

    /*
     * comment1
     * commenet2
     */

# 文档

C程序可以用doxygen从程序中提取文档。

文档注释：

    /**
     * @file
     * @brief
     * @author
     * @date
     * @version
     * @copyright
     */

# 编译和链接

编译只检查语法错误和函数以及变量是否申明．将*.c源文件编译成*.o目标文件．

    gcc -g -Wall -I/head/file/path -c -o helloworld.o helloworld.c

链接检查函数和变量的定义．将*.o目标文件链接之后生成可执行文件，或者打包成库文件*.a或*.so.

    # normal
    gcc -g -Wall -o helloworld helloworld.o
    # static library *.a
    gcc -g -Wall -o libstatic.a helloworld.o -L/static/lib/path -lstatic
    # dynamic library *.o
    gcc -g -Wall -o libdynamic.so helloworld.o -L/dynamic/lib/path -ldynamic -Wl, -rpath=/dynamic/lib/path
