---
layout: post
title: Linux之系统管理
comments: true
date: 2016-04-03 14:04:05
updated:
tags:
- Linux
categories:
- Linux
permalink:
---

# 中文输入法

安装一个中文输入法框架fcitx(IBus, SCIM, UIM)：

    sudo apt-get install fcitx

安装一种输入法引擎：

    sudo apt-get install fcitx-googlepinyin
    sudo apt-get install fcitx-sunpinyin
    sudo apt-get install fcitx-libpinyin
    sudo apt-get install fcitx-sougoupinyin
    sudo apt-get install fcitx-cloudpinyin

配置程序：

    kcm-fcitx - for qt - <https://github.com/fcitx/kcm-fcitx>
    fcitx-configtool - for gtk - <https://github.com/fcitx/fcitx-configtool>

在键盘输入方式系统从ibus改为fcitx，然后重启。

# gedit打开txt文件乱码

    sudo apt-get install dconf-editor

org->gnome->gedit->preferences->encodings->auto-detected
添加'GB2312','GBK',...

# virtualbox 开机自动挂载共享文件夹

    sudo vim /etc/rc.local
    mount.vboxsf -w ShareFolderNameOnWindows MountPointOnLinux

# 挂载U盘失败

移动硬盘或者u盘不能挂载，删掉/etc/fstab的关于sdb的行，保存后重新插拔。

# Linux修改hostname

    sudo vim /etc/hostname
    sudo vim /etc/hosts
    sudo reboot

# Linux创建桌面图标（比如eclipse）

    cd /usr/share/applications
    sudo vi XXX.desktop

添加必要属性后拖到桌面或启动栏即可。

# Linux安装QQ

    sudo apt-get install libgtk2.0-0:i386
    sudo apt-get install lib32ncurses5
    sudo apt-get install -f
    sudo dpkg -i fonts-wqy-microhei_0.2.0-beta-2_all.deb
    sudo dpkg -i ttf-wqy-microhei_0.2.0-beta-2_all.deb
    sudo dpkg -i wine-qqintl_0.1.3-2_i386.deb

# 安装文档的包

    sudo apt-get install glibc-doc manpages-dev manpages-posix-dev manpages-zh

手册位于/usr/share/man

# 记录终端操作

安装相关工具:

    $sudo apt-get install ttyrec
    $sudo apt-get install imagemagick
    $hg clone https://bitbucket.org/antocuni/tty2gif

开始记录:

    $ttyrec

在终端播放记录文件ttyrecord:

    $ttyplay ttyrecord

将ttyrecord文件转化成gif文件:

    $tty2gif.py typing ttyrecord

将多个gif文件合并成一个文件:

    $convert -limit memory 2mb -limit map 2mb -delay 2 -loop 0 *.gif example.gif

# 网络代理

在下面路径添加代理脚本:

    /etc/profile.d

    sys_proxy.sh
    http_proxy="http://proxy-server:port"
    https_proxy="http://proxy-server:port"
    ftp_proxy="http://proxy-server:port"
    no_proxy=localhost,127.0.0.1,...
    export http_proxy ftp_proxy https_proxy no_proxy

# ufw & iptables

# upstart & systemd
