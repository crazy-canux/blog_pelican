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

***

# shell命令

    bash --help

## thefuck

一个纠正shell命令输错的命令

<https://github.com/nvbn/thefuck>

***

# shell script

## shellcheck

一个debug脚本的工具．

<https://github.com/koalaman/shellcheck>

## shell注释

单行注释：

    # comment

多行注释：

    :<<!EOF!
    comment
    !EOF! can be any symbol and character.
    !EOF!

