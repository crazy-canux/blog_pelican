---
layout: post
title: Monitoring之Nagios
comments: true
date: 2016-03-25 11:15:48
updated:
tags:
- nagios
- monitoring
categories:
- Operation
- Monitor
permalink:
---

# Nagios

> Nagios is the industry standard in IT infrastructure monitoring

> Nagios offers complete monitoring and alerting for servers, switches, applications, and services.

Nagios官方宣称nagios是IT基础监控的工业标准。

Nagios提供对服务器，交换机，应用和服务的完整的监控和警报。

Nagios是无agent的，nagios的plugin通过协议远程获取信息。

<https://www.nagios.org/>

<https://www.nagios.com/>

<https://exchange.nagios.org/>

<https://github.com/NagiosEnterprises>

<https://github.com/nagios-plugins>

***

# Nagios安装配置

## Nagios发展

Nagios core 1.0

Nagios core 2.0

Nagios core 3.0

Nagios XI

Nagios core 4.0

目前nagios有两大阵营：

开源解决方案： Nagios core

商业解决方案： Nagios XI

## Nagios安装配置

安装和配置nagios core,plugins,addons参考

官方文档:

<https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/toc.html>

中文文档：

<http://nagios-cn.sourceforge.net/nagios-cn/index.html>

***

# Nagios开源解决方案

## Nagios core:

>Nagios Core is the monitoring and alerting engine that serves as the primary application around which hundreds of Nagios projects are built.

Nagios core是监控和警报的主引擎，围绕它建立了成千上万的项目。
技术栈是c，只能安装在linux/unix系统。
Nagios core只是一个监控套件，本身没有监控功能，需要插件来完成监控。

<https://www.nagios.org/projects/nagios-core/>

<https://github.com/NagiosEnterprises/nagioscore>

## Nagios plugins:

>Efficient, standalone extensions that provide low-level intelligence for monitoring anything and everything with Nagios Core.

Nagios core的监控插件,也就是官方插件,主要是c、shell和perl。

<https://www.nagios.org/projects/nagios-plugins/>

<https://github.com/nagios-plugins/nagios-plugins>

## Nagios frontends:

>Web interfaces, themes, Windows and Linux interfaces, and mobile apps for Nagios. Change the look and style of Nagios to suite your needs.

Nagios frontends包括了 主题,web接口,移动设备接口。

<https://www.nagios.org/downloads/nagios-core-frontends/>

## Nagios config tools(Nagios addons projects):

>Tools and GUIs for simplifying Nagios Core configuration.

nagios core的组件。

包括Lilac,NagiosQL,NConf,OneCMDB,ignoramus

<https://www.nagios.org/projects/nagios-config-tools/>

<https://www.nagios.org/downloads/nagios-core-addons/>

<https://github.com/NagiosEnterprises>

## Nagios exchange:

>Nagios® Exchange is the central place where you'll find all types of Nagios projects - plugins, addons, documentation, extensions, and more. This site is designed for the Nagios Community to share its Nagios creations.

Nagios exchange是nagios的开源宝库。

包括第三方plugins、addons和docs。

<https://exchange.nagios.org/https://exchange.nagios.org/>

***

# Nagios商业解决方案

## Nagios XI:

>Our most powerful IT infrastructure monitoring and IT monitoring software alerting solution for today’s demanding organizational requirements.

Nagios XI 是现代化的商业监控解决套件。

Nagios XI 使用nagios core 4.0。

Nagios XI 架构：

![pic](/images/nagiosxi.png)

## Nagios network analyzer

## Nagios log server

## Nagios fusion

## Nagios incident manager

***

# Nagios 集中监控

## 本地监控

使用nagios core + plugins只能监控本地的linux/unix机器。

## 远程监控

使用nagios core + plugins + addons可以监控远程的linux/unix/windows机器。

