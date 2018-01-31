Title: WinRM
Date: 2016-07-17 08:36:36
Tags: Windows, WinRM



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

windows的三种网络安全协议。

Basic是基本的明文协议, NTLM是早期的安全协议,Kerberos是最新的安全协议.

# service权限管理

查看service的auth配置：

    cmd> winrm get winrm/config/service/auth

service只有Negotiate和Kerberos是默认开启的:

    Basic = false
    Kerberos = true
    Negotiate = true
    Certificate = false
    CredSSP = false

Negotiate对domain用户选择kerberos,对local用户选择NTLM.

设置service的Basic和Certificate和CredSSP(默认关闭)：

    #cmd> winrm set winrm/config/service/auth @{Basic="true"}
    #cmd> winrm set winrm/config/service/auth @{Certificate="true"}
    #cmd> winrm set winrm/config/service/auth @{CredSSP="true"}

设置是否允许不加密：

    #cmd> winrm set winrm/config/service @{AllowUnencrypted="true"}

# client权限管理

查看client的auth配置：

    cmd> winrm get winrm/config/client/auth

设置client的CredSSP(默认关闭),其它默认都是开启：

    #cmd> winrm set winrm/config/client/auth @{CredSSP="true"}

设置client的trustedhosts:

    #cmd> winrm set winrm/config/client @{TrustedHosts="*"}

# Winrs

winrs是winrm的客户端．

    $winrs -r:http://<ip-address> -u:domain/user -p:pass command

***
