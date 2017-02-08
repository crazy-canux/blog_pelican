---
layout: post
title: Tivoli之ITM
comments: true
date: 2016-04-20 13:57:31
updated:
tags:
- ITM
- IBM
- Tivoli
- Monitoring
categories:
- Operation
- Tivoli
permalink:
---

# ITM

ITM: IBM Tivoli Monitoring

是IBM的Cloud & Smart Infrastructure监控解决方案。

Architecture Overview:

![pic](/images/tivoli.png)

ITM主要由管理组件和可选组件组成。

Tivoli Management Services:
1. TEMS
2. TEPS
3. TEP client
4. Historical data collection(warehouse agent)
   * warehouse proxy
   * summarization and pruning agent
5. OS agent

Optional components:
1. Dashboard Application Services Hub
    * Tivoli Monitoring dashboards(Infrastructure Management Dashboards for Servers)
    * Tivoli Common Reporting
    * Tivoli Enterprise Monitoring Automation Server
2. Tivoli Event Synchronization component
3. Authorization Policy Components(tivcmd)

<http://www.ibm.com/support/knowledgecenter/SSTFXA_6.3.0/com.ibm.itm.doc_6.3/welcome_63.htm>

## 安装ITM

Windows: C:\IBM\ITM

Linux/Unix: /opt/IBM/ITM

分为本地安装和分布式安装。

1. 需要先为TEPS和TDW安装DB(ODBC/JDBC)。

    DB2

    MSSQL

    Oracle

2. 在windows/linux/unix安装ITM framework

    TEMA

    Warehouse Proxy agent

    Summarization and Pruning agent

    Tivoli performance Analyzer

    TEMS

    TEPS

    TEPD

    TEMAS

3. 安装agent

    安装操作系统的agent：

    monitoring agent for your OS。

    安装数据库的agent：

    TEMA/TEMS/TEPS同时勾选DB的agent。

    安装agent builder的agent。

<http://www-933.ibm.com/support/fixcentral/swg/downloadFixes?parent=ibm%2FTivoli&product=ibm/Tivoli/IBM+Tivoli+Monitoring&release=All&platform=All&function=fixId&fixids=6.3.0-TIV-ITM-FP0005&includeRequisites=1&includeSupersedes=0&downloadMethod=http>

...

# TEMS

TEMS:  Tivoli Enterprise Monitoing Server

TEMS分为remote和hub，remote最后都汇总到hub。

HTEMS: Hub Tivoli Enterprise Monitoring Server

RTEMS: Remote Tivoli Enterprise Monitoring Server

一个TEMS建议管理700个agent

# TEMA

TEMA: Tivoli Enterprise Monitoring Agent

安装agent之后通过GUI工具Tivoli Enterprise Monitoring Service来配置和启动agent。

也可以通过命令行来配置和启动agent。

agent配置需要指定HTEMS服务器。

## Agentless

TEMS -> Agentless server -> servers

就是用一个中间服务器通过snmp等协议来监控不需要安装agent的被监控服务器。

一个agentless可以设置10个实例(操作系统)，一个实例可以监控100个节点(被监控服务器)。

Agentless OS agents:
1. Agentless Monitoring for AIX OS - SNMP
2. Agentless Monitoring for HP-UX OS - SNMP
3. Agentless Monitoring for Linux OS - SNMP
4. Agentless Monitoring for Solaris OS - SNMP,CIM-XML
5. Agentless Monitoring for Windows OS - SNMP,WMI

## Agent

TEMS -> servers(agent)

一个agent连2个TEMS,一个primary，一个backup。

agent分为：

1. Operating System agent
2. specialized agent
3. Application agent

OS agent：
1. Windows
2. Unix
3. Linux
4. IBM i5/OS

specialized agent：
1. warehouse proxy agent
2. warehouse summarization and pruning agent
3. Log file agent
4. System p® agents (AIX Premium, CEC Base, HMC Base, VIOS Premium)
5. Systems Director base agent
6. Tivoli zEnterprise® Agent
7. Performance Analyzer

# TEPS+DB

TEPS: Tivoli Enterprise Portal Server