NRPE(for linux)/NRPE_NT(for windows)和check_nrpe, 运行远程机器上的插件, 支持windows/unix/linux:

    nagios core + check_nrpe <=> NRPE/NRPE_NT + plugins

NSCP和check_nt, 只能使用固定的几个命令查基本属性, 支持windows/linux/unix：

    nagios core + check_nt -H <NSCP IP> [-v <command>] <=> NSCP(NSClient++)

NSCP和check_nrpe，可以传自己的命令或插件, 支持windows/linux/unix：

    nagios core + check_nrpe -H <NSCP IP> [-c <command/plugins>] [-a <argument list>] <=> NSCP(NSClient++) + plugins

NSCP和NSCA/NRDP,NSCP主动check,然后将结果发送给NSCA/NRDP:

    nagios core + NSCA <=> NSCP(NSClient++)

NCPA是python写的跨平台代理, 支持linux/windows/unix：

    nagios core + check_ncpa.py <=> NCPA

***

# Nagios 分布式监控

## NRDP/NSCA/NSCA-ng

官方推荐，NRDP是NSCA的升级版,提供被动检测,这种方式效率低，稳定性差。

    nagios core <- plugins <- NSCA <= send_nsca <- ocsp <- Nagios core <=> Hosts
                                   ^
                                  ||
                                  send_nsca <- ocsp <- Nagios core <=> Hosts

***

# Nagios的组件

<https://www.nagios.org/downloads/nagios-core-addons/>

<https://github.com/NagiosEnterprises>

## NDOUtils(NDO)/IDOUtils(IDO)

从nagios导出当前和历史数据到mysql数据库,需要安装数据库。

相似功能有mk livestatus。

N * (Nagios core + NDO module) -> TCP/Socket -> NDO2DB daemon -> DB

<https://github.com/NagiosEnterprises/ndoutils>

## NSTI

Nagios SNMP Trap Interface.

<https://github.com/NagiosEnterprises/nsti>

## BPI

Nagios Business Process Intelligence.

<https://github.com/NagiosEnterprises/nagiosbpi>

# 其它组件介绍

## NCONF

nagios的基于web的配置工具。

<http://www.nconf.org/dokuwiki/doku.php>

<https://github.com/nconf/nconf>

## DNX

分布式组件。

<http://dnx.sourceforge.net/>

<https://sourceforge.net/projects/dnx/>

## Nagiosgraph

> nagiosgraph parses output and performance data from Nagios plugins and stores
the data in RRD files. nagiosgraph creates graphs and generates HTML pages with
graphic reports from the data.

基于RRD，绘制nagios的性能图。

<http://nagiosgraph.sourceforge.net/>

<https://sourceforge.net/projects/nagiosgraph/>

***

# consol的分布式监控方案

一家德国的咨询和解决方案软件公司。

可以通过 check_MK 的omd来安装。

<https://www.consol.de/>

<https://labs.consol.de/index.html>

<https://github.com/ConSol>

主要贡献组件：

<https://github.com/sni>

主要贡献插件：

<https://github.com/lausser>

![pic](/images/nagios.png)

## Mod gearman

labs consol的分布式监控组件, gearman的worker。

<http://www.mod-gearman.org/>

<https://github.com/sni/mod_gearman>

## NDOUtils/livestatus

Event broker.

## Thruk

基于perl的web框架catalyst的dashbord。

<http://www.thruk.org/>

<https://github.com/sni/Thruk>

***

# Op5的分布式监控方案

一家瑞典的监控和解决方案公司。

<https://www.op5.com/>

<https://kb.op5.com/dashboard.action>

<https://github.com/op5>

## merlin

分布式组件。

<https://kb.op5.com/display/MERLIN/Distributed+%28Merlin%29+Home>

<https://github.com/op5/merlin>

## NDOUtils/MK livestatus

Eevent broker

## Ninja

Dashboard.

<https://kb.op5.com/display/GUI/GUI+%28Ninja%29+Home>

<https://github.com/op5/ninja>
