Title: PSL_Socket&IPC
Date: 2016-08-12 15:33:29
Tags: Python, IPC, Socket



# Interprocess Communication and Networking

## subprocess

    import subprocess

classes:

    Popen(args,
    bufsize=0, executable=None, stdin=None, stdout=None, stderr=None,
    preexec_fn=None, close_fds=False, shell=False,cwd=None,
    env=None, universal_newlines=False,startupinfo=None, creationflags=0)
    # p = Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

    check_output(*popenargs, **kwargs)
    # output = check_output(["ls", "-l", "/dev/null"]) -> 如果返回码为０返回命令结果，否则抛出CalledProcessError.

data:

    PIPE = -1
    STDOUT = -2

## asynchat

## asyncore

## SocketServer

python2叫SocketServer,python3改名为socketserver.

用于简化实现网络客户端和服务器的大量样板代码。

## socket

## ssl

## signal

***

# TPL

相关的第三方库

## sh

<https://github.com/amoffat/sh>

    $pip install sh

    import sh
