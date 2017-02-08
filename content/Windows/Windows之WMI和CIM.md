---
layout: post
title: Windows之WMI和CIM
comments: true
date: 2016-04-03 14:15:47
updated:
tags:
- Windows
- wmi
categories:
- Windows
permalink:
---

# WMI/CIM

WMI: windows management instrumentation.

<https://msdn.microsoft.com/en-us/library/aa394582(v=vs.85).aspx>

CIM: common information model.

<https://msdn.microsoft.com/en-us/library/aa389234(v=vs.85).aspx>

DCOM: distributed COM.

wmi通过DCOM远程连接，但是DCOM不能绕过防火墙。

命名空间:

    root\cimv2
    root\microsoftdns
    root\securitycenter

WMI工具：
1. windows自带wmi测试工具wbemtest.
2. WMI Explorer用于查找wmi和cim的Class和Properties.

<http://www.ks-soft.net/hostmon.eng/wmi/index.htm#SysReq>

windows怎样设置wmi：

135 (Microsoft RPC), 137-139 (NetBIOS) and 445 (Microsoft DS). These are TCP ports.

设置的用户需要是管理员组。

<https://technet.microsoft.com/en-us/library/cc771551(v=ws.11).aspx>

给wmi设置fix port(server in DMZ)：

使用过程中不需要指定端口。

<https://msdn.microsoft.com/zh-cn/library/bb219447(v=vs.85).aspx>

# wmic

wmic是wmi的客户端命令。

windows的wmic：

    >wmic # 进入wmi的交互模式
    >wmic -? # 查看帮助
    >wmic /? # 查看帮助
    >wmic ... # 非交互模式运行命令
    >wmic process call create shutdown.exe # 本地关机

linux的wmic：

Linux需要自己创建wmic命令，可以通过samba获取，也可以安装openvas的安装包。

    $man wmic
    $wmic -U [domain/]adminuser%password //host "select * from Win32_ComputerSystem"

<https://mikepalmer.net/debianubuntu-wmi-client-package-with-openvas-libwmiclient1-patches/>

# WMI的Class

<https://msdn.microsoft.com/zh-cn/library/aa394554(v=vs.85).aspx>

1. wmi system class

    <https://msdn.microsoft.com/zh-cn/library/aa394583(v=vs.85).aspx>

        __Win32Provider
        ...

2. MSFT class

    policy provider classes

        MSFT_Providers
        MSFT_Rule
        MSFT_SomFilter

    WMI Troubleshooting classes

        MSFT_WmiProvider_Counters
        MSTF_WmiSelfEvent

3. CIM class

    <https://msdn.microsoft.com/zh-cn/library/aa386179(v=vs.85).aspx>

        CIM_Action
        ...

4. Standard Consumer class

        ActiveScriptEventConsumer
        CommandLineEventConsumer
        LogFileEventConsumer
        NTEventLogEventConsumer
        ScriptingStandardConsumerSetting
        SMTPEventConsumer

# WMI的Provider

<https://msdn.microsoft.com/zh-cn/library/aa394570(v=vs.85).aspx>

1. Win32 Provider

    Computer System Hardware Classes

    <https://msdn.microsoft.com/zh-cn/library/aa389273(v=vs.85).aspx>

        Win32_Fan
        ...

    Operating System Classes

    <https://msdn.microsoft.com/zh-cn/library/dn792258(v=vs.85).aspx>

        Win32_ClassicCOMApplicationClasses
        ...

    Performance Counter Classes

    <https://msdn.microsoft.com/zh-cn/library/aa392738(v=vs.85).aspx>

        Win32_Perf
        Win32_PerfFormattedData
        Win32_PerfRawData

    WMI Service Management Classes

    <https://msdn.microsoft.com/zh-cn/library/dn792273(v=vs.85).aspx>

        Win32_MethodParameterClass
        Win32_WMISetting
        Wim32_WMIElementSetting

# wql

<https://msdn.microsoft.com/zh-cn/library/aa394606(v=vs.85).aspx>

wql关键字：

    SELECT, FROM, WHERE, AND, OR, NOT, NULL, IS, TRUE, FALSE, WITHIN, LIKE, HAVING
    REFERENCES OF, KEYSONLY, ISA, ASSOCIATORS OF, __CLASS, GROUP Clause

常用WQL：

    select * from meta_class where __class like '%win32%' # 查询wmi的类
    select * from meta_class where __class like '%cim%' # 查询cim的类

    select * from cim_datafile where drive="c:" and path="\\path\\" and filename like "%%" and extension like '%%'
    select * from cim_directory where drive="c:" and path="\\path\\"
    select * from cim_logicaldisk
    select * from win32_operationsystem
    select * from win32_service
    select * from win32_process

# Python

## windows

Windows安装[pywin32](https://sourceforge.net/projects/pywin32/?source=navbar)和[wmi](http://timgolden.me.uk/python/wmi/index.html)两个包,可以访问wmi。

    pip install pywin32
    pip install wmi
    import wmi
    c = wmi.WMI()
    c.<wmi class/wmi provider>

## linux

linux需要先安装wmic命令。

Linux通过subprocess/sh远程执行wmic命令。

### subprocess

python标准库subprocess

    import subprocess
    wmi_output = subprocess.check_output(command)
    command = ['wmic', '-U', domain\\user%password, //host, wql]

### sh

sh是subprocess的升级版。

    pip install sh

    from sh import wmic
    output = sh.wmic(arguments)
    arguments = ['-U', domain\\user%password, //host, wql]

