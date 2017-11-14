Title: SSH
Date: 2016-07-28 15:53:34
Tags: Network, SSH



# OpenSSH

<http://www.openssh.com/>

windows上支持ssh协议的客户端：

* putty
* xshell
* MobaXterm
* secureCRT

安装：

    $ sudo apt-get install openssh-server

***

# SSH命令

ssh是openssh协议的客户端．

远程操作的命令包括ssh, scp, sftp.

ssh

    $ ssh

scp

    $ scp

sftp

    $ sftp

常用选项：

    -o StrictHostKeyChecking=no

ssh也包括一些密钥管理的命令.

ssh-keygen

    $ ssh-keygen -t rsa -C 'canuxcheng@gmail.com'

    # 通过将本机的公钥拷贝到远程机器实现无密码访问．
    # 将本机的public-key拷贝到远程机器的authorized_keys.
    $ ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote
    # 另外的拷贝方法
    $ ssh user@host "cat >> ~/.ssh/authorized_keys" < ~/.ssh/id_rsa.pub
    $ sudo service ssh restart # 需要重启ssh服务

    非交互式通过命令行传密码的命令：
    $ sshpass -p [password]

ssh-add

ssh-keysign

ssh-keyscan

***

# python的第三方库

## paramiko

<https://github.com/paramiko/paramiko/>

paramiko依赖pycrypto

    $pip install paramiko

    import paramiko

    # SSHClient
    client = paramiko.SSHClient()
    # methods:
    load_system_host_keys(filename=None)
    load_host_keys(filename)
    get_host_keys()
    set_missing_host_key_policy(policy)
    # paramiko.client.AutoAddPolicy()
    # paramiko.client.RejectPolicy()
    # paramiko.client.WarningPolicy()
    save_host_keys(self, filename)
    connect(hostname, port=22, username=None, password=None, pkey=None, key_filename=None, timeout=None, allow_agent=True, look_for_keys=True, compress=False, sock=None)
    # 查找Authentication顺序：
    # 1. pkey or key_filename
    # 2. allow_agent
    # 3. look_for_keys
    # 4. username/password
    stdin, stdout, stderr = exec_command(command, bufsize=-1, timeout=None, get_pty=False) # 返回三个ChannelFile类型的对象
    # stdin -> paramiko.ChannelFile
    # output = stdout.readlines() -> list
    # error = stderr.readlines() -> list
    invoke_shell(self, term='vt100', width=80, height=24, width_pixels=0, height_pixels=0)
    open_sftp(self)
    set_log_channel(self, name)
    get_transport() # return a transport
    close(self)

    # Transport
    connect(self, hostkey=None, username='', password=None, pkey=None)
    cancel_port_forward(self, address, port)
    close(self)
    open_channel(self, kind, dest_addr=None, src_addr=None)  # Request a new channel to the server
    open_session(self) # alias of open_channel
    run(self)
    send_ignore(self, bytes=None)
    start_client(self, event=None)
    start_server(self, event=None, server=None)
    stop_thread(self)
    use_compression(self, compress=True)

    # Channel
    close()
    exec_command(command)
    exit_status_ready(self)
    invoke_shell(self)
    invoke_subsystem(self, subsystem)
    makefile(self, *params)
    makefile_stderr(self, *params)
    recv(self, nbytes)
    recv_exit_status(self)
    recv_ready(self)
    recv_stderr(self, nbytes)
    recv_stderr_ready(self)
    send(self, s)
    send_exit_status(self, status)
    send_ready(self)
    send_stderr(self, s)
    sendall(self, s)
    sendall_stderr(self, s)
    settimeout(self, timeout)
    shutdown(self, how)
    shutdown_read(self)
    shutdown_write(self)

    # ChannelFile(BufferedFile)
    read(size=None) # 读size字节，默认整个文件
    readline(size=None) # 读下一行
    readlines(sizehint=None) # 读所有行，返回list
    write(data)
    writelines(sequence)
    close()

***

# Java

