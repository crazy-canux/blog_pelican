Title: Vagrant
Date: 2017-01-12 21:00:01
Tags: Vagrant



# Vagrant

构建在虚拟化技术之上的虚拟机运行环境管理工具．

适合用来构建和分发开发环境．通过命令行可以批量自动化，不用一个一个安装配置图形界面的虚拟机．

<https://github.com/mitchellh/vagrant>

需要安装virtualbox或vmware等虚拟机.

vagrant还支持其它的providers(docker, vmware, hyper-v, aws)

可以在这里找到很多vagrant可用的box:

<https://atlas.hashicorp.com/boxes/search>

***

# 初始化

    $ mkdir -p /home/user/vagrant
    $ cd /vagrant

    $ vagrant init # 生成一个Vagrantfile文件．

    # 相当于直接配置了Vagrantfile.
    $ vagrant init [box-name]

# 添加box

    # 默认从https://atlas.hashicorp.com/boxes/search下载该box.
    $ vagrant box add [[--name ]box-name] hashicorp/precise64

    # 也可以使用下载到本地的box
    $ vagrant box add [[--name ]box-name] /path/to/your.box

    # 也可以使用自己的服务器上的box
    $ vagrant box add [[--name ]box-name] URL

    # 修改Vagrantfile:
    Vagrant.configure("2") do |config|
      config.vm.box = "[box-name]"
    end

# 使用box

    $ vagrant up [box-name]
    $ vagrant up --provider docker/aws/vmware/hyperv/... [box-name]

    $ vagrant ssh
    # 会进入一个vagrant@precise64:~$的环境．
    # /vagrant 是一个和/home/user/vagrant同步的路径．

# 结束使用

    $ vagrant status # 查看box状态
    $ vagrant halt # 关闭box
    $ vagrant reload # 重启box
    $ vagrant suspend
    $ vagrant resume
    $ vagrant provision

    # 会销毁box占用的所有资源，但不删除box.
    $ vagrant destroy

# 管理box

    $ vagrant box list
    $ vagrant box remove

***

# 配置Vagrantfile

    config.vm.box_version = "1.1.0"
    cfg.vm.hostname = "ubuntu.labs"

    # 端口映射, 把主机的端口映射到vagrant的box
    # 访问主机的该端口就是访问vagrant的box
    cfg.vm.network :forward_port, guest: 80, host: 8080

    # 私有网络，只有主机可以访问vagrant的box.
    # 如果多个vagrant的box设定在同一个网段也可以互相访问．
    cfg.vm.network :private_network, ip: "192.168.50.10"

    # 公有网络，vagrant的box和主机使用一样的网络．
    cfg.vm.network :public_network
    cfg.vm.network :public_network, ip: "192.168.1.1"

    cfg.vm.synced_folder "/var/tmp/pkg-build", "/var/tmp/pkg-build"

***

# 打包

用户可以打包自己的开发环境，然后分发出去．

    $ vagrant package [options] [name]
    $ vagrant package

***

# windows

在windows物理机安装virtualbox和vagrant.

windows不支持ssh,所以需要类似于putty这种客户端．

    host: 127.0.0.1
    port: 2222
    user: vagrant/root
    password: vagrant

# linux

只能在linux物理机安装virtualbox和vagrant使用．

如果想在windows物理机里面的virtualbox上安装的linux系统中使用vagrant会报错：

    # default: Warning: Connection timeout. Retrying...

因为需要在linux上在安装virtualxo，然后不能设置加速．

![Pic](/images/vagrant.PNG)

![Pic1](/images/vagrant1.PNG)

# Q&A

1. vagrant怎样打包ESXi上的虚拟机．

2. vagrant能否打包cluster(virtualbox或esxi)
