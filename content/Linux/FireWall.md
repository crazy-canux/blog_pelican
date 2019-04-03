Title: FireWall
Date: 2016-03-31 21:48:59
Tags: Linux, FireWall



# Firewall

UFW: linux防火墙配置工具，底层还是调用iptables.

filewall: centos的防火墙命令, 底层还是调用iptables.

***

# SELinux

Security-Enhanced-Linux

本地安全

***

# Netfilter

网络安全

***

# iptables

通过iptables操作Netfilter实现应用层安全.

table:

    filter 默认表
    nat
    mangle

chain;

    INPUT
    FORWARD
    OUTPUT

iptables命令:

    -L/--list  [chain [ rulenum]]
    -S/--list-rules [chain [rulenum]]
    -Z/--zero [chain [rulenum]]

    -A/--append chain
    -C/--check chain
    -N/--new chain

    -X/--delete-chain [chain]
    -F/--flush [chain]

    -R/--replace chain rulenum
    -D/--delete chain [rulenum]
    -I/--insert chain [rulenum]

    -P/--policy chain target

    -E/--rename-chain old-chain new-chain

options:

    [!] -p/--protocol
    [!] -s/--source
    [!] -d/--destination
    [!] -o/--out-interface
    [!] -i/--in-interface
    [!] -f/--fragment
    --line-number  # 显示rulenum
    --dport   destination-port
    --sport    source-port
    -m/--match
    -j/--jump
    -v/--verbose
    -t/--table   filter/nat/mangle

others:

    # 保存规则
    iptables-save > firewall.txt
    # 加载规则
    iptables-restore firewall.txt

开机启动:

    iptables-save > /etc/iptables.rules
    vim /etc/network/if-pre-up.d/iptables
    #!/bin/bash
    iptables -F
    iptables -X
    iptables -t nat -F
    iptables -t nat -X
    iptables-restore /etc/iptables.rules

