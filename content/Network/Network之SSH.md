---
layout: post
title: Network之SSH
comments: true
date: 2016-07-28 15:53:34
updated:
tags:
- ssh
categories:
- Network
permalink:
---

# OpenSSH

<http://www.openssh.com/>

# python

## paramiko

<https://github.com/paramiko/paramiko/>

paramiko依赖pycrypto

<https://github.com/dlitz/pycrypto>

    pip install cryptography
    pip install paramiko

    import paramiko

    # client
    client = paramiko.SSHClient()
    load_system_host_keys(filename=None)
    load_host_keys(filename)
    get_host_keys()
    set_missing_host_key_policy(policy)
    # 允许连接不在know_hosts文件中的主机
    set_missing_host_key_policy(paramiko.AutoAddPolicy())
    save_host_keys(self, filename)
    connect(hostname, port=22, username=None, password=None, pkey=None, key_filename=None, timeout=None, allow_agent=True, look_for_keys=True, compress=False, sock=None)
    # 查找Authentication顺序：
    # 1. pkey or key_filename
    # 2. allow_agent
    # 3. look_for_keys
    # 4. username/password
    stdin, stdout, stderr = exec_command(command, bufsize=-1, timeout=None, get_pty=False)
    # stdin -> paramiko.ChannelFile
    # output = stdout.readlines() -> list
    # error = stderr.readlines() -> list
    invoke_shell(self, term='vt100', width=80, height=24, width_pixels=0, height_pixels=0)
    open_sftp(self)
    set_log_channel(self, name)
    get_transport() # return a transport
    close(self)

    # transport
    accept(self, timeout=None)
    add_server_key(self, key)
    atfork(self)
    auth_interactive(self, username, handler, submethods='')
    auth_none(self, username)
    auth_password(self, username, password, event=None, fallback=True)
    auth_publickey(self, username, key, event=None)
    cancel_port_forward(self, address, port)
    close(self)
    connect(self, hostkey=None, username='', password=None, pkey=None)
    get_exception(self)
    get_hexdump(self)
    get_log_channel(self)
    get_remote_server_key(self)
    get_security_options(self)
    get_server_key(self)
    get_username(self)
    getpeername(self)
    global_request(self, kind, data=None, wait=True)
    is_active(self)
    is_authenticated(self)
    open_channel(self, kind, dest_addr=None, src_addr=None)  # Request a new channel to the server
    open_session(self) # alias of open_channel
    open_forward_agent_channel(self)
    open_forwarded_tcpip_channel(self, (src_addr, src_port), (dest_addr, dest_port))
    open_sftp_client(self)
    open_x11_channel(self, src_addr=None)
    renegotiate_keys(self)
    request_port_forward(self, address, port, handler=None)
    run(self)
    send_ignore(self, bytes=None)
    set_hexdump(self, hexdump)
    set_keepalive(self, interval)
    set_log_channel(self, name)
    set_subsystem_handler(self, name, handler, *larg, **kwarg)
    start_client(self, event=None)
    start_server(self, event=None, server=None)
    stop_thread(self)
    use_compression(self, compress=True)

    # channel
    close()
    exec_command(command)
    exit_status_ready(self)
    fileno(self)
    get_id(self)
    get_name(self)
    get_pty(self, term='vt100', width=80, height=24, width_pixels=0, height_pixels=0)
    get_transport(self)
    getpeername(self)
    gettimeout(self)
    invoke_shell(self)
    invoke_subsystem(self, subsystem)
    makefile(self, *params)
    makefile_stderr(self, *params)
    recv(self, nbytes)
    recv_exit_status(self)
    recv_ready(self)
    recv_stderr(self, nbytes)
    recv_stderr_ready(self)
    request_forward_agent(self, handler)
    request_x11(self, screen_number=0, auth_protocol=None, auth_cookie=None, single_connection=False, handler=None)
    resize_pty(self, width=80, height=24, width_pixels=0, height_pixels=0)
    send(self, s)
    send_exit_status(self, status)
    send_ready(self)
    send_stderr(self, s)
    sendall(self, s)
    sendall_stderr(self, s)
    set_combine_stderr(self, combine)
    set_name(self, name)
    setblocking(self, blocking)
    settimeout(self, timeout)
    shutdown(self, how)
    shutdown_read(self)
    shutdown_write(self)

# Java
