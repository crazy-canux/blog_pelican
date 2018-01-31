Title: Monitoring Tivoli
Date: 2016-04-20 13:57:31
Tags: Monitoring, ITM



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

***

***

# Agent Builder

IBM Agent Builder agents

windows:

    C:\Program Files(x86)\IBM\AgentBuilder

aix/linux:

    /opt/ibm/AgentBuilder

Data source:
1. JDBC
2. HTTP
3. SOAP
4. Ping
5. Socket
6. Java API
7. WMI
8. Perfmon
9. CIM
10. SNMP
11. JMX
12. command return code
13. output from a script
14. A log file
15. AIX Binary Log
16. windows event log
17. A process
18. A Windows service

# create agent

Every agent have a unique produce code.

Like: k00-k99, k{0-9}{A-Z}.

1. Create the agent in the Agent Builder
    agent information
    data source
    runtime configuration

2. Install and test the agent
    output and install the agent
    config and start agent in MTEMS.
    confirm agent data
    revise and retest as needed

3. Add application support
    create in TEP, including queries, workspaces, situations, and take actions.
    Import application support into agent in Agent Builder.
    Retest the agent and application support

4. Create an installation solution.
    Create solution install package from the agent.
    Create solution install package from the package.
    Run the image on the target location.

# install agent

Three ways to instal the agent.

You must install the TEMS and TEPS support on TEMS(HTEMS) and TEPS server.

1. generate the agent files in an ITM installation on this machine

    通过GUI快速安装，Agent Builder和ITM（TEMS和TEPS）安装在同一台机器上。

2. generate a solution install package

    创建安装镜像来安装，windows的.exe和linux/unix的.bin。

3. create a compressed file so that the agent can be installed on another system

    命令行安装。
    生成一个.zip和一个.tgz文件。
    包括windows的.bat和linux/unix的.sh安装文件

    安装下面三个包(等效方法一）：

        InstallIra.bat/.sh itm_install_location [[-h Hub_TEMS_hostname] -u HUB_TEMS_username -p Hub_TEMS_password]
        InstallIra.bat C:\IBM\ITM -h <HTEMS> -u <username> -p <password> # for windows
        ./InstallIra.sh /opt/IBM/ITM -h <HTEMS> -u <username> -p <password> # for linux

    在被监控机器安装agent:

        installIraAgent.bat/.sh itm_install_location
        installIraAgent.bat C:\IBM\ITM # for windows
        ./installIraAgent.sh /opt/IBM/ITM # for linux

    在TEMS(HTEMS)服务器安装对agent的支持：

        installIraAgentTEMS.bat/.sh itm_install_location [[-h Hub_TEMS_hostname] -u HUB_TEMS_username -p Hub_TEMS_password]
        installIraAgentTEMS.bat C:\IBM\ITM # for local HTEMS windows server.
        ./installIraAgentTEMS.sh /opt/IBM/ITM # for local HTEMS linux server.

    在TEPS服务器安装对agent的支持：

        installIraAgentTEPS.bat/.sh itm_install_location [[-h TEPS_hostname] -u TEPS_username -p TEPS_password]
        installIraAgentTEPS.bat C:\IBM\ITM # for local TEPS windows server.
        ./installIraAgentTEPS.sh /opt/IBM/ITM # for local TEPS linux server.

# config agent

需要为agent指定HTEMS服务器，并重启agent，然后重启TEPD。

可以通过Tivoli Enterprise Monitoring Service来配置和启动，也可以通过命令行。

查看所有agent信息：

    /opt/IBM/ITM/bin/cinfo -i # check the productcode and platformCode.

config agent:

    ./itmcmd config -A productcode

start agent:

    ./tacmd agent start productcode

# uninstall agent

1. uninstall from commandline.

    windows:

        cd ITM_INSTALL/TMAITM6
        cd C:\IBM\ITM\TMAITM6_x64
        kxx_uninstall.vbs ITM_INSTALL
        K<product code>_uninstall.vbs C:\IBM\ITM

    linux/unix:

        /opt/IBM/ITM/bin/uninstall.sh [-f] [-i] [-h install_dir] productcode platformCode

2. Remove from TEP client(clear offline entry)

# Monitoring windows resources

1. Windows Management Instrumentation(WMI)

2. Windows Performance Monitor(Perfmon)

3. Windows Event Log

# Monitoring process and command return codes

1. Monitoring process

2. Monitoring command return code

# Monitoring custom data sources

1. Monitoring script output

2. Monitoring log file

# Monitoring remote resources

1. Monitoring SNMP

2. Monitoring CIM

3. Moitoring JMX

***

***

# Netcool/OMNIbus

IBM Tivoli Netcool/OMNIbus

TEC: Tivoli Enterprise Console, 已经被Netcool/OMNIbus替代。

windows:

    C:\Program Files(x86)\IBM\NCOhome

linux/aix:

    /opt/IBM/NCOhome

Browser版本需要安装IBM的JRE，在C:\Program Files\IBM\Java70。

# EIF

EIF: Event Integration Facility
