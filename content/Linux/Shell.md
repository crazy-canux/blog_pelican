Title: Shell
Date: 2016-04-01 20:42:59
Tags: Shell, Bash, Zsh, Fish



# Shell

Linux的shell有很多种,大多数linux发行版的默认登录shell是BASH。

查看当前使用的shell：

    echo $SHELL
    echo $0

查看安装了哪些shell：

    cat /etc/shells

设置登陆shell:

    $chsh -s $(which shellname)

shell分为登陆shell和交互式shell:

    # 输出有i的就是交互shell
    $echo $-

非交互登陆shell:
* 先运行系统配置文件/etc/profile(调用/etc/bash.bashrc和/etc/profile.d/*.sh)
* 然后运行用户配置文件~/.profile(调用~/.bashrc和~/bin)
* 最后退出用户登陆~/.bash_logout

交互非登陆shell:
* 先运行/etc/bash.bashrc(调用/etc/bash_completion(调用/etc/bash_completion.d/*.sh))
* 然后运行~/.bashrc(调用~/.bash_aliases和~/bash.d和~/bin)

***

# shell相关项目

## bash-it

大部分发行版默认使用bash,无需额外安装。

bash的优化项目bash-it：

<https://github.com/Bash-it/bash-it>

## zsh

<http://www.zsh.org/>

## oh-my-zsh

<https://github.com/robbyrussell/oh-my-zsh>

## fish-shell

<https://github.com/fish-shell/fish-shell>

## oh-my-fish

<https://github.com/oh-my-fish/oh-my-fish>

## thefuck

一个纠正shell命令输错的命令

<https://github.com/nvbn/thefuck>

## shellcheck

一个debug脚本的工具．

<https://github.com/koalaman/shellcheck>

***

# shell script

基本语法

    #!/usr/bin/env bash

    command1 && command2    # 当command1执行成功（返回0)才会执行command2
    command1 || command2    # 当command1执行失败（返回非0)才会执行command2

## shell注释

单行注释：

    # comment

多行注释：

    :<<!EOF!
    comment
    !EOF! can be any symbol and character.
    !EOF!

## shell关键字和特殊符号

三个特殊命令

    echo
    printf
    test

关键字

    function

## shell运算符和优先级

原生shell不支持数学运算，可以通过expr来实现．

    # expr表达式内部运算符前后要空格.
    val=`expr 2 + 2`

算术运算符

    +
    -
    *    # `expr $a \* $b`, 不要转义
    /
    %
    =     # a=$b
    ==    # [ $a == $b ] , 需要中括号，需要空格
    !=    # [ $a != $b ], 同上

关系运算符

    # 只支持数字，不支持字符串．需要中括号和空格
    -eq
    -ne
    -gt
    -lt
    -ge
    -le

布尔运算符

    # 符合短路和斷路原则
    !     # [ !false ]
    -o    # [ exp1 -o exp2 ], 有一个为true就返回true
    -a    # [ exp1 -a exp2], 两个都是true才返回true

逻辑运算

    ||
    &&

字符串运算符

    =
    !=
    -Z    # 字符串长度为0返回true
    -n    # 字符串长度为0返回false
    str    # [ $a ], 字符串不为空返回true

文件测试运算符

    -b
    -c
    -d
    -f
    -g
    -k
    -p
    -u
    -r
    -w
    -x
    -s
    -e

## shell数据结构和变量

变量类型：

    局部变量
    环境变量
    shell变量

定义变量:

    等号前后不能有空格
    不能用数字开头命名变量
    不能用标点符号和关键字

    var=`ls /etc`  # 返回的是stdout+stderr
    var=$(ls /etc)

使用变量：

    $var
    ${var}

只读变量:

    使用readonly定义只读变量，不能再重新赋值

    var=value
    readonly var

删除变量:

    使用unset删除变量，被删除的变量不能使用.

    var=value
    unset var

变量操作：

    ${var/old/new} # 将变量中的old替换成new.
    ${var:start:end} # 获取变量的start到end个字符，相当于var[start:end],下标从0开始.

字符串类型：

    单引号的字符串是原样输出，其中的变量是无效的，里面不能有单引号.
    var='this is string'

    双引号的字符串里面可以有变量，可以出现转义字符.
    var="this is string"

    获取字符串长度
    var="this is tring"
    echo ${#var}

    字符串切片
    var="this is string"
    ${var:start:end}    # 相当于var[start:end], 下标从0开始

    获取pattern在string中的起始下标
    string="this is string"
    `expr index "$string" pattern`

数字类型：

数组:


## shell控制流

if

    if []; then command; ...; fi

    if condition
    then
        command
    fi

    []/test 中必须为执行的命令的stdout+stderr.
    if [ ! `cat file | grep pattern | wc -l` ]
    if [ ! 0 ] 此时0为真, [ ! 0 ]为假

    if command 看返回码$?, 0表示真,其它表示假.

if-else

    if condition; then command; ...; else command; fi

    if condition
    then
        command
    else
        command
    fi

if-elif-else

    if condition; then command; ...; elif condition; then command; ...; else command; fi

    if condition
    then
        command
    elif condition
    then
        command
    else
        command
    fi

while

    while condition; do command;...; done

    while condition
    do
        command
    done

    # 无限循环
    while :
    do
        command
    done

    # 无限循环
    while true
    do
        command
    done

for

    for ((i=1; i<=100; i++))
    for i in {1..100}
    for i in `seq 1 100`

    for VAR in ${1,2,3,...}; do command; ...; done

    for var in item1 item2 ... itemN
    do
        command
    done

    # 无限循环
    for (( ; ; ))

until

    until condition; do command; ...; done

    until condition
    do
        command
    done

case

    case $VAR in
    val1)
        command
        ...
        ;;
    val2)
        command
        ...
        ;;
    esac

break

continue

## shell函数

return只是返回当前函数，不退出主程序

exit直接退出主程序

通过关键字function定义函数:

    function Name {    // ()可省略
    function Name() {
        ...
        # 如果不显示调用return返回，则函数返回最后一条命令的结果
        return $?
    }

也可以直接定义函数:

    Name() {
        ...
    }

函数返回值:

    $?

函数参数：

    $1 - $9 可以在函数内部获取调用函数时候传递进来的９个参数
    ${10} - ${100} 获取第十个参数和后面的参数

特殊字符：

    $# 表示传递到脚本的参数个数,不包括程序本身
    $* 传入所有参数
    $@ 传入所有参数
    $$
    $!
    $-

## 输入输出和重定向

stdout和stdin重定向到一个地方:

    1> 只重定向stdout
    2> 只重定向stderr
    2>&1 同时重定向stdout+stderr

    main > 2>&1 log1.log | tee log2.log # 同时重定向到两个文件
    main 2>&1 | tee ${LOG} # 同时将stdout和stderr输出到终端和日志文件.

## 文件包含
