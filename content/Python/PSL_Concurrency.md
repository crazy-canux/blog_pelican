Title: PSL_Concurrency
Date: 2016-08-15 11:04:12
Tags: Python, Concurrency



# Concurrent Execution

进程：每个进程都有自己的地址空间，内存，数据栈以及其它记录其运行轨迹的辅助数据

线程：线程（有时被称为轻量级进程）跟进程有些相似，不同的是，所有的线程运行在同一个进程中，共享相同的运行环境

IPC: 进程/线程之间交换信息叫进程间通信．

python的多线程由于GIL只有并发没有并行，无论有多少cpu,一次只能有一个python解释器(线程)执行.一次只能执行一个线程.一次只能用到一个逻辑cpu.

IO密集型任务消耗IO,但是不消耗CPU,cpu切换消耗少,适合用多线程.

python的多进程可以并行,每个进程启动一个解释器进程.

多进程开销大，消耗内存.

计算密集型消耗cpu,任务个数不超过cpu个数．适合用多进程，把每个cpu跑满.

## multiprocessing

多进程就是同时执行多个任务.

python可以通过多进程取代多线程，从而绕过多线程的GIL.

python是静态语言，

    import multiprocessing

classes:

    # multiprocessing.Process
    proc = Process(group=None, target=None, name=None, args=(), kwargs={})
    # methods:
    run(self)
    start(self) # 启动一个进程
    join(self, timeout=None) # 父进程等待子进程结束
    is_alive()
    terminate(self)
    # data descriptor:
    authkey
    daemon # proc.daemon = True 后台运行
    exitcode
    ident
    name
    pid

functions:

    # 普通函数
    active_children()
    allow_connection_pickling()
    cpu_count() # 获取cpu个数
    current_process()
    freeze_support()
    get_logger()
    log_to_stderr(level=None)

    Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)
    pool = Pool()
    # func只能是顶层函数，不能是方法和内部函数.
    # 进程池，可以控制进程数量,processes 默认是cpu个数(cpu_count())
    # 非阻塞，维持进程总数，当一个进程结束会添加新的进程到pool,主进程不阻塞，同步运行，pool中的进程并发执行.
    apply_async(func, args=(), kwargs={}, callback=None) # 非阻塞,
    map_async(func, iterable, chunksize=None, callback=None) # 非阻塞
    # 阻塞，维持进程总数，当一个进程结束会添加新的进程到pool，主进程阻塞，pool中的进程一个一个执行.
    apply(func, args=(), kwargs={}) # 阻塞
    map(func, itreable, chunksize=None) # 阻塞
    terminate() # 终止所有任务
    close() # 关闭pool,不接受新任务
    join() # 等待pool中子进程结束，要在close/terminate之后调用.

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
    Manager()

    Array(typecode_or_type, size_or_initializer, **kwds)

    RawArray(typecode_or_type, size_or_initializer)

    Value(typecode_or_type, *args, **kwds)

    RawValue(typecode_or_type, *args)

    Event()

    # 同步：　条件变量
    Condition(lock=None)

    # 同步：信号量
    Semaphore(value=1)

    # 同步：有界信号量
    BoundedSemaphore(value=1)

    # 同步： 锁
    Lock()

    # 同步: 锁
    RLock()

data:

    SUBDEBUG = 5
    SUBWARNING = 25

## threading

多线程就是把单个任务分成不同部分运行.

threading支持守护线程(通过join方法实现)．

    import threading

