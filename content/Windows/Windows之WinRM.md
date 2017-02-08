---
layout: post
title: Windows之WinRM
comments: true
date: 2016-07-17 08:36:36
updated:
tags:
- winrm
categories:
- Windows
permalink:
---

# WinRM

Windows Remote Management

WinRM是WSMAN(WS-Management Protocol)的增强版。

WinRM是基于SOAP的防火墙友好的远程协议。

<https://msdn.microsoft.com/en-us/library/aa384426(v=vs.85).aspx>

WinRM设置:

<https://msdn.microsoft.com/en-us/library/aa384372(v=vs.85).aspx>

检查winrm所有配置：

    cmd> winrm get winrm/config

快速设置winrm：

    cmd> winrm quickconfig
    cmd> winrm quickconfig -transport:https

查看listener配置：

    cmd> winrm enumerate winrm/config/listener

WinRM配置包括监听设置,协议设置,Client,Service和Winrs四部分.

# 权限管理

windows的三种网络安全协议。

Basic是基本的明文协议, NTLM是早期的安全协议,Kerberos是最新的安全协议.

查看service的auth配置：

    cmd> winrm get winrm/config/service/auth

service只有Negotiate和Kerberos是默认开启的:

    Basic = false
    Certificate = false
    Kerberos = true
    Negotiate = true
    CredSSP = false

Negotiate对domain用户选择kerberos,对local用户选择NTLM.

设置service的Basic和Certificate和CredSSP(默认关闭)：

    cmd> winrm set winrm/config/service/auth @{Basic="true"}
    cmd> winrm set winrm/config/service/auth @{Certificate="true"}
    cmd> winrm set winrm/config/service/auth @{CredSSP="true"}

# python

pywinrm

<https://github.com/diyan/pywinrm>

使用basic, certificate和NTLM：

    pip install pywinrm

使用kerberos需要安装：

    sudo apt-get install libkrb5-dev
    pip install pywinrm[kerberos]

使用CredSSP需要安装:

    sudo apt-get install libssl-dev
    pip install pywinrm[credssp]

transport参数:

Basic and Certificate(plaintext) just support local user.

SSL will use Certificate when used cert_pem and cert_key_pem, or revert to Basic over https.

NTLM support both local user and domain user, auth = 'domain\\user'

CredSSP support both local user and domain user and just use https, auth = 'domain\\user'

Kerberos just support domain user, auth = 'user@domain'

Session使用：

    import winrm

    Session(target, auth, **kwargs)
    run_cmd(self, command, args=())
    run_ps(self, script)

    # domain 用户使用 ntlm
    s = winrm.Session('ip address', auth=('domain\user', 'password'), transport='ntlm', server_cert_validation='ignore')

    r = s.run_cmd('ipconfig', ['/all'])
    return_code = r.status_code
    output = r.std_out
    error = r.std_err

Protocol使用：

    import winrm

    Protocol(endpoint, transport=u'plaintext', username=None, password=None, realm=None, service=None, keytab=None, ca_trust_path=None, cert_pem=None, cert_key_pem=None, server_cert_validation=u'validate', kerberos_delegation=False, read_timeout_sec=30, operation_timeout_sec=20, kerberos_hostname_override=None)

    open_shell(self, i_stream=u'stdin', o_stream=u'stdout stderr',
    run_command(self, shell_id, command, arguments=(), console_mode_stdin=True,
    get_command_output(self, shell_id, command_id)
    working_directory=None, env_vars=None, noprofile=False, codepage=437,
    lifetime=None, idle_timeout=None)
    skip_cmd_shell=False)
    send_message(self, message)
    cleanup_command(self, shell_id, command_id)
    close_shell(self, shell_id)

    # domain 用户使用 ntlm
    p = winrm.Protocol(endpoint='http://127.0.0.1:5985/wsman', transport='ntlm', username=r'DOMAIN\user', password='password',server_cert_validation='ignore')

    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    p.close_shell(shell_id)
