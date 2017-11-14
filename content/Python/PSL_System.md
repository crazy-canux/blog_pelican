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
    listdir(path)
    makedirs(path [, mode=0777])
    mkdir(path [, mode=0777])
    walk(top, topdown=True, onerror=None, followlinks=False) # 返回 (dirpath, dirnames, filenames) 类型的迭代器
    remove(path) # remove a file
    rmdir(path) # remove a directory
    removedirs(path)
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

    clock()
    sleep(seconds) # 延迟
    tzset()

    # 获取时间戳(Epoch seconds)
    time() # 获取当前时间戳
    mktime(tuple) # mktime((2017,8,23,11,7,10,12)) , 参数是时间元组

    # 获取时间元组 (tm_year,tm_mon,tm_mday,tm_hour,tm_min, tm_sec,tm_wday,tm_yday,tm_isdst)
    localtime([seconds]) # 参数是时间戳
    gmtime([seconds]) # 参数是时间戳
    strptime(string, format) # 参数是时间字符串

    # 获取时间字符串
    asctime([tuple])
    strftime(format[, tuple])
    ctime(seconds) # 参数是时间戳

data:

## logging

    import logging

classes:

    Logger(Filterer)
    # methods:
    setLevel(self, level) # 只会输出指定level以上的log, 默认是WARNING
    critical(self, msg, *args, **kwargs) # 50
    error(self, msg, *args, **kwargs) # 40
    warning(self, msg, *args, **kwargs) # 30
    info(self, msg, *args, **kwargs) # 20
    debug(self, msg, *args, **kwargs) # 10
    exception(self, msg, *args, **kwargs) #
    log(self, level, msg, *args, **kwargs) #
    addHandler(self, hdlr) # 添加handler到logger

    Formatter
    %(asctime)s

    Handler(Filterer)
    # methods:
    setFormatter(self, fmt)
    setLevel(self, level)

    StreamHandler(Handler) # 默认打印到sys.stderr

    FileHandler(StreamHandler) # 打印到文件

functions:

    basicConfig(**kwargs) # 设置log的格式，默认是BASIC_FORMAT.
    # filename/filemode/format/datefmt/level/stream
    # stream默认是sy.stderr,当filename和stream同时指定，stream被忽略．
    getLogger(name=None) # 返回Logger类型对象

data:

    BASIC_FORMAT = '%(levelname)s:%(name)s:%(message)s'
    CRITICAL = 50
    FATAL = 50
    ERROR = 40
    WARN = 30
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

## getopt

C风格的参数处理.

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

    # HelpFormatter

    # Action

functions:

data:

## io

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
    Process(group=None, target=None, name=None, args=(), kwargs={})
    # methods:
    run(self)
    start(self)
    join(self, timeout=None)
    is_alive()
    terminate(self)
    # data descriptor:
    authkey
    daemon
    exitcode
    ident
    name
    pid

functions:

    # 工厂函数

    Manager()

    Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)

    # IPC: 管道

    Pipe(duplex=True) # duplex=True表示默认是双向pipe.
    receiver, sender = Pipe()
    sender.send(obj)
    receiver.recv()
    close()

    # IPC: 消息队列

    # 来自于Queue.Queue, 具体方法参考Queue.Queue
    Queue(maxsize=0) # return a queue object
    q = Queue()

    # IPC: 共享内存
    Array(typecode_or_type, size_or_initializer, **kwds)
    RawArray(typecode_or_type, size_or_initializer)
    Value(typecode_or_type, *args, **kwds)
    RawValue(typecode_or_type, *args)

    Event()
    Semaphore(value=1)
    BoundedSemaphore(value=1)
    Lock()
    RLock()
    Condition(lock=None)

    # 普通函数

    active_children()
    allow_connection_pickling()
    cpu_count()
    current_process()
    freeze_support()
    get_logger()
    log_to_stderr(level=None)

data:

    SUBDEBUG = 5
    SUBWARNING = 25

## thread

实现了基本的线程操作，推荐使用更高级的threading替代该模块．

functions:

    start_new_thread(function, args[, kwargs]) # 启动新线程，执行function(*args, **kwargs), 函数返回时线程退出．
    stack_size([size])
    interrupt_main()
    get_ident()
    exit()
    allocate_lock()

## threading

threading支持守护线程(通过join方法实现)．

    import threading

classes:

    # threading.Thread
    Thread(group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
    # methods:
    run(self) # 子类重写用来定义线程的功能的函数, 通常通过这种方式来创建线程
    start(self) # 开始执行线程
    join(self, timeout=None) # 主程序挂起，直到线程结束,再继续运行主程序
    getName(self) # 返回线程名字
    setName(self, name) # 设置线程名字
    isAlive(self) # 表示线程是否还在运行的boolean
    isDaemon(self) # 返回线程的daemon标志
    setDaemon(self, daemonic) # 在调用start方法前把daemon标志设为daemonic

functions:

    # 工厂函数：

    Timer(*args, **kwargs)
    t = Timer(30.0, f, args=[], kwargs={})
    t.start() # 在一个子线程等待，timeout就执行f(*args, **kwaargs).
    t.cancel() # 如果还在等待就取消．

    Event(*args, **kwargs)
    BoundedSemaphore(*args, **kwargs)
    Semaphore(*args, **kwargs)
    Condition(*args, **kwargs)
    Lock = allocate_lock(...)
    RLock(*args, **kwargs)

    # 普通函数：

    activeCount() # 当前活动的线程对象的数量
    currentThread() # 返回当前线程对象
    enumerate() # 返回当前活动线程列表
    settrace(func) # 为所有的线程设置一个跟踪函数
    setprofile(func) # 为所有线程设置一个profile函数
    stack_size()

## select

## mmap

## dummy_thread

## dummy_threading

## readline

## rlcompleter

***

# TPL

## Click

<https://github.com/pallets/click>

## Pexpect

<https://github.com/pexpect/pexpect>
