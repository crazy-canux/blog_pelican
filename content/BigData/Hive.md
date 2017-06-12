Title: Hive
Date: 2017-04-24 22:57:37
Tags: Hadoop, Hive



# Hive

<https://github.com/apache/hive>

<http://hive.apache.org/>

Hive2数据仓库用于读取，写入和管理使用SQL的大型分布式数据集．

hive2的client: beeline(hive命令的升级版)

***

# beeline

    $ beeline --silent
    beeline> !connect jdbc:hive2://[ip]:[port]/[database] [username] [password]

    # jdbc for hive
    $ beeline -u "jdbc:hive2://[ip]:10000[/database]" -n [username] -p [password] -e "USE [database]; ..."
