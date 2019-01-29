Title: Admin
Date: 2016-04-03 14:04:05
Tags: Linux, Ubuntu, CentOS, Suse



# Linux Admin

dpkg: ubuntu, debian.

rpm: fedora, centos, redhat.

zypper: suse.

***

# Linux系统常用的安装和配置

## virtualbox

开机自动挂载共享文件夹

    # 手动挂在命令, 需要安装增强功能
    $ mount -t vboxsf FolderNameOnWindows /path/on/linux

    # 实现开机自动挂载
    $ sudo vim /etc/rc.local
    mount.vboxsf -w ShareFolderNameOnWindows MountPointOnLinux

## xrdp

从windows的RDP远程连接linux.

use RDP on windows to connect to ubuntu16.04.

    sudo dpkg -i tigervncserver_1.6...deb # download and install tigervncserver first.
    sudo apt-get install -f
    sudo apt-get instal xrdp -y
    echo unity > ~/.xsession

use RDP on windows to connect to ubuntu14.04.

    sudo apt-get install xrdp
    sudo apt-get install xfce4
    echo xfce4-session > ~/.xsession
    sudo vim /etc/xrdp/startwm.sh
    # add 'startxfce4' to last line.
    sudo service xrdp restart

## systemd

sytemd是upstart的替代版本．通过查看/sbin/init指向systemd还是upstart.

    $ ls -l /sbin/init
    /sbin/init -> /lib/systemd/systemd

    /etc/systemd/system/***.service
    $ sudo vim ***.service
    $ sudo systemctl start/stop/status ***

    # 重新加载.service文件
    $ systemctl daemon-reload

    # 设置开机自动启动
    $ systemctl list-unit-files
    $ systemctl enable ***
    $ systemctl disable ***
    $ systemctl is-enabled grafana-server

日志管理:

    $ journalctl -xe ***.servivce

## upstart

如果init指向upstart, service如果在/etc/init.d找不到会去/etc/systemd/system找.

    $ ls -l /sbin/init
    /sbin/init

    /etc/init.d/***
    $ sudo vim ***
    $ sudo service *** start/stop/status

    # 设置开机自动启动
    $ update-rc.d *** defaults
    # 取消开机启动
    $ update-rc.d *** remove

## 清理内存的buff/cache

    echo 3 > /proc/sys/vm/drop_caches
    # reboot才能改回默认的0

## 终端现实超大艺术字

    $ sudo apt-get install figlet
    $ figlet <text>

***

# Ubuntu/Debian安装后的基本配置

    sudo apt-get install build-essential make libssl-dev

## 中文输入法

安装一个中文输入法框架fcitx(IBus, SCIM, UIM)：

    $ sudo apt-get install fcitx

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

## dconf修改配置

也可以通过系统自带的dconf命令修改．

    $ sudo apt-get install dconf-editor

gedit打开txt文件乱码

    # org->gnome->gedit->preferences->encodings->auto-detected 添加'GB2312','GBK',...

开启远程桌面无密码登陆

    $ dconf write /org/gnome/desktop/remote-access/require-encryption false
    or
    # org->gnome->desktop->remote-access->require-encryption false

## 挂载U盘失败

移动硬盘或者u盘不能挂载，删掉/etc/fstab的关于sdb的行，保存后重新插拔。

## 创建桌面图标（比如eclipse）

    cd /usr/share/applications
    sudo vi XXX.desktop

添加必要属性后拖到桌面或启动栏即可。

## 安装QQ

    sudo apt-get install libgtk2.0-0:i386
    sudo apt-get install lib32ncurses5
    sudo apt-get install -f
    sudo dpkg -i fonts-wqy-microhei_0.2.0-beta-2_all.deb
    sudo dpkg -i ttf-wqy-microhei_0.2.0-beta-2_all.deb
    sudo dpkg -i wine-qqintl_0.1.3-2_i386.deb

## 安装文档的包

手册位于/usr/share/man

    sudo apt-get install glibc-doc manpages-dev manpages-posix-dev manpages-zh

## 记录终端操作

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

## 添加用户为管理员

    $ vim /etc/sudoers
    user     ALL = (ALL:ALL) ALL

## Ubuntu网络设置

ubuntu修改hostname:

    $ sudo vim /etc/hostname
    new-hostname
    $ sudo vim /etc/hosts
    ip-address hostname
    $ sudo reboot

设置系统代理:

    $ vim /etc/profile.d/sys_proxy.sh
    http_proxy="http://proxy-server:port"
    https_proxy="http://proxy-server:port"
    ftp_proxy="http://proxy-server:port"
    no_proxy=localhost,127.0.0.1,...
    export http_proxy ftp_proxy https_proxy no_proxy

设置静态IP:

    $ ifconfig
    # 查看网卡，ubuntu14.04 eth0, ubuntu16.04 ens160
    $ vim /etc/network/interfaces
    auto eth0
    iface eth0 inet static
        address 192.168.0.1
        netmask 255.255.255.0
        gateway 192.168.0.0
        dns-nameservers 8.8.8.8
    $ sudo service networking restart

## E: Sub-process /usr/bin/dpkg returned an error code (1)

method1:

    $ sudo mkdir -p /var/lib/dpkg/info/package
    $ sudo mv /var/lib/dpkg/info/package.* /var/lib/dpkg/info/package

method2:

    $ sudo apt-get purge package
    $ sudo apt-get install package

## ubuntu14.04安装升级pip

    # ubuntu14.04 默认python2.7.6, 不带pip
    $ sudo apt-get install pip # 安装1.5.4
    $ sudo -H pip install -U pip
    $ sudo pip install pyopenssl ndg-httpsclient pyasn1
    $ sudo -H pip install -U pip

## ubuntu16.04安装配置python

    默认python3.5.2， 需要安装2.7.12
    sudo apt-get --yes install python2.7
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1

***

# Centos/Fedora/Redhat安装后的基本配置

    $ sudo yum -y install epel-release kernel-devel gcc gcc-c++

## Centos网络配置

安装mini版本之后配置网络：

    $ vi /etc/sysconfig/network-scripts/ifcfg-enxxx
    ONBOOT=no -> yes
    # service network restart
    $ sudo yum install net-tools
    $ ifconfig

设置静态IP:

    $ vim /etc/sysconfig/network-scripts/ifcfg-enxxx
    BOOTPROTO= # dhcp(自动获取), static(固定IP), node(手动设置)
    IPADDR="192.168.0.1"
    PREFIX="21"
    GATEWAY="192.168.0.0"
    DNS1="192.168.0.0"

设置可以同时访问外网和本地连接的方法：

    # 网卡１用于外网连接
    # settings -> network -> network card1 -> NAT
    $ cat /etc/sysconfig/network-scripts/ifcfg-en01
    BOOTPROTO=dhcp # 自动获取ip
    ONBOOT=yes
    UUID # 通过$ nmcli con show 命令查看
    HWADDR # 通过 $ ip addr 命令查看, 这个可以不设置

    # 网卡２用于本地局域网
    setting -> network-> network card2 -> host-only
    # cp /etc/sysconfig/network-scripts/ifcfg-en01 /etc/sysconfig/network-scripts/ifcfg-en02
    $ vim /etc/sysconfig/network-scripts/ifcfg-en02
    NAME
    DEVICE
    BOOTPROTO=static
    ONBOOT=yes
    UUID
    HWADDR
    IPADDR=192.168.56.102

    $ sudo service network restart

修改hostname,局域网可以根据hostname相互访问：

    $ sudo vim /etc/sysconfig/network
    NETWORKING=yes
    HOSTNAME=new-hostname

    $ sudo vim /etc/hostname
    new-hostname
    $ sudo vim /etc/hosts
    ip-address hostname

    $ sudo reboot

## centos安装增强功能

    $ sudo mkdir -p /media/cdrom
    $ sudo mount /dev/cdrom /media/cdrom
    $ cd /media/cdrom
    $ sudo ./VBoxLinuxAdditions.run --nox11

