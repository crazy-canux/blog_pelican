Title: Hadoop HDFS
Date: 2016-04-11 22:57:37
Tags: Hadoop, HDFS



# HDFS

Hadoop Distributed File System: hadoop分布式文件系统

hadoop hdfs分为三部分:

master NameNode -> JobTracker

secondary NameNode

DataNode -> TaskTracker

hdfs命令的三种方式:

    $ hadoop fs  # 本地文件系统和hdfs文件系统都能用
    $ hadoop dfs
    $ hdfs dfs
