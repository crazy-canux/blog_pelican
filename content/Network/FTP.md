Title: FTP
Date: 2016-07-28 16:08:54
Tags: Network, FTP



# FTP

ftp服务器有很多：

1. vsftpd
2. proftpd
3. pyftpdlib

***

# vsftpd

安装vsftpd:

    $ sudo apt-get install vsftpd

windows开启ftp服务和建立IIS站点即可。

linux配置：

    $ vim /etc/vsftpd.conf
    local_root=/home/canux/FTP
    anon_root=/home/canux/FTP
    local_enable=YES
    anonymous_enable=YES
    chroot_local_user=YES
    $ sudo service vsftpd restart

ftp的网页浏览格式：

    ftp://host/path
    ftp://username:password@host:port/path

***

# ftp命令

## ftp

    $ ftp [-46pinegvd] [host [port]]

***

# python的FTP标准库

## ftplib

***
