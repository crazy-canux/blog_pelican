Title: Monitoring old
Date: 2016-05-18 19:23:25
Tags: Monitoring, Nagios ,Naemon ,Icinga ,Shinken ,Centreon, Opsview, Check_mk



# **Monitoring**

My monitoring project on github:

<https://github.com/crazy-canux/awesome-monitoring>

***

# **Nagios**

For more informations, see here:

<http://canuxcheng.com>

***

# Naemon

<http://www.naemon.org/>

<https://github.com/naemon>

## Distribution

Naemon can use the same addons as nagios to do the distribution
monitoring.

## Naemon-core

Naemon is 100% Nagios compatible and written in C.

The next generation of nagios.

<https://github.com/naemon/naemon-core>

## Naemon-Livestatus

Event broker, fork from MK_livestatus.

<https://github.com/naemon/naemon-livestatus>

## Thruk

Dashboard.

***

# Icinga

<https://www.icinga.org/>

<https://github.com/Icinga>

<https://exchange.icinga.org/>

## Icinga2

Based on nagios and written in C++.

<https://github.com/Icinga/icinga2>

## IDOUtils

Event broker.

## Icingaweb2

Dashboard.

<https://github.com/Icinga/icingaweb2>

***

# Shinken

<http://www.shinken-monitoring.org/>

<https://github.com/naparuba/shinken>

<https://github.com/shinken-monitoring>

## Shinken(core)

Shinken is nagios compatible monitoring framework, written in python.

<https://github.com/naparuba/shinken>

## mod livestatus

Event broker.

<https://github.com/shinken-monitoring/mod-livestatus>

## mod webui

<https://github.com/shinken-monitoring/mod-webui>

Dashboard

***

# Centreon

<https://www.centreon.com>

<https://github.com/centreon>

<https://github.com/centreon/centreon-plugins>

## centreon engine

Centreon is monitoring scheduler and written in C++.

<https://github.com/centreon/centreon-engine>

## centreon broker

Event broker。

<https://github.com/centreon/centreon-broker>

## centreon(web)

Dashboard.

<https://github.com/centreon/centreon>

***

# Opsview

<https://www.opsview.com/>

## opsview core

Extend from nagios core, written in perl.

<https://www.openhub.net/p/opsview>

***

# check_MK

> Welcome to the official Homepage of Check_MK. Check_MK is comprehensive IT monitoring solution in the tradition of Nagios.

check_Mk有两个版本：
1. Raw edition(开源版本)
2. Enterprise edition(商业版本)

check_Mk是基于agent的，需要在被监控机器上安装agent。

check_MK包括mk livestatus等组件。

<http://mathias-kettner.com/check_mk.html>

<http://git.mathias-kettner.de/git/?p=check_mk.git;a=tree>

<http://mathias-kettner.com/check_mk_exchange.php?HTML=yes>

![pic](/images/mkdis.PNG)

## check_MK macro core

是nagios core的升级版，用python写的。

![pic](/images/check_mk.PNG)

## MK livestatus

Event broker,是NDO/IDO的升级版,不需要数据库。

支持：
1. mk Multisite
2. thruk
3. nagvis
4. BPI
5. CoffeeSaint
6. RealOpInsight

## install check_mk

安装正确的版本：

    sudo gdebi check-mk-raw-1.2.8p1_0.trusty_amd64.deb

检查是否安装成功：

    omd version

查看帮助：

    omd help

## Use check_mk

需要root权限：

    sudo -i

创建一个site：

    omd create mysite

启动site：

    omd start mysite

切换到site的admin：

    su - mysite

登陆Multisite:

http://HOSTNAME/mysite/

username: omdadmin

password: omd

## WATO

check_mk的GUI配置工具。

1. Install Monitoring Agents on monitoring server

    通过WATO的Monitoring Agents下载check-mk-agent安装到被监控机器上。

2. Activating servers

    通过WATO的Hosts创建一台被监控的server。

3. Activating services

## Multisite

check_mk 的dashboard。

## Use notify and event console

***
