Title: PSL_Socket
Date: 2016-08-12 15:33:29
Tags: Python, Socket



# Interprocess Communication and Networking

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

    # 非交互执行sudo命令, 或者使用pexpect
    Popen(['sudo', '-S'] + shlex.split(command), universal_newlines=True, ...)
    child.communicate(password+'\n')

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

## SocketServer

python2叫SocketServer,python3改名为socketserver.

一般的socket server的类, client可以通过socket来实现．

    import SocketServer

classes:

    BaseRequestHandler(self, request, client_address, server)

    BaseServer

    StreamRequestHandler(BaseRequestHandler)
    self.rfile
    self.wfile
    # methods:
    handle(self) # 子类重写该方法
    finish(self)
    setup(self)

    TCPServer(BaseServer)
    TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
    # methods:
    serve_forever(poll_interval=0.5)
    shutdown()
    handle_request()
    fileno()
    ...
    # Instance variables:
    server_address
    RequestHandlerClass
    socket
    # Class variables:
    timeout
    ...

    DatagramRequestHandler(BaseRequestHandler)
    self.request
    self.client_address
    self.server
    # methods:
    handle(self) # 子类重写该方法
    finish(self)
    setup(self)

    UDPServer(TCPServer)
    UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
    # methods:
    serve_forever(self, poll_interval=0.5)

## asynchat

## asyncore

## ssl

## signal

***

# TPL

相关的第三方库

## sh

<https://github.com/amoffat/sh>

    $ pip install sh

    import sh
