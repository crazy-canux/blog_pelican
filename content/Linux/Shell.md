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

## shell注释

单行注释：

    # comment

多行注释：

    :<<!EOF!
    comment
    !EOF! can be any symbol and character.
    !EOF!

## shell关键字和特殊符号

## shell运算符和优先级

## shell数据结构和变量

变量类型：

    局部变量
    环境变量
    shell变量

定义变量:

    等号前后不能有空格
    不能用数字开头命名变量
    不能用标点符号和关键字

    var=`ls /etc`
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

if-else

    if []; then command; ...; else command; fi

if-elif-else

    if []; then command; ...; elif []; then command; ...; else command; fi

while

    while []; do command;...; done

for

    for VAR in ${1,2,3,...}; do command; ...; done

## shell函数

return只是返回当前函数，不退出主程序

exit直接退出主程序

## 输入输出和重定向
