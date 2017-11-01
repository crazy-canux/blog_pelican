Title: Shell Coreutils
Date: 2016-03-31 21:51:25
Tags: Linux, Shell, Coreutils, Bash, Zsh, Fish



# Linux的外部命令

Linux外部命令的项目是coreutils。

外部命令在coreutils目录中

查看外部命令所在目录：

    echo $PATH

外部命令在下列目录中：

    /sbin

    /bin

    /usr/sbin

    /usr/bin

    /usr/local/sbin

    /usr/local/bin

    /usr/games

    /usr/local/games

查看外部命令手册的在线手册：

    man [command]
    info [command]

自定义外部命令：

添加\$PATH变量，然后放到该目录。

***

# 系统管理

    uname # 打印linux系统信息
    $ uname -a
    cat /etc/issue
    cat /proc/version

    lsb_release # 查看发行版本信息
    $ lsb_release -a

    getconf # 查询系统配置的变量，LONG_BIT表示系统位数

    lscpu # 显示cpu架构的信息
    cat /proc/cpuinfo # 查看cpu信息

    vmstat # 报告虚拟内存的统计信息
    free # 显示空闲和使用的系统内存
    cat /proc/meminfo # 查看内存信息

    lspci # 列出所有PCI设备
    lsusb # 列出USB设备
    lsblk # 列出块设备
    lshw # 列出硬件

    clear
    passwd
    pkill

# 文件和目录管理

    mkdir
    tree
    cat
    col
    colrm
    comm
    csplit
    ed
    ex
    fmt
    fold
    join
    look
    mtype
    pico
    sort
    tr
    expr
    uniq
    wc
    chmod
    chown
    chgrp
    chattr
    cksum
    cmp
    diff
    diffstat
    file
    cut
    less
    more
    locate
    lsattr
    mattrib
    mdel
    mdir
    mktemp
    mmove
    mren
    mtools
    mtoolstest
    mv
    od
    paste
    patch
    rcp
    rm
    split
    tee
    touch
    umask
    which
    cp
    whereis
    mcopy
    mshowfat
    lprm
    lpr
    lpq
    rev
    toilet
    aafire
    xeyes
    pv
    yes
    cal
    factor

    rsync
    rsync [OPTION]... SRC [SRC]... DEST
    rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
    rsync [OPTION]... [USER@]HOST:SRC [DEST]

    四个用到正则表达式的重要命令：
    sed
    awk
    grep/ack/ag
    find

# 压缩备份

    tar
    zip

# 磁盘管理

    df # 查看文件系统信息
    $ df -h

    du
    $ du -h

    dd
    fsck
    fdisk
    sync

# 设备管理

    setleds
    loadkeys
    dumpkeys
    MAKEDEV

***

# 网络管理

    telnet
    ping # 用于确定网络的连通性
    ifconfig # 查看TCP/IP设置
    arp # 用于确定IP地址的网卡物理地址
    route # 操作路由表的命令：
    nslookup # 查询IP地址和对应的域名
    ethtool # 查询网络设备信息

    netstat #查看当前网络状态
    netstat -anp    # 查看哪些端口是打开的．
    sudo netstat -anp | grep port # 查看端口是否被使用

    lsof #
    lsof -i # 查看
    sudo lsof -i :port # 查看端口是否被使用

    tcpdump
    wget
    iptables
    virsh

    # 在Network里面研究的几个常用命令
    curl(参考network-http)
    ftp(参考network-ftp)
    snmp(参考network-snmp)
    ssh/scp/sftp(参考network-ssh)
