Title: Hive
Date: 2017-04-24 22:57:37
Tags: Hadoop, Hive



# Hive

<https://github.com/apache/hive>

<http://hive.apache.org/>

Hive2数据仓库用于读取，写入和管理使用SQL的大型分布式数据集．

hive2的client: beeline(hive命令的升级版)

***

# hive/beeline

hive

    $ hive --help

beeline

    $ beeline --silent=true
    beeline> !connect jdbc:hive2://[ip]:[port]/[database] [username] [password]

    $ beeline -u "jdbc:hive2://[ip]:10000[/database]" -n [username] -p [password] -e "USE [database]; ..."

***

# sql

normal table:

    > create table tablename (var type, var1 type1);

parquet table:

    > create table {table_name} (var type, var1 type1) STORED AS PARQUET;

partition table:

    > create table {table_name} (var type, var1 type1) PARTITION BY (var2 type2);
    > insert into {table_name} PARTITION (var2 = {pid}) VALUES {values};

parquet partition table:

    > create table {table_name} (var type, var1 type1) PARTITIONED BY (var2 type2) STORED AS PARQUET;
    > insert into {table_name} PARTITION (var2 = {pid}) VALUES {values};
