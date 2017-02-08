---
layout: post
title: PowerShell之内置命令
comments: true
date: 2016-05-24 10:44:44
updated:
tags:
- powershell
- windows
categories:
- Windows
- PowerShell
permalink:
---

# Get-Help和Help:

get-help查看帮助信息,help分页查看帮助信息，man是help的别名

命令说明：

    Get-Help
    Help

查看所有命令和概念：

    Get-Help *
    Help *

模糊查找命令和概念：

    Get-Help *<name>*
    Help *<name>*

查看具体命令帮助：

    Get-Help {<CmdletName> | <TopicName>}
    Help {<CmdletName> | <TopicName>}
    <CmdletName> -?

get-help/help的选项:

    get-help get-help
    -examples # 查看示例
    -full # 查看所有帮助
    -parameter # 查看选项的帮助
    -detailed # 查看详细信息
    -online # 打开文档中的link
    -showwindow # 用窗口打开

# Helpfile

3.0/4.0 需要先下载帮助手册：

    update-help

所有helpfile：

    Get-Help/Help about_*

查看具体helpfile：

    Get-Help/Help about_<name>

***

# Cmdlets

cmdlets是powershell的内置命令,类型是System.Management.Automation.CmdletInfo

cmdlets的方法：

    Equals
    GetHashCode
    GetType
    ToString

cmdlets的属性：

    CommandType
    DefaultParameterSet
    Definition
    HelpFile
    ImplementingType
    Module
    ModuleName
    Name
    Noun
    OutputType
    Parameters
    ParameterSets
    PSSnapln
    Verb
    Visibility
    DLL
    HelpUri

常用cmdlets命令：

    Get-Command -CommandType cmdlet # 查看所有cmdlet

    Get-Command
    Invoke-Command
    Measure-Command
    Show-Command
    Trace-Command

    Get-Service
    New-Service
    Restart-Service
    Resume-Service
    Set-Service
    Stop-Service
    Suspend-Service

    Get-Process
    Debug-Process
    Start-Process
    Stop-Process
    Wait-Process

    Get-Member  # 查看属性
    Add-Member

    Get-Host
    Read-Host
    Write-Host
    Out-Host

    Out-Default
    Out-File    # 重定向，也可以用>, >>
    Out-GridView
    Out-Null
    Out-Printer
    Out-String

    Write-Debug
    Write-Error
    Write-EventLog
    Write-Output
    Write-Progress
    Write-Verbose
    Write-Warning

# Function

powershell内置函数

    Get-Command -CommandType function # 查看所有function
    ls function:

所有function：

    prompt
    TabExpansion2
    Clear-Host
    more
    help
    mkdir
    Get-Verb
    oss
    cd..
    cd\
    ImportSystemModules
    Pause
    A:
    ...
    Z:
    Get-FileHash

# Alias

powershell内置别名

    Get-Command -CommandType alias # 查看所有alias
    dir alias: # 查看所有alias
    ls alias: | where {$_.Definition.Startswith("Start")}

    Get-Alias # 查看所有alias
    Set-Alias
    New-Alias
    Import-Alias
    Export-Alias

常用alias：

    ForEach-Object    %/foreach
    Where-Object    ?/where
    Select-Object    select
    Compare-Object    compare/diff
    Tee-Object    tee
    Sort-Object    sort

    Set-Location    cd/chdir/sl
    Get-Location    pwd/gl

    Clear-Content    clc
    Get-Content    cat/type/gc

    Clear-History    clhy
    Get-History    h/history/ghy
    Invoke-History    ihy/r

    Clear-Variable    clv
    Set-Variable    set/sv

    Clear-Item    cli
    Clear-ItemProperty    clp
    Copy-Item    copy/cp/cpi
    Remove-Item    del/erase/rd/ri/rm/rmdir
    Move-Item    mv/move/mi
    Get-ChildItem    dir/ls/gci

    Get-Process    ps/gps
    Stop-Process    kill/spps
    Start-Process    start/saps

    Clear-Host    clear/cls

    Write-Output    echo/write

    New-PSDrive    mount

    Invoke-WebRequest    curl/wget

    Start-Sleep    sleep

    help    man
    mkdir    md

***

# Provider

provider相关cmdlet：

    Get-PSProvider # 查看provider
    Get-PSDrive    # 查看驱动器
    New-PSDrive    # 新建驱动器
    Remove-PSDrive    # 删除驱动器

所有provider：

    # 这三个驱动器可以用ls或dir直接查看内容
    ls alias:
    dir function:
    Alias   # 别名驱动器
    Function    # 函数驱动器
    Variable    # 变量驱动器

    # 这三个驱动器需要具体的驱动器,然后cd进去查看
    FileSystem    # 文件系统驱动器
    Environment
    Registry

    help/get-help <provider_name>    # 查看provider帮助

***

# object

object主要通过管道|使用。

object相关的cmdlet：

    Compare-Object
    ForEach-Object
    Group-Object
    Measure-Object
    New-Object
    Select-Object
    Sort-Object
    Tee-Object
    Where-Object

object转化：

    get-command -verb *convert*
    ...

导出object：

    get-command -verb *export*
    ...

导入object：

    get-command -verb *import*
    ...

# module

    Get-Module
    get-module -listavailable # 查找安装的模块
    Import-Module
    import-module sqlps # 导入第三方mssql模块
    get-command -module sqlps # 查看模块中所有命令
    New-Module
    Remove-Module

# format

安装路径有一些xml文件已经做了一些默认的格式化。

格式化的数据只能传给Out-File/out-host/out-printer/out-null/out-string/out-default.

    Export-FormatData
    Get-FormatData
    Update-FormatData
    Format-Custom
    Format-List
    Format-Table
    Format-Wide
