Title: PSL_System
Date: 2016-08-15 11:04:12
Tags: Python, System



# Generic Operating System Services

## os

    import os

    os.path # 参考PSL_File
    os.name
    os.curdir
    os.pardir # 表示上一级路径
    os.sep
    os.extsep
    os.altsep
    os.pathsep
    os.linesep
    os.defpath
    os.devnull

classes:

functions:

    WCOREDUMP(...)
    ...
    abort(...)
    fork() # 创建一个子进程，返回0给子进程，返回子进程pid给父进程．
    exec*
    wait() # 等待子进程结束，返回(pid, status).
    waitpid(pid, options) # 等待指定子进程结束.
    ...

    # 使用subprocess模块代替下列函数：
    system(command) # 在subshell执行命令，返回退出码(windows系统始终为0),而非命令执行结果．
    spawn*
    popen*(command [, mode='r' [, bufsize]]) # 执行命令，返回命令执行结果的文件句柄(file对象)

data:

    EX_CANTCREAT = 73
    ...

## time

    import time

classes:

functions:

    # 获取当前unix时间戳
    time.time()

    # 将时间2011-09-27 10:50:00转换成时间戳（从1970开始的秒数）
    time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))

    # 将时间戳转换成时间2011-09-27 10:50:00
    time.gmtime(1472540718.340721)

    time.sleep(seconds) # 延迟

data:

## io

## logging

    import logging

## getopt

## argparse

    import argparse

classes:

    # argparse.ArgumentParser(_AttributeHolder, _ActionsContainer)
    parser = argparse.ArgumentParser()
        prog -- The name of the program (default: sys.argv[0])
        usage -- A usage message (default: auto-generated from arguments)
        description -- A description of what the program does
        epilog -- Text following the argument descriptions
        parents -- Parsers whose arguments should be copied into this one
        formatter_class -- HelpFormatter class for printing help messages
        prefix_chars -- Characters that prefix optional arguments
        fromfile_prefix_chars -- Characters that prefix files  containing additional arguments
        argument_default -- The default value for all arguments
        conflict_handler -- String indicating how to handle conflicts
        add_help -- Add a -h/-help option
    # methods:
    add_argument_group(self, *args, **kwargs) # -> argparse._ArgumentGroup
    add_argument(self, *args, **kwargs)
        name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
        action - The basic type of action to be taken when this argument is encountered at the command line.
        nargs - The number of command-line arguments that should be consumed.
        const - A constant value required by some action and nargs selections.
        default - The value produced if the argument is absent from the command line.
        type - The type to which the command-line argument should be converted.
        choices - A container of the allowable values for the argument.
        required - Whether or not the command-line option may be omitted (optionals only).
        help - A brief description of what the argument does.
        metavar - A name for the argument in usage messages.
        dest - The name of the attribute to be added to the object returned by.
    add_subparsers(self, **kwargs) # -> argparse._SubParsersAction
    add_mutually_exclusive_group(self, **kwargs)
    set_defaults(self, **kwargs)
    parse_args(self, args=None, namespace=None) # -> argparse.Namespace
    parse_known_args(self, args=None, namespace=None) # -> argparse.Namespace
    convert_arg_line_to_args(self, arg_line)
    error(self, message)
    exit(self, status=0, message=None)
    format_help(self)
    format_usage(self)
    format_version(self)
    print_help(self, file=None)
    print_usage(self, file=None)
    print_version(self, file=None)
    get_default(self, dest)
    register(self, registry_name, value, object)

    # argparse._ArgumentGroup
    # methods:
    add_argument(self, *args, **kwargs)
    add_argument_group(self, *args, **kwargs)
    add_mutually_exclusive_group(self, **kwargs)
    get_default(self, dest)
    register(self, registry_name, value, object)
    set_defaults(self, **kwargs)

    # argparse._SubParsersAction
    # methods:
    add_parser(self, name, **kwargs) # -> argparse.ArgumentParser

functions:

data:

## errno

## getpass

## curses

<https://github.com/crazy-canux/python/blob/master/python/psl/mycurses.py>

    import curses

## platform

## ctypes

    import ctypes

***

# Optional Operating System Services

进程：每个进程都有自己的地址空间，内存，数据栈以及其它记录其运行轨迹的辅助数据

IPC: 进程之间交换信息叫进程间通信．

线程：线程（有时被称为轻量级进程）跟进程有些相似，不同的是，所有的线程运行在同一个进程中，共享相同的运行环境

## multiprocessing

python可以通过多进程取代多线程，从而绕过GIL.

    import multiprocessing

classes:

    # multiprocessing.Process

functions:

    Queue(maxsize=0) # return a queue object.

data:

    SUBDEBUG = 5
    SUBWARNING = 25

## thread

实现了基本的线程操作，推荐使用更高级的threading替代该模块．

## threading

    import threading

classes:

    # threading.Thread
    Thread(group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
    # methods:
    getName(self)
    setName(self, name)
    isAlive(self)
    isDaemon(self)
    setDaemon(self, daemonic)
    start(self)
    run(self)
    join(self, timeout=None)

functions:

    # 工厂函数：

    Timer(*args, **kwargs)
    t = Timer(30.0, f, args=[], kwargs={})
    t.start() # 在一个子线程等待，timeout就执行f(*args, **kwaargs).
    t.cancel() # 如果还在等待就取消．

    # 普通函数：

    activeCount()

## dummy_thread

## dummy_threading

## readline

## rlcompleter

## select

## mmap

***

# TPL

## Click

<https://github.com/pallets/click>

## Pexpect

<https://github.com/pexpect/pexpect>
