Title: Hadoop
Date: 2016-04-11 22:57:37
Tags: Hadoop



# Hadoop

<https://github.com/apache/hadoop>

apache hadoop是一个框架，允许使用简单的编程模型在大量计算机上对大型数据集进行分布式处理．

hadoop1只有HDFS和MapReduce两个模块，hadoop2开始分为HDFS, YARN, MapReduce三个模块．

hadoop的版本:

* apache hadoop
* hortonworks hadoop (HWX)
* cloudera hadoop (CDH)

# 安装hadoop

hadoop有三种安装模式：

* 单节点模式
* 伪分布式模式
* 分布式模式

参考Linux Admin和Network SSH如何安装多台centos，并且配置局域网，让本地多台机器相互访问．

一个cluster搭建完成后可以安装hadoop.

下载hadoop的二进制安装包，然后放到/home/hadoop/目录下并解压．

设置环境变量：

    $ vim ~/.bash_profile
    export HADOOP_HOME=/home/hadoop/hadoop-3.0.0-alpha2
    export PATH=$HADOOP_HOME/bin:$PATH

修改配置文件：

    $ cd hadoop-3.0.0-alpha2/etc/hadoop
    $ vim core-site.xml

    $ vim hdfs-site.xml

    $ vim mapred-site.xml

    $ vim yarn-site.xml

格式化hadoop文件系统：

    $ hdfs namenode -format

***

# Hadoop common

支持其它模块的常用工具．

***

# HDFS

Hadoop Distributed File System: hadoop分布式文件系统

# YARN

Yet Another Resource Negotiator: 作业调度和集群资源管理的框架．

# Map-Reduce

一种基于YARN的大型数据并行处理系统．

