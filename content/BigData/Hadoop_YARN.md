Title: Hadoop YARN
Date: 2016-04-11 22:57:37
Tags: Hadoop, YARN



# YARN

作业调度和集群资源管理的框架．

yarn的两个组件：

* resourcemanager
* nodemanager

***

# yarn commands

    yarn [--config confdir] COMMAND [--loglevel loglevel] [GENERIC_OPTIONS] [COMMAND_OPTIONS]

user commands:

    $ yarn application
    ...

admin commands:

    $ yarn daemonlog
    ...

***

# resource manager

resource manager由两部分组成：

* scheduler
* applicationmanager

ResourceManager功能：

* 处理客户请求
* 启动／监控applicationmaster
* 监控nodemanager
* 资源分配与调度

ApplicationMaster功能：

* 数据切分
* 为应用申请资源, 并分配给内部任务
* 任务监控与容错

***

# node manager

node manager功能：

* 单个节点的资源管理
* 处理来自resourcemanager的命令

***


