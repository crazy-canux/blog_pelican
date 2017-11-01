Title: Ansible
Date: 2017-01-12 21:05:48
Tags: Ansible



# Ansible

<https://github.com/ansible/ansible>

<http://www.ansible.com.cn/index.html>

ansible通过SSH来远程管理Linux/Unix机器．

ansible通过winrm+powershell来远程管理Windows机器．

安装:

    $ sudo pip install ansible
    $ sudo apt-get install ansible
    $ sudo yum install ansible

配置：

参考Network-SSH实现从controller到所有node的无密码登陆

配置文件执行顺序:

    ANSIBLE_CONFIG
    ansible.cfg
    .ansible.cfg
    /etc/ansible/ansible.cfg

# ansible命令

ansible运行命令的两种方式：
1. Ad-hoc相当于直接运行shell命令
2. playbooks相当于运行shell脚本

ansible:

    $ansible --help
    -m MODULE_NAME, --module-name=MODULE_NAME # 执行模块，默认是command
    -M MODULE_PATH, --module-path=MODULE_PATH # 指定模块的路径
    -a MODULE_ARGS, --args=MODULE_ARGS # 模块的参数
    -i INVENTORY, --inventory INVENTORY # 默认/etc/ansible/hosts, 需要指定hosts分组
    -f FORKS, --forks=FORKS # 指定并发进程的数量
    -b, --become
    --become-method=BECOME_METHOD # sudo(default)/su/pbrun/pfexec/runas/doas
    --become-user=BECOME_USER # root(default)
    -K, --ask-become-pass
    --list-hosts
    $ ansible -u username -b # 从username sudo到root
    $ ansible -u userA -b --become-user userB # 从userA sudo到userB

    # all表示用于/etc/ansible/hosts中定义的所有的远程主机组
    $ansible all -m ping
    $ansible all -a 'echo $USER'

***

# inventory

    $ sudo vim /etc/ansible/hosts

***

# module

module也就是所说的task plugins/library plugins.

    $ ansible-doc -l/--list #　查看所有已经安装的模块

commands modules：

    command # 默认模块，用于在远程机器上执行命令
    shell # 和command相同，只是该模块支持管道
    raw # 和command相同
    expect
    script
    telnet

files modules:

    copy src dest
    synchronize src dest

package modules:

    apt name/deb state=present/absent/latest/build-dep update_cache autoclean autoremove
    apt_repository repo state=present/absent
    apt_rpm pkg state=present/absent
    yum name state=present/absent/latest/installed/removed

***

# playbooks

playbook的格式是YAML.

    $ ansible-playbook playbook.yaml -K -vvv > output.txt
    -i INVENTORY, --inventory INVENTORY # 默认/etc/ansible/hosts, 在playbook中指定hosts分组，而不是命令行
    -C, --check
    --syntax-check
    --list-tags
    --list-tasks

become:

    become: true
    become_user: root
    become_method: sudo
    become_flags:

debug:

    strategy: debug
