Title: Linux FileSystem
Date: 2016-03-31 21:48:59
Tags: Linux, FileSystem



# VFS

Linux采用虚拟文件系统，支持多个文件系统协议．

***

# ext/ext2/ext3/ext4

# JFS2

# ramfs

linux的VM(虚拟内存)包括ramfs和swap.

对内存的支持

# swap

交换分区，当内存不足，会把内存上暂时不运行的程序保存到swap，获取部分内存空间运行．

# tmpfs

临时文件系统, 优先使用ramfs,　其次使用swap.

    # 挂载tmpfs
    mount -t tmpfs -o size=1024m tmpfs /path/to/mount
    # /etc/fstab　
    tmpfs /dev/shm tmpfs,defaults,size=512m 0 0

# vfat/fat/ntfs

windows文件系统

# cifs/smbfs

# nfs