classes:

    # threading.Thread
    t = Thread(group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
    threads.append(t)
    # methods:
    run(self) # 子类重写用来定义线程的功能的函数, 通常通过这种方式来创建线程
    start(self) # 开始执行线程
    join(self, timeout=None) # 主程序挂起，直到线程结束,再继续运行主程序
    is_alive(self) # 表示线程是否还在运行的boolean
    getName(self) # 返回线程名字
    setName(self, name) # 设置线程名字
    isDaemon(self) # 返回线程的daemon标志
    setDaemon(self, daemonic) # daemonic=True 使线程在后台运行

functions:

    active_count() # 当前活动的线程对象的数量
    current_thread() # 返回当前线程对象
    enumerate() # 返回当前活动线程列表
    settrace(func) # 为所有的线程设置一个跟踪函数
    setprofile(func) # 为所有线程设置一个profile函数
    stack_size()

    Timer(*args, **kwargs)
    t = Timer(30.0, f, args=[], kwargs={})
    t.start() # 在一个子线程等待，timeout就执行f(*args, **kwaargs).
    t.cancel() # 如果还在等待就取消．

    Event(*args, **kwargs)

    # 同步：　条件变量
    Condition(*args, **kwargs)

    # 同步：　信号量
    Semaphore(value=1, *args, **kwargs)
    # 信号量，默认value=1, 内部计数器不能小于0,当计数器==0时，调用acquire会阻塞.

    # 同步：　有界信号量
    BoundedSemaphore(value=1, *args, **kwargs)
    # 有界信号量，默认value=1，内部计数器不能小于0，并且不能大于value。
    # 当计数器==0，调用acquire会阻塞，当>value抛出VAlueError异常
    # 可用来控制并发运行的线程数量
    bs = BoundSemaphore(number) # bs是全局的.
    def thread_function(*args, **kwargs):
        ...
        bs.release() # 使计数器+1
    for t in threads:
        bs.acquire() # 使计数器-1
        thread.start()
    for t in threads:
        t.join()

    # 同步：　锁
    Lock()
    # 使同一变量在多个线程间同步
    lock = Lock()
    variable = value
    def thread_function(*args, **kwargs):
        global lock
        global variable
        lock.acquire() # 加锁，使线程进入同步阻塞状态
        variable = new_value
        lock.release() # 释放锁

    # 同步：　锁
    RLock(*args, **kwargs)

## subprocess

开启一个子进程来执行外部命令.

    import subprocess

classes:

    Popen(args,
    bufsize=0, executable=None, stdin=None, stdout=None, stderr=None,
    preexec_fn=None, close_fds=False, shell=False,cwd=None,
    env=None, universal_newlines=False,startupinfo=None, creationflags=0)
    # p = Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 如果命令和参数是字符串形式，需要参数shell=True
    # p = Popen(command_string, shell=True, ...)

    # 非交互执行sudo命令, 或者使用sh/pexpect等第三方库
    Popen(['sudo', '-S'] + shlex.split(command), stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, ...)
    stdout, stderr = child.communicate(password+'\n')

    # methods:
    poll() # 检查子进程是否结束，返回returncode.
    wait() # 等待子进程结束，返回returncode.
    communicate(input=None) # 返回(stdout, stderr).
    kill() # 发送SIGKILL信号
    pipe_cloexec()
    send_signal(sig)
    terminate()

    # Data:
    stdin
    stdout
    stderr
    pid
    returncode

functions:

    call(*popenargs, **kwargs)
    # retcode = call(["ls", "-l"])

    check_call(*popenargs, **kwargs)
    # check_call(["ls", "-l"]) -> 如果返回码为０就返回，否则抛出CalledProcessError.

    check_output(*popenargs, **kwargs) # 返回一个字符串
    # output = check_output(["ls", "-l", "/dev/null"]) -> 如果返回码为０返回命令结果，否则抛出CalledProcessError.

data:

    PIPE = -1
    STDOUT = -2

## socket

socket协议的标准库

    import socket

classes:

    # socket = class _socketobject(__builtin__.object)
    # socket.socket([family[, type[, proto]]])
    close() # 关闭socket
    shutdown(flag) # 0 关闭读，１关闭写，２全部关闭
    # eg: socket.socket(AF_INET, SOCK_STREAM, 0) ipv4+tcp
    # eg: socket.socket(AF_INET, SOCK_DGRAM, 0) ipv4+udp

    # methods:
    bind(address) # 服务器绑定(host, port)到socket
    listen(backlog) # 服务器开始监听tcp
    accept() # 服务器阻塞等待客户的tcp连接, 返回(socket object, address info)

    connect(address) # 客户端主动初始化tcp连接,连接失败抛出异常
    connect_ex(address) # 同上，连接失败返回errno

    send(data[, flags]) # 发送tcp数据
    sendall(data[, flags]) # 发送完整tcp数据
    recv(buflen[, flags]) # 接收tcp数据
    recv_into(buffer[, nbytes[, flags]])

    sendto(data[, flags], addr) # 发送udp数据
    recvfrom(buflen[, flags]) # 接收udp数据
    recvfrom_into(buffer[, nbytes, [, flags])])

    getpeername() # 获取当前socket的远端地址
    getsockname() # 获取当前socket的地址
    getsockopt(level, option[, buffersize]) # 获取socket参数
    setsockopt(level, option, value) # 设置socket参数

    setblocking(flag)
    gettimeout()
    settimeout(timeout)

    makefile([mode[, bufsize]])
    fileno()

    dup()

    # data descriptor:
    family/type/proto　参考man 2 socket
    recv
    recv_into
    recvfrom
    recvfrom_into
    send
    sendto

functions:

    create_connection(address, timeout=<object object>, source_address=None)
    fromfd(fd, family, type[, proto]) # 用一个已经打开的文件描述符创建一个socket对象
    getaddrinfo(host, port [, family, socktype, proto, flags])
    getdefaulttimeout()
    getfqdn(name='') # FQDN, 获取完整域的信息
    gethostbyaddr(host) -> (name, aliaslist, addresslist)
    gethostbyname(host)
    gethostbyname_ex(host) -> (name, aliaslist, addresslist)
    gethostname()
    getnameinfo(sockaddr, flags) --> (host, port)
    getprotobyname(name)
    getservbyname(servicename[, protocolname])
    getservbyport(port[, protocolname])
    htonl(integer)
    htons(integer)
    inet_aton(string)
    inet_ntoa(packed_ip)
    inet_ntop(af, packed_ip)
    inet_pton(af, ip)
    ntohl(integer)
    ntohs(integer)
    setdefaulttimeout(timeout)
    socketpair([family[, type[, proto]]]) -> (socket object, socket object)

## asynchat

## asyncore

## ssl

## signal

## select

## mmap

## dummy_thread

## dummy_threading

***
