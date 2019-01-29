Title: Libvirt
Date: 2017-04-05 21:47:54
Tags: Virtualization, Libvirt



# Libvirt

支持多种虚拟化平台的库

<https://libvirt.org/>

安装:

    $ sudo apt-get install libvirt-bin (包含virsh命令和libvirtd daemon)

    $ sudo apt-get install libvirt-dev # 库, python/go client依赖该库

    $ sudo apt-get install virt-manager # windows管理工具

    $ sudo apt-get install virt-view # ...

    $ sudo service libvirt-bin restart

# virsh

libvirt的命令行工具

    $ virsh list --all    # 查看所有虚拟机
    $ virsh list --all --name # 只看domain name.

    $ virsh define /path/to/X.xml    # 从xml配置文件定义一个domain
    $ virsh start     # 启动虚拟机
    $ virsh reboot    # 重启虚拟机

    $ virsh shutdown   # 关闭虚拟机
    $ virsh destroy    # 强制关闭虚拟机
    $ virsh undefine   # 移除虚拟机
    $ virsh vncdisplay # 查看虚拟机的vnc信息，可以通过vnc访问.

    # 批量操作vm
    $ for vm in `virsh list --all --name`; do virsh /destroy/undefine ${vm}; done

***

# libvirt-qemu

libvirt操作qemu/kvm.

本地:

    qemu:///system
    qemu:///session
    qemu+unix:///system
    qemu+unix:///session

ssh远程:

    # 需要enable该用户的ssh权限
    qemu+ssh://user@host:port/system

tcp远程:

    qemu+tcp://host:port/system

    vim /etc/libvirt/libvirtd.conf:
    listen_tls = 0　　　　　　　　　　#禁用tls登录
    listen_tcp = 1　　　　　　　　　  #启用tcp方式登录
    tcp_port = "16509"　　　　　　　#tcp端口16509
    listen_addr = "0.0.0.0"
    unix_sock_group = "libvirtd"
    unix_sock_rw_perms = "0770"
    auth_unix_ro = "none"
    auth_unix_rw = "none"
    auth_tcp = "none"　　　　　　   #TCP不使用认证
    max_clients = 1024　　　　　　  #最大总的连接客户数1024
    min_workers = 50　　　　　　    #libvirtd启动时，初始的工作线程数目
    max_workers = 200　　　　　　 #同上，最大数目
    max_requests = 1000　　　　　
    #最大同时支持的RPC调用，必须大于等于max_workers
    max_client_requests = 200　　 #每个客户端支持的最大连接数

    vim /etc/default/libvirt-bin:
    # Start libvirtd to handle qemu/kvm:
    start_libvirtd="yes"
    # options passed to libvirtd, add "-l" to listen on tcp
    libvirtd_opts="-d -l --config /etc/libvirt/libvirtd.conf"

    $ sudo service libvirt-bin restart
