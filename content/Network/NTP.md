Title: NTP
Date: 2016-07-28 16:08:54
Tags: Network, NTP



# NTP

NFS: Network Time Protocol

UTC: Coordinated Universal Time, 世界统一时间

GMT: Greenwich Mean Time, 格林尼治标准时间, = UTC

CET: Central European Time, 欧洲中部时间, = UTC+1, 下令时=UTC+2

CST: Chinese Standard Time, 中国标准时间, = UTC+8

***

# 时区管理

    $ timedatectl list-timezones # 查看所有时区
    $ sudo timedatectl set-timezone Asia/Shanghai # 设置时区
    $ ls -l /etc/localtime # 应该是一个链接

***

# ntp

安装:

    $ sudo apt-get install ntp

## ntpdate

从目标服务器同步.

    ntpdate -u ip

## ntpstat

    $ sudo apt-get install ntpstat

***

# chrony

ntp的升级版.

