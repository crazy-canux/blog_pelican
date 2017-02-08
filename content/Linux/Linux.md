---
layout: post
title: Linux
comments: true
date: 2016-03-31 21:48:59
updated:
tags:
- Linux
categories:
- Linux
permalink:
---

# Linux

Linux严格讲指的是Linux这一类操作系统的内核。

Linux内核的github：

<https://github.com/torvalds/linux>

Linux内核的站点：

<https://www.kernel.org/>

商业化的linux系统：
1. redhat enterprise linux
2. suse enterprise linux

免费的服务器版本：
1. centos (rhel的免费版服务器版)
2. open suse
3. debian/ubuntu

免费的桌面版本：
1. fedora (原来的redhat desktop linux)
2. open suse
3. debian/ubuntu

# Linux桌面环境

X windows

KDE

GNOME2(Mate)

GNOME3(Mate/Cinnamon)

Unity

xface

lxde

enlightenment(https://www.enlightenment.org/start)

# Linux桌面管理器：

xDM

gDM(gnome)

kDM(kde)

lightDM

# Linux的shell

查看shell内置命令：

    help [command]

查看shell的外部命令(包括应用程序的命令行)

    man [command]
    man 1 [command]
    info [command]

查到包括宏，包，惯用法等

    man 7 <name>

查到系统管理员命令

    man 8 <name>

查到内核的惯用法

    man 9 <name>

# Linux编程

## Linux程序调用结构：

1. 应用程序(包括shell外部命令)/Shell命令(也就是shell内部命令)
2. C标准库glibc(包括ISO C和POSIC封装的系统系统调用)
3. Linux系统调用
4. Linux内核

## 查看手册：

通过CONFORMING TO可以看到函数遵循什么标准。

查到的是系统调用（实际上也是POSIX封装的同名函数）

    man 2 <name>

查到的glibc（包括ISO C，POSIX的部分函数，其它库）

    man 3 <name>

查看系统调用所有函数宏

    man syscalls

查看未实现的系统调用

    man unimplemented

查看glibc

    man libc

查看C和Linux的标准

    man standards

# Grub

引导程序。

windows的引导程序是NTloader。

linux/unix的引导程序有lilo和grub。
