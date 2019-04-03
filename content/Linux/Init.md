Title: Init
Date: 2019-02-03 14:04:05
Tags: Linux, Upstart, Systemd



# Linux Init

linux系统启动的第一个进程,pid=1的进程.

    $ ls -l /sbin/init
    /sbin/init ->   upstart
    /sbin/init -> /lib/systemd/systemd

***

# systemd

sytemd是upstart的替代版本．通过查看/sbin/init指向systemd还是upstart.

service文件位置:

    /etc/systemd/system/***.service
    /lib/systemd/system/*.service
    /usr/lib/systemd/system/*.service

service文件编写:

<http://www.jinbuguo.com/systemd/systemd.service.html>

    [Unit]
    Description=details
    After=containerd.service # 之前启动
    Before= # 之后运行
    Bindsto= #
    Wants=containerd.service # 弱依赖
    Requires= # 强依赖

    [Service]
    Type=simple/notify/dbus/forking/idle/oneshot
    ExecStartPre=
    ExecStart=
    ExecStartPost=
    ExecStop=
    ExecStopPost=
    ExecReload=
    KillMode=node/mixed/process/control-group
    Restart=no/on-success/on-failure/on-abnormal/-on-abort/on-watchdog/always
    RestartSec=3s # 重启之前等待的时间.
    TimeoutSec=  # TimeoutStartSec+TimeoutStopSec

    [Install]
    WantedBy=multi-user.target

systemctl命令:

    # 修改后需要重新加载.service文件
    $ systemctl daemon-reload

    $ systemctl start/stop/status ***
    $ systemctl list-unit-files
    $ systemctl show docker

    # 设置开机自动启动
    $ systemctl enable ***
    $ systemctl disable ***
    $ systemctl is-enabled ***

日志管理:

    $ journalctl -xe ***.servivce

***

# upstart

如果init指向upstart, service如果在/etc/init.d找不到会去/etc/systemd/system找.

    /etc/init.d/***

    $ sudo service *** start/stop/status

    # 设置开机自动启动
    $ update-rc.d *** defaults
    # 取消开机启动
    $ update-rc.d *** remove

***
