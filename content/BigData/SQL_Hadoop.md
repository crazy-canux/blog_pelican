Title: SQL On Hadoop
Date: 2017-04-24 22:57:37
Tags: Hadoop, Hive, Impala, HAWQ



# Hive

<https://github.com/apache/hive>

<http://hive.apache.org/>

Hive数据仓库用于读取，写入和管理使用SQL的大型分布式数据集．

# Impala

<https://github.com/apache/incubator-impala>

<https://impala.apache.org/>

# HAWQ

<http://hawq.incubator.apache.org/>

<https://github.com/apache/incubator-hawq>

HAWQ是在Pivotal Greenplum和PostgreSQL基础上开发而来．

HAWQ可以通过HDFS在本机快速，交互查询hadoop数据．

# presto

<https://github.com/prestodb>

<https://prestodb.io/>

***

# beeline

    # for hive
    $ beeline -u "jdbc:hive2://[ip]:10000[/database]" -n [username] -p [password] -e "USE [database]; ..."

    # for impala
    $ beeline -u "jdbc:hive2://[ip]:21050[/database];auth=noSasl" -n [username] -p [password] -e "USE [database]; ..."
