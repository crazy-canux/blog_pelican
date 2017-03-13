Title: Ansible
Date: 2017-01-12 21:05:48
Tags: Ansible



# Ansible

<https://github.com/ansible/ansible>

<http://www.ansible.com.cn/index.html>

ansible通过SSH来远程管理Linux/Unix机器．

ansible通过winrm+powershell来远程管理Windows机器．

安装:

    $sudo -E pip install ansible

使用:

    $ansible --help
    # windows的内置模块在/usr/share/ansible/windows
    # linux/unix的内置模块在/usr/share/ansible/system
    -m MODULE_NAME, --module-name=MODULE_NAME # 执行本地ansible模块内的命令
    -a MODULE_ARGS, --args=MODULE_ARGS # 执行远程机器上的命令
    -u REMOTE_USER, --user=REMOTE_USER
    -S, --su
    -R SU_USER, --su-user=SU_USER
    -s, --sudo
    -U SUDO_USER, --sudo-user=SUDO_USER

    # all表示用于/etc/ansible/hosts中定义的所有的远程主机组
    $ansible all -m ping
    $ansible all -m shell -a 'echo $USER'

配置文件执行顺序:

    ANSIBLE_CONFIG
    ansible.cfg
    .ansible.cfg
    /etc/ansible/ansible.cfg

ansible运行命令的两种方式：

* Ad-hoc相当于直接运行shell命令
* playbooks相当于运行shell脚本

***

# Ad-Hoc


***

# playbooks

playbook的格式是YAML.

