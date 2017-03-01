---
layout: post
title: C总结
comments: true
date: 2016-04-02 16:06:14
updated:
tags:
- C
- Linux
- Unix
- Windows
- POSIX
- ISO C
- ANSI C
categories:
- C
permalink:
---

# C标准

ISO C89(ANSI C89) -> ISO C99 -> ISO C11

ANSI C 和 ISO C是对通用C语言的接口的定义。

符合这种标准的实现为C语言标准库,也叫libc。

Unix/Linux的POSIX包含libc。

Linux的glibc包含libc。

Windows的msvcrt包含libc。

其它和C相关的标准：

BSD

System V

XPG

SUS

# Linux的标准C库glibc：

遵循ISO C11 和 POSIX.1-2008。

还包括一些其它标准。

关于ISO C 和 POSIX参考另外两篇博文。

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
