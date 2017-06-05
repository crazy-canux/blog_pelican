Title: SQL On Hadoop
Date: 2017-04-24 22:57:37
Tags: Hadoop, Hive, Presto, Impala, HAWQ



# Hive

<https://github.com/apache/hive>

<http://hive.apache.org/>

Hive2数据仓库用于读取，写入和管理使用SQL的大型分布式数据集．

hive2的client: beeline(hive命令的升级版)

    $ beeline --silent
    beeline> !connect jdbc:hive2://[ip]:[port]/[database] [username] [password]

***

# Presto

<https://github.com/prestodb>

<https://prestodb.io/>

presto的client: presto-cli(rename to presto)

    $ presto --server localhost:8080 --catalog hive --schema default

***

# Impala

<https://github.com/apache/incubator-impala>

<https://impala.apache.org/>

impala的client: impala-shell

***

# HAWQ

<http://hawq.incubator.apache.org/>

<https://github.com/apache/incubator-hawq>

HAWQ是在Pivotal Greenplum和PostgreSQL基础上开发而来．

HAWQ可以通过HDFS在本机快速，交互查询hadoop数据．

hawq的交互式命令行接口, 类似于postgresql, 参考postgresql.

hawq的client: psql (参考postgresql)

***

# Use jdbc connect sql engine on hadoop

    # beeline for hive
    $ beeline -u "jdbc:hive2://[ip]:10000[/database]" -n [username] -p [password] -e "USE [database]; ..."

    # beeline for impala(use hive jdbc driver.)
    $ beeline -u "jdbc:hive2://[ip]:21050[/database];auth=noSasl" -n [username] -p [password] -e "USE [database]; ..."

    # for presto
    $ jdbc:presto://host:port/catalog/schema

    # for impala
    $ jdbc:impala://Host:Port[/Schema];Property1=Value;Property2=Value;...

    # for hawq
    $ jdbc:pivotal:greenplum://hdm1:5432;DatabaseName=getstartdb;User=hdbuser;Password=hdbpass
