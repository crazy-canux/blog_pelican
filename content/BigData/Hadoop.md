Title: Hadoop
Date: 2016-04-11 22:57:37
Tags: Hadoop



# Hadoop

<https://github.com/apache/hadoop>

apache hadoop是一个框架，允许使用简单的编程模型在大量计算机上对大型数据集进行分布式处理．

hadoop1只有HDFS和MapReduce两个模块，hadoop2开始分为HDFS, YARN, MapReduce三个模块．

hadoop的版本:

* apache hadoop
* hortonworks hadoop (HDP)
* cloudera hadoop (CDH)
* mapr
* transwarp

# 安装hadoop

hadoop有三种安装模式：

* 单节点模式
* 伪分布式模式
* 分布式模式

参考Linux Admin和Network SSH如何安装多台centos，并且配置局域网，让本地多台机器相互访问．

下载hadoop的二进制安装包，然后放到/home/hadoop/目录下并解压．

推荐的cluster node:

    NameNode(hdfs)
    Secondary NameNode(hdfs)
    DataNode(hdfs)
    ResourceManager server(yarn)
    NodeManager server(yarn)
    WebAppProxy server(yarn)
    MapReduceJobHistory server(mapreduce)

设置环境变量：

    $ vim ~/.bash_profile
    export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-.../jre
    export HADOOP_HOME=/home/hadoop/hadoop-3.0.0-alpha2
    export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$PATH
    $ source ~/.bash_profile

修改hadoop的环境变量：

    $ cd hadoop-3.0.0-alpha2/etc/hadoop
    $ vim hadoop-env.sh
    export JAVA_HOME='/usr/lib/jvm/java-1.8.0-openjdk-.../jre

    # 测试java和hadoop的环境是否可用：
    $ hadoop

分布式环境搭建：

<http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html>

    $ vim core-site.xml

    $ vim hdfs-site.xml # namenode, datanode

    $ vim yarn-site.xml # resourcemanager, nodemanager, webappproxy

    $ vim mapred-site.xml # mr application, mr jobhistory

    # slaves file
    $ vim workers
    namenode
    secondnamenode
    datanode
    datanode2
    yarnserver
    mjhserver

    # hadoop rack awareness

    # logging
    $ vim log4j.properties

CLI for hadoop cluster:

启动一个hadoop　cluster需要同时启动hdfs和yarn, 推荐用单独的用户分别启动这两个组件．

    # 第一次启动hdfs，需要格式化hdfs
    $ hdfs namenode -format <cluster_name>

    # 启动hdfs namenode 和　datanode
    $ hdfs --daemon start namenode
    $ hdfs --daemon start datanode
    # 如果ssh已经实现无密码连接，可以一次启动cluster的所有node
    $ $HADOOP_HOME/sbin/start-dfs.sh

    # 启动yarn resourcemanager　和　nodemanager
    $ yarn --daemon start resourcemanager
    $ yarn --daemon start nodemanager
    # 如果配置了slaves file 并且cluster node实现ssh无密码登陆，可以一次启动
    $ $HADOOP_HOME/sbin/start-yarn.sh

    # 启动webappproxy server
    $ yarn --daemon start proxyserver

    # 启动MapReduce Jobhistory server.
    $ mapred --daemon start historyserver

    # stop namenode
    $ hdfs --daemon stop namenode
    # stop datanode
    $ hdfs --daemon stop datanode
    # stop at the same time
    $ $HADOOP_HOME/sbin/stop-dfs.sh

    # stop resourcemanager
    $ yarn --daemon stop resourcemanager
    # stop nodemanager
    $ yarn --daemon stop nodemanager
    # stop at the same time
    $ $HADOOP_HOME/sbin/stop-yarn.sh

    # stop webappproxy server
    $ yarn stop proxyserver

    # stop jobhistory server
    $ mapred --daemon stop historyserver

GUI for hadoop cluster:

    # namenode
    http://nn:9870
    # resource manager
    http:rm:8080
    # mapreduce job history server
    http://jhs:19888

***

# Hadoop Commands

     hadoop [--config confdir] [--loglevel loglevel] [COMMAND] [GENERIC_OPTIONS] [COMMAND_OPTIONS]

user command:

    $ hadoop archive
    $ hadoop fs
    ...

admin command:

    $ hadoop daemonlog
    ...

***

# fs commands

file system command:

支持本地文件系统，hdfs文件系统，还有其它文件系统．

    $ hadoop fs

    $ hadoop fs -cat URI [URI ...]
    ...

***
