Title: Libvirt
Date: 2017-04-05 21:47:54
Tags: Virtualization, Libvirt



# Libvirt

支持多种虚拟化平台的库

<https://libvirt.org/>

安装:

    $ sudo apt-get install libvirt-bin libvirt-dev

# virsh

libvirt的命令行工具

    $ virsh list --all    # 查看所有虚拟机
    $ virsh list --all --name # 只看domain name.

    $ virsh define    # 从xml配置文件定义一个domain
    $ virsh start    # 启动虚拟机
    $ virsh reboot    # 重启虚拟机

    $ virsh shutdown    # 关闭虚拟机
    $ virsh destroy    # 强制关闭虚拟机
    $ virsh undefine    # 移除虚拟机
    # 批量操作vm
    $ for vm in `virsh list --all --name`; do virsh /destroy/undefine ${vm}; done

***
