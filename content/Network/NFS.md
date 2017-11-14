Title: NFS
Date: 2016-07-28 16:08:54
Tags: NFS



# NFS

NFS: Network File System

安装：

    # 在nfs服务器安装nfs服务
    $ sudo apt-get install nfs-kernel-server
    # 添加共享目录并授权
    $ sudo vim /etc/exports
    /home/user/share *(rw,no_root_squash)
    $ sudo service nfs-kernel-server restart

    # 在nfs客户端安装nfs客户端
    $ sudo apt-get install nfs-common
    # 自动挂载
    $ sudo vim /etc/fstab
    nfs-server-ip:/home/user/share /home/user1/share nfs auto 0 0
    $ sudo mount -a
    # 手动挂载
    $ sudo mount -t nfs nfs-server-ip:/home/user/share /home/user1/share

***
