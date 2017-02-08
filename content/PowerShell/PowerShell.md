---
layout: post
title: PowerShell
comments: true
date: 2016-04-26 09:52:02
updated:
tags:
- powershell
- windows
categories:
- Windows
- PowerShell
permalink:
---

# PowerShell

Console: command line interface

ISE: script editor and console combination

Version:

2.0,3.0,4.0,5.0

C:\Windows\System32\powershell 存放64位powershell

C:\Windows\SysWOW64\powershell 存放32位powershell

    >$PSVersionTable
    >$HOST

Install/Update:

<https://www.microsoft.com/zh-CN/download/details.aspx?id=40855>

安装Windows Management Framework4.0即可。

    >$PSHOME

多版本时切换版本:

    >powershell -version 2

***

# powershell相关项目

<https://github.com/Microsoft>

<https://github.com/PowerShell>

<https://github.com/PowerShellOrg>

## win32-openssh

windows的SSH。

<https://github.com/PowerShell/Win32-OpenSSH>

***

# powershell命令

    >powershell -?
    >powershell /?
    >powershell -help

***

# powershell script

powershell是默认大小写不敏感的。

同一行多个命令需要用分号;隔开。

powershell的安全策略：
1. restricted(default)
2. allsigned
3. remotesigned
4. unrestricted
5. bypass

# 注释

单行注释：

    # comment

多行注释(文档注释)：

    <#
    comment1
    comment2
    ...
    #>

帮助文档:

在脚本开头的注释中用下面关键字插入文档。

    <#
    .SYNOPSIS
    Write your synopsis here.

    .DESCRIPTION
    Write your description here.

    .PARAMETER param1
    Write your param1 information here.

    .EXAMPLE
    Write your example1 here.

    .NOTES
    Write your notes here.

    .LINK
    http://test.com
    #>

# 数据类型

## 变量

所有的变量都存储在Variable驱动器中,可以用Variable驱动器对变量操作。

    ls Variable: # 查看所有变量

系统变量：

    $_    # 表示管道中的当前对象
    ?    # True表示上一个命令成功执行,False失败

自定义变量：

变量以\$开头定义,但是\$不是变量名的一部分。

变量包含数字，字母和小划线。


    $var1="test"
    $var1

    # 交换两个变量的值
    $var1,$var2=$var2,$var1

变量类型：

可以不用指定变量类型。

    [string]$str="123"
    [int]$num=123
    [boolean]bool="True"

判断变量类型：

    $str -is [string]
    $num -as [int]

## 数组

包含多个变量就是一个数组。

    $var2=1,2,3
    $var2[index]
    $var2[0] # 数组第一个元素
    $var2[-1] # 数组最后一个元素

## 字典：

hash类型。

    @{L=<key>;
    E={$_.<value>};
    formatstring=<format>}

    @{N=<key>;E={$_.<value>}}
    @{Label=<key>;E={$_.<value>}}
    @{Name=<key>;E={$_.<value>}}

# 运算符

基本运算符：

    = # 赋值运算符，可以把任何数据类型包括对象赋值给变量
    + # 加法和字符串拼接
    - # 减法
    * # 乘法
    / # 除法
    () # 优先运算符

特殊运算符：

    $($procs[0].name) # 子变量
    '$var' # 单引号中的变量原样输出
    "$var" # 双引号中的变量被替换
    "`$var" # `重音符可以用在双引号中转义
    `t    # 制表符
    `n    # 换行符
    kb/mb/gt/tb/pb # 单位可以运算

比较运算符：

    -eq
    -ne
    -gt
    -ge
    -lt
    -le
    -contains 包含
    -notcontains

布尔运算符：

    -not 求反
    -and
    -or
    -xor

***

# 控制流

powershell支持foreach循环。

if条件语句：

    if ($this -eq $that) {
        expression
    } elseif ($those -gt $these) {
        expression2
    } else {
        expression3
    }

switch条件语句：

    switch ($condition) {
        val1 {
            expression
            break
        }
        val2 {
            expression2; break
        }
        default {
            default_expression
        }
    }

foreach循环语句：

    foreach ($name in $names) {
        expression
    }

for循环语句：

    for ($loop=1; condition; $loop++)
    {
        expression
    }

while循环语句:

    while (condition)
    {
        expression
    }

do-while循环语句：

    do {
        expression
    } while (condition)

break语句：

break用于循环和switch语句。

continue语句：

continue用于循环语句。

***

# 函数

函数：

    function name {
        ...
    }

调用函数:

    .\file.ps1
    name

选项：

    [CmdletBinding()]
    Param(
        [Parameter(Mandatory=$True)]
        [String]$ComputerName, # ComputerName强制为通过命令行输入参数

        [int]$EventID=1234, # EventID有默认参数

        [Parameter(Mandatory=$True)][ValidateRange(0,23)]
        [int]$Number # 给出参数的范围
    )

    [CmdletBinding(SupportsShouldProcess$True)] # 支持-whatif和-confirm
    [ValidateSet(1,3,8)] # 给出参数的可选值
    [alias("id", "nunber")] # 给参数指定别名

***

# 模块

系统模块路径：

    c:\Windows\System32\WindowsPowershell\v1.0\Modules\

函数可以打包成模块放在系统模块路径或用户自己的模块路径。

模块放到同名的目录mytools下，取名mytools.psm1

导入用户自己路径下的模块：

    Import-Module -name C:\Modules\mytools

***

# 异常和错误处理

调试语句：

    Write-Verbose "print verbose information." # 打印调试信息

    Write-Debug "print debug information." # 使用-Debug进入debug模式，exit退出。

调试相关系统变量：

    $ErrorActionPreference='Continue' # 调试的系统变量，默认报错继续执行

    $DebugPreference='SilentlyContinue'

    $ErrorView='NormalView'

    $Error 存储整个shell的错误。

异常捕获：

    Try {
        expressions
    }
    Catch {
        "execute when catch the error."
    }
    Finally {
        "execute anyway."
    }

断点调试：

    $Condition = {if ($a -is [int] -and $a -gt 100) {Write-Host "`$a was modified"}}
    $Breakpoint = Set-PSBreakpoint -Variable a -Mode Write -Script $psise.CurrentFile.FullPath -Action $Condition
