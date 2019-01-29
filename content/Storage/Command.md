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

# mount

mount/umount挂载文件系统:

    mount
    mount -t type -o option device dir
    mount -t ext4 /dev/sdb1 /var/www
    mount -t tmpfs -o size=100G tmpfs /var/www

    umount
    umount device/dir

# dd

dd转化并拷贝文件:

    dd

# fsck

fsck检查并修复文件系统:

    fsck

# mkfd

mkfs:

    mkfs [options] [-t type fs-options] device [size]
    mkfs.ext4 /dev/sdb1

# fdisk

fdisk管理磁盘分区表:

    fdisk
    fdisk -l

    fdisk /dev/sda # 可以创建新的磁盘分区
    > n ...    创建新的分区
    > t (8e表示linux LVM), 修改分区类型
    > w 保存修改
    partprobe /dev/sda # 在不重启的情况下保存分区

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

设备管理:

    lspci # 列出所有PCI设备

    lsusb # 列出USB设备

    lsblk # 列出块设备

    lshw # 列出硬件

    setleds

    loadkeys

    dumpkeys

    MAKEDEV


