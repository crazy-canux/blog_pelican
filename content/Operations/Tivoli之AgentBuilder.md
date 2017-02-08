---
layout: post
title: Tivoli之AgentBuilder
comments: true
date: 2016-04-25 10:19:28
updated:
tags:
- ITM
- IBM
- Tivoli
- Monitoring
- Agent Builder
categories:
- Operation
- Tivoli
permalink:
---

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

