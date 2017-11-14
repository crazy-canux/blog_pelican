Title: Samba
Date: 2016-04-03 14:46:19
Tags: Network, Samba



# SMB/CIFS

SMB/CIFS占用TCP和UDP的139和445端口。

SMB: server message block.

CIFS: common internet file system, 是SMB的升级版本。

# Samba

Samba: Linux/Unix上的SBM/CIFS,用于跨平台的共享。

安装:

    $ sudo apt-get insall samba

配置：

    $ vim /etc/samba/smb.conf
    [shared]
    comment = share this folder
    path = /home/canux/Share
    public = yes
    guest ok = yes
    browsable = yes
    writable = no
    read only = yes

重启：

    $ sudo service smbd restart

windows访问：

    \\ip\folder

linux访问：

    connect to server -> smb://ip/folder
