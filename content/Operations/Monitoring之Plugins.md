---
layout: post
title: Monitoring之Plugins
comments: true
date: 2016-04-08 16:17:39
updated:
tags:
- nagios
- plugin
categories:
- Operation
- Monitor
permalink:
---

# Monitoring Plugins

Nagios/naemon/icinga/shinken/centreon/opsview/sensu

Office project:

<https://github.com/monitoring-plugins>

<https://www.monitoring-plugins.org/>

My plugin project:

<https://github.com/crazy-canux/pymonitoringplugins>

Open source project:

<https://github.com/crazy-canux/awesome-monitoring>

# monitoring-plugins

## negate

设置相反状态

    -o 设置ok对应状态
    -w
    -c
    -u

## check_http

    [-f <ok|warning|critcal|follow|sticky|stickyport>] # 跳转
    -p PORT # http:80, https:443
    -a "USERNAME":"PASSWORD"
    -u PATH
    --ssl=1/-S # https需要ssl
    -s SEARCH
    -e SEARCH,SEARCH...
    -l # 用在-r或-R前面,表示可以在多行进行正则匹配
    -r # 正则匹配
    -R # 大小写不敏感的正则匹配
    -C # 检查证书, 不检查URL
    -t # timeout.
    -w # warning response time
    -c # critical response time

***

# Windows monitoring

* check_wmi_plus.pl

        IgnoreMyOutDatedPerlModuleVersions
        -m checkfolderfileage -a 'C:' -o '/tmp' -inc _FileAge=@0:1000 -c 10
        -m check_file_count -a 'F:' -o '/folder'

* check_snmp_win_services.pl

    查windows的service

        -n <name>[,<name2>]... # 指定service名字，默认大小写不敏感,正则匹配，逗号分隔多个service，用display name。
        -N=<n> # 匹配到service数量大于n就报错
        -r # 精确匹配

* check_smb_shares.pl

# Linux/Unix monitoring

* check_hpasm.pl

# OS X monitoring

* OSX-Monitoring-Tools

# Vitual Machine monitoring

* check_wmware_api.pl

* check_vmware_esx.pl

# DB monitoring

* check_mysql_health.pl

* check_oracle_health.pl

* check_db2_health.pl

* check_mssql_health.pl

        --name database/sql

# Network monitoring

* check_nwc_health.pl

# Storage monitoring

* check_snmp_storage.pl

    返回用了多少空间。

* check_disk

    返回剩余多少空间。

# Log monitoring

* check_logfiles.pl

* check_events.pl

# Process monitoring

* check_snmp_process.pl

        -n <name> # process名字，大小写敏感，正则匹配，windows需要用processname.exe
        -r # 精确匹配
        -w minW, maxW
        -c minC, maxC # minC <= minW < maxW < maxC

# Application monitoring

* check_sap_health.pl

* check_mailbox_health.pl

***

# Monitoring插件开发

Nagios Plugin API:

<https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/pluginapi.html>

Developing Plugins For Use With Embedded Perl:

<https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/epnplugins.html>

Nagios plugin development guidelines:

<https://nagios-plugins.org/doc/guidelines.html>

Monitoring Plugin Development Guidelines:

<https://www.monitoring-plugins.org/doc/guidelines.html>

Nagios不是基于agent的，所以插件都是通过协议来获取监控信息。

plugin需要遵守下面规则：
1. 至少输出一行文本到STDOUT
2. 事件状态由插件的返回码决定

返回码：

    0： OK（绿色）
    1： Warning（黄色）
    2： Critical（红色）
    3： Unknown（深黄色）


阀值：

    10    |    <0 or >10 alert
    10:    |    <10 alert
    ~:10    |    >10 alert
    10:20    |    <10 or >20 alert
    @10:20    |    >=10 and <=20 alert

***

# check_MK插件开发
