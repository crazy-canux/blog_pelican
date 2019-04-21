Title: Ansible
Date: 2017-01-12 21:05:48
Tags: DevOps, Ansible



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

手动配置:

    $ sudo vim /etc/ansible/ansible.cfg
    [defaults]
    ask_pass = False
    host_key_checking = False

# ansible命令

ansible运行命令的两种方式：
1. Ad-hoc相当于直接运行shell命令
2. playbooks相当于运行shell脚本

ansible:

    $ ansible -i inventory group1:group1:group3/all ...

    $ansible --help
    -m MODULE_NAME, --module-name=MODULE_NAME # 执行模块，默认是command
    -M MODULE_PATH, --module-path=MODULE_PATH # 指定模块的路径
    -a MODULE_ARGS, --args=MODULE_ARGS # 模块的参数
    -i INVENTORY, --inventory INVENTORY # 默认/etc/ansible/hosts, 需要指定hosts分组
    -f FORKS, --forks=FORKS # 指定并发进程的数量
    -C, --check
    -D, --diff
    -l SUBSET, --limit=SUBSET
    --syntax-check
    --list-hosts
    -v, --verbose # -v, -vvv, -vvvv

    # 提权选项
    -b, --become
    --become-method=BECOME_METHOD # sudo(default)/su/pbrun/pfexec/runas/doas
    --become-user=BECOME_USER # root(default)
    -K, --ask-become-pass

    # 连接选项
    -u REMOTE_USER
    --ssh-common-args
    --ssh-extra-args
    -T TIMEOUT # default 10s
    -K, --ask-pass

***

# inventory

inventory包括主机和分组,以及主机变量和分组变量.

可以是ini格式，也可以是yaml格式.

    $ sudo vim /etc/ansible/hosts

ini格式:


    定义主机和主机变量
    [host1]
    node1 ansible_connection=ssh ansible_host=host ansible_port=port ansible_user=user ansible_ssh_pass=password

    定义分组和分组变量
    [group1]
    node1
    node2
    [group1:vars]
    ansible_connection=local/smart/ssh/paramiko
    ansible_host=
    ansible_port=
    ansible_user=
    ansible_ssh_pass=
    ansible_ssh_common_args=
    ansible_ssh_extra_args=
    ansible_become=
    ansible_become_method=
    ansible_become_user=
    ansible_become_pass=
    ansible_become_exe=
    ansible_become_flags=

    定义分组的分组
    [big-group:children]
    group1
    group2

yaml:

    all:
      hosts:    # 定义主机和主机变量
        node1:
          ansible_host:
          ip:
          access_ip:
      children:    # 定义分组和分组变量
        group1:
          hosts:
            node1:
          vars:
            proxy:
        group2:
          hosts:
            node2:
        big-group: # 定义分组的分组
          children:
            group1:
              hosts:
                node1:
            group2:
              hosts:
                node2:

***

# module

module也就是所说的task plugins/library plugins.

    $ ansible-doc -l/--list #　查看所有已经安装的模块

commands modules：

    command # 默认模块，用于在远程机器上执行命令
    shell # 和command相同，只是该模块支持管道和特殊字符，一般用来执行脚本和复杂命令
    raw
    expect
    script
    telnet

files modules:

    copy src dest mode ...
    synchronize src dest ...

package modules:

    apt name/deb state=present/absent/latest/build-dep update_cache autoclean autoremove
    apt_repository repo state=present/absent
    apt_rpm pkg state=present/absent
    yum name state=present/absent/latest/installed/removed

***

# adhoc

    $ ansible group -m <module> -a <args> ...

copy:

    $ ansible group -m copy -a "src=/sr dest=/dest mode=0655"

# playbooks

playbook的格式是YAML.

    $ ansible-playbook -i inventory playbook.yaml -K -vvv > output.txt
    -i INVENTORY, --inventory INVENTORY # 默认/etc/ansible/hosts, 在playbook中指定hosts分组，而不是命令行

    - hosts: host-or-group
      remote_user: user

      task:
      - name: task name.
        module: args

variables:

    register: var   # 用var来存储task的结果,查看不同模块的返回值．

become:

    become: true
    become_user: root
    become_method: sudo
    become_flags:

debug:

    strategy: debug

***

# awx

ansible的web管理界面.

<https://github.com/ansible/awx>
