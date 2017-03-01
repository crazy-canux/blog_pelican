---
layout: post
title: C语言之POSIX
comments: true
date: 2016-04-02 11:18:05
updated:
tags:
- C
- ISO C
- ANSI C
- POSIX
categories:
- C
permalink:
---

# POSIX标准

Portable Operating System Interface

可移植性操作系统接口, POSIX兼容ISO C。

所有Unix都遵循，几乎所有Linux都遵循，Windows部分支持。

POSIX.1/IEEE 1003.1-1990

POSIX.2/IEEE Std 1003.2-1992/ISO IEC 9945-2:1993)

POSIX.1.b/IEEE Std 1003.1b-1993/ISO IEC 9945-1:1996)

POSIX.1.c/IEEE Std 1003.1c-1995

POSIX.1.d/IEEE  Std  1003.1c-1999

POSIX.1.g/IEEE Std 1003.1g-2000

POSIX.1.j/IEEE  Std  1003.1j-2000

POSIX.1-2001/SUSv3(包括了所有C99的API)

POSIX.1-2008/SUSv4

官方网站：

<http://www.opengroup.org/austin/>

# Cygwin

提供POSIX的API用于windows上开发Linux/Unix程序。

源代码不能在windows运行。

<https://cygwin.com/index.html>

***

# POSIX标准定义的必须头文件

## <dirent.h>

## <fcntl.h>

## <glob.h>

## <netdb.h>

## <pwd.h>

## <regex.h>

## <tar.h>

## <termios.h>

## <unistd.h>

## <utime.h>

## <utime.h>

## <wordexp.h>

## <arpa/inet.h>

## <net/if.h>

## <netinet/in.h>

## <netinet/tcp.h>

## <sys/mman.h>

## <sys/select.h>

## <sys/socket.h>

## <sys/stat.h>

## <sys/times.h>

## <sys/types.h>

## <sys/un.h>

## <sys/utsname.h>

## <wait.h>

***

# POSIX标准定义的可选头文件

## <aio.h>

## <pthread.h>

## <semaphore.h>

## <mqueue.h>

## <sched.h>

## <spawn.h>

## <strops.h>

## <trace.h>

***

# POSIX标准定义的XSI扩展头文件

## <sys/ipc.h>

## <sys/msg.h>

## <sys/sem.h>

## <sys/shm.h>

## <cpio.h>

## <dlfcn.h>

## <fmtmsg.h>

## <ftw.h>

## <iconv.h>

## <langinfo.h>

## <libgen.h>

## <monetary.h>

## <ndbm.h>

## <nl_types.h>

## <poll.h>

## <search.h>

## <strings.h>

## <syslog.h>

## <ucontext.h>

## <ulimit.h>

## <utmpx.h>

## <sys/resource.h>

## <sys/statvfs.h>

## <sys/time.h>

## <sys/timeb.h>

## <sys/uio.h>

