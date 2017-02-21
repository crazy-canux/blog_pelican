Title: Shell之外部命令
Date: 2016-03-31 21:51:25
Tags: Linux, Shell, Bash, Zsh, Fish



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

    uname # 打印系统信息
    lsb_release # 查看发行版本信息
    cat /etc/issue #
    cat /proc/version
    getconf # 查询系统配置的变量，LONG_BIT表示系统位数
    cat /proc/cpuinfo # 查看cpu信息
    vmstat # 报告虚拟内存的统计信息
    free # 现实空闲和使用的系统内存
    cat /proc/meminfo # 查看内存信息
    lscpu # 显示cpu架构的信息
    lspci # 列出所有PCI设备
    lsusb # 列出USB设备
    lsblk # 列出块设备
    lshw # 列出硬件

    # sudo apt-get install sysstat
    iostat
    mpstat

# 系统设置

# 文件和目录管理

    mkdir
    tree
    cat

# 文件编辑

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

# 磁盘管理

    df
    du
    dd
    fsck
    fdisk

# 设备管理

    setleds
    loadkeys
    dumpkeys
    MAKEDEV
