---
layout: post
title: PowerShell之RemoteManagement
comments: true
date: 2016-07-18 14:54:39
updated:
tags:
- powershell
- wmi
- cim
- winrm
- rpc
categories:
- Windows
- PowerShell
permalink:
---

# Windows远程管理

1. WinRM, 远程处理,在远程机器上执行命令
2. WMI/CIM
3. RPC, 远程连接,在发起远程连接的机器上执行命令

***

# WinRM

一对一远程处理:

类似于linux的ssh。

    Enter-PSSession -ComputerName name
    ...
    Exit-PSSession

一对多远程处理:

同时远程到多台机器执行命令或脚本。

Invoke-Command一次创建一个连接对象，返回PSComputerName属性，执行完后就关闭连接。

    Invoke-Command -ComputerName name1,name2 -ScriptBlock {command1;command2}

    Invoke-Command -ComputerName name1,name2 -FilePath filepath

    Invoke-Command -ComputerName (Get-Content hosts.txt) ...

通过argumentlist把本地的参数传给远程的命令:

    $lvar1="value1"
    $lvar2="value2"
    Invoke-Command -ComputerName name
    -ScriptBlock {
    Param($var1, $var2)
    ...
    }
    -ArgumentList $lvar1, $lvar2

通过\$using:传本地参数到远程机器：

    $var1="value1"
    Invoke-Command -ComputerName name
    -ScriptBlock {
    ... $using:var1
    }

创建持久的远程处理：

    $session1=New-PSSession -ComputerName server1
    Enter-PSSession -Session $session1 ...
    Invoke-Command -Session $session1 ...

***

# WMI

    Get-WmiObject
    Remove-WmiObject
    Invoke-WmiMethod
    Register-WmiEvent
    Set-WmiInstance

    # 用powershell跑一个wql。
    Get-WmiObject -Query "select * from win32_service where name='winRM'" | Format-List -Property Name,status

    # 远程管理
    Get-WMIObject -ComputerName ...

# CIM

    Get-CimClass
    Get-CimInstance
    Get-CimSession
    Get-CimAssociatedInstance
    Invoke-CimMethod
    New-CimInstance
    New-CimSession
    New-CimSessionOption
    Register-CimIndicationEvent
    Remove-CimInstance
    Remove-CimSession
    Set-CimInstance

***

# RPC

    # 远程连接
    Get-Service -ComputerName ...