使用MTEMS来配置TEPS,添加DB。

# TEPD(TEP client)

TEP -> TEPS

TEP: Tivoli Enterprise Portal client

TEP是GUI界面，分为：
1. Desktop
2. Browser
3. JavaWS: java web start

需要安装IBM的java，在C:\Program Files\IBM\Java70。

使用TEP来查看监控结果。

默认用户是sysadmin, 需要为TEPD指定TEPS服务器。

1. Browser版本

        http://<TEPS Server>:15200/cnp.html

2. Desktop版本

        http://<TEPS Server>:15200/tep.jnlp

    安装ITM可以选择安装桌面版,也可以从Java Web Start获取桌面版。


3. Java Web Start版本

    结合了desktop和browser的优点,从web下载，在桌面运行。

TEP的结构：

* Navigator view

    Enterprise

    Operating Platform(操作系统类型)

    Node(一台服务器一个节点)

    Agent(一个节点上的agent)

    Situation(一个agent上的situation)

    Event(一个situation有多个event)

    Attribute group(相同的Situation是一个group)

* Navigator workspace

    每个view项目都有一个默认的workspace。

...

# History data collection(TDW)

TDW: Tivoli Data Warehouse

存储历史数据。支持DB2，Oracle， MSSQL。

也就是将agent收集的数据存到数据库。

## Warehouse Proxy

TDW使用该agent从agents收集和加载数据。

使用MTEMS配置warehouse proxy。

## Summarization and Pruning agent

TDW使用该agent控制数据库大小。

使用MTEMS配置summarization and pruning agent。

# Jazz for Service Management(Visualization)

## Dashboard Application Services Hub(DASH)(visualization services)

## IBM Tivoli Common Reporting(reporting services)

## Registry Services

## Security Services

## Administration Services

## Tivoli Directory Integrator

## IBM HTTP Server

## IBM WebSphere® Application Server

## Web Server Plug-ins for IBM WebSphere Application Server

...

# Management

管理所有组件一般使用GUI叫manage tivoli monitoring services

windows/linux/unix都可以用GUI。

也可以使用CLI（命令行）,见后文.

一般使用GUI来启动、停止和配置组件。

# CLI

Command Line Interface

## tacmd

支持windows/linux/unix。

/opt/IBM/ITM/bin/tacmd

C:\IBM\ITM\BIN\tacmd

查看tacmd手册：

    ./tacmd help
    ./tacmd ?

登陆和登出HTEMS:

    ./tacmd login -s [PROTOCOL://]HOST[:PORT] -u [USERNAME] -p [PASSWORD] -t [TIMEOUT]
    ./tacmd logout

登陆和登出TEPS：

    ./tacmd tepsLogin -s [TEPS_HOSTNAME] -u [USERNAME] -p [TEPS_PASSWORD] -t [TIMEOUT] -i [IGNORE]
    ./tacmd tepsLogout

管理agent：

    ./tacmd startAgent/stopAgent/restartAgent/viewAgent/updateAgent ...

刷新Netcool/OMNIbus：

    ./tacmd refreshTECinfo {-t|--type} {eif|maps|attr|all}

## itmcmd

用于Linux/Unix系统的命令

/opt/IBM/ITM/bin/itmcmd

查看itmcmd手册：

    ./itmcmd help
    ./itmcmd ?

启动或停止TEMS:

    ./itmcmd server [-options] {start|stop} tems_name

启动或停止agent：

    ./itmcmd agent [-options] {start|stop} {pc ...|all}

启动MTEMS:

    ./itmcmd manage &

## tivcmd

...

# Advanced Administration

## Queries(query editor)

DB agent -> normal way to get data source from database servers.

ODBC -> get data source from windows database

JDBC -> get data source from linux/unix database

## Advanced link topics

Simple link:

Just used to navigate portal workspaces without using the navigator.

Advanced link:

Can be used to manipulate data that is displayed in the target workspace.

## Advanced situation techniques(situation editor)

## Agent autonomy

## Policy(workflow editor)

## Agentless monitoring

TEPS -> Agentless Monitoring Serve -> Servers

## Agent Managent Services(AMS)

