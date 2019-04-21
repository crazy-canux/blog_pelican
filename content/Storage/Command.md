Title: Storage Command
Date: 2019-03-31 21:51:25
Tags: Storage, Linux, Windows



# sysstat:

    # <https://github.com/sysstat/sysstat>
    $ sudo apt-get install sysstat
    # 包括 iostat/mpstat/pidstat/tapestat/cifsiostat

    # 查看diskio信息
    $ sudo iostat

# iotop

    # 查看进程的diskio
    $ sudo apt-get install iotop
    $ sudo iotop

# df

df计算文件系统磁盘空间使用:

    df
    $ df -h

    # 查看目录信息(读写哪个设备)
    $ df /path/folder

# dd

dd转化并拷贝文件:

    dd

# fsck

fsck检查并修复文件系统:

    fsck

# fdisk

fdisk管理磁盘分区表:

    fdisk
    fdisk -l

    fdisk /dev/sda # 可以创建新的磁盘分区
    > n ...    创建新的分区
    > t (8e表示linux LVM), 修改分区类型
    > w 保存修改
    partprobe /dev/sda # 在不重启的情况下保存分区

# parted

大存储分区工具,比如nas,raid.

# mkfd

mkfs:

    mkfs [options] [-t type fs-options] device [size]
    mkfs.ext4 /dev/sdb1 # 将分区格式化成ext4格式.

# mount

相关文件:

    /etc/fstab
    /etc/mtab

    查看磁盘的uuid, 通过uuid挂载
    ls -l /dev/disk/by-uuid

mount/umount挂载文件系统:

    mount # 查看所有挂载信息

    mount -t type -o option device dir

    # 将目录挂载到指定磁盘分区
    mount -t ext4 /dev/sdb1 /opt
    等效修改/etc/fstab
    /dev/sdb1 /opt ext4 defaults 0 0

    # 将目录挂在到内存上.
    mount -t tmpfs -o size=100G tmpfs /var/www

    # 本机挂载, 将本机的folder2挂载到folder1, folder2中原有的内容会隐藏.
    mount --bind /path/folder1 /path/folder2
    /path/folder1 /path/folder2 none bind 0 0

    umount
    umount device/dir

# 磁盘管理

    # 先创建linux lvm分区
    pvcreate <pv-name> # 创建物理卷PV
    pvdisplay
    vgextend <vg-name> <pv-name>  # 给物理卷创建卷组VG
    vgdisplay
    lvextend -r -l +100%FREE <lv-path> # 将物理卷上的空闲空间全部放到逻辑卷LV上
    lvdisplay

sync同步缓存写入固态存储:

    sync

查看所有硬件设备:

    lshw # 列出硬件
    lshw -class disk # 查看磁盘设备

设备管理:

    lspci # 列出所有PCI设备

    lsusb # 列出USB设备

    lsblk # 列出块设备

    setleds

    loadkeys

    dumpkeys

    MAKEDEV

***

# IOPS

磁盘IO.

安装fio:

    $ sudo apt-get install fio

测试随机读写的IO:

    $ fio -filename=/dev/sda1 -direct=1 -iodepth 1 -thread -rw=randrw
    -rwmixread=70 -ioengine=psync -bs=16k -size=200G -numjobs=30 -runtime=100
    -group_reporting -name=mytest


