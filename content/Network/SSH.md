Title: SSH
Date: 2016-07-28 15:53:34
Tags: Network, SSH



# OpenSSH

<http://www.openssh.com/>

windows上支持ssh协议的客户端：

* putty
* xshell
* MobaXterm
* secureCRT

安装：

    $ sudo apt-get install openssh-server

***

# SSH命令

ssh是openssh协议的客户端．

远程操作的命令包括ssh, scp, sftp.

ssh

    $ ssh
    # 远程执行命令需要用双引号，不能用单引号
    $ ssh username@host "command/script"

scp

    $ scp

sftp

    $ sftp

常用选项：

    -C   compression
    # 不需要输入yes来交互, 或者修改/etc/ssh/ssh_config
    -o StrictHostKeyChecking=no
    -o UserKnownHostsFile /dev/null

ssh也包括一些密钥管理的命令.

ssh-keygen

    $ ssh-keygen -t rsa -C 'canuxcheng@gmail.com'

    # 通过将本机的公钥拷贝到远程机器实现无密码访问．
    # 将本机的public-key拷贝到远程机器的authorized_keys.
    $ ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote
    # 另外的拷贝方法
    $ ssh user@host "cat >> ~/.ssh/authorized_keys" < ~/.ssh/id_rsa.pub
    $ sudo service ssh restart # 需要重启ssh服务

    非交互式通过命令行传密码的命令：
    $ sshpass -p [password]

ssh-add

ssh-keysign

ssh-keyscan

***

# 启用root远程ssh

    $ sudo -i
    # passwd root
    # vim /etc/ssh/sshd_config
    > PermitRootLogin prohibit-password
    > PermitRootLogin yes
    # service ssh restart
