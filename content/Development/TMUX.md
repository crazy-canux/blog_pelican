---
layout: post
title: TMUX
comments: true
date: 2016-06-19 11:17:53
updated:
tags:
- tmux
- screen
categories:
- Develop
- TMUX
permalink:
---

# tmux

tmux是终端复用工具，类似于gnu screen。

tmux三个基本概念：

1. 会话（session）

2. 窗口（window）

3. 面板（pane）

tmux使用c/s架构，tmux命令启动tmux服务器，一个tmux服务有多个session，
每个session就是tmux管理下的伪终端集合，一个session有多个window与之关联，
每个window就是一个伪终端，占据整个屏幕，一个window可以被分割成多个pane。

***

# tmux安装和配置

tmux依赖libevent和ncurses库。

<http://tmux.github.io/>

<http://libevent.org/>

<http://invisible-island.net/ncurses/>

    sudo apt-get install tmux
    sudo yum install tmux

用户配置文件： ~/.tmux.conf

系统配置文件： /etc/tmux.conf

***

# tmux相关项目

## TPM

Tmux Plugins Manager.

<https://github.com/tmux-plugins/tpm>

***

# tmux用法

    man tmux

开启tmux：

    tmux

退出tmux：

    exit
    ctrl + d

列出tmux会话：

    tmux ls

## tmux快捷键

tmux的prefix是ctrl-b

按下ctrl-b然后松开，通知tmux下面的按键是快捷键。

查看所有快捷键：

    ctrl-b + ?


显示时间：

    ctrl-b + t

## session操作

交互式选择一个session:

    ctrl-b + s

选择一个session来detach：

    ctrl-b + D

detach当前session:

    ctrl-b + d

重命名当前的session：

    ctrl-b + $

## window操作

交互式选择一个window:

    ctrl-b + w

创建一个新window:

    ctrl-b + c

关闭当前window:

    ctrl-b + &

切换到上一个window:

    ctrl-b + p

切换到下一个window:

    ctrl-b + n

移到之前选中的window：

    ctrl-b + l

使用window号切换window:

    ctrl-b + [number]

重命名window:

    ctrl-b + ,

## pane操作

横向分屏:

    ctrl-b + %

纵向分屏:

    ctrl-b + "

选择pane:

    ctrl-b + [方向键]

关闭当前pane:

    ctrl-b + x

显示pane号:

    ctrl-b + q

把当前的pane变成一个window：

    ctrl-b + !

移动到之前的活跃的pane：

    ctrl-b + ;

选择当前window的下一个pane：

    ctrl-b + o

## tmux使用鼠标和粘贴复制

复制：

    shift-鼠标左键

粘贴：

    shift-鼠标右键

列出所有粘贴缓冲区：

    ctrl-b + #

交互式选择一个缓冲区的内容粘贴：

    ctrl-b + =

使用复制模式：

    ctrl-b + [

使用粘贴模式：

    ctrl-b + ]
