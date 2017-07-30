Title: Impala
Date: 2017-04-24 22:57:37
Tags: Hadoop, Impala



# Impala

<https://github.com/apache/incubator-impala>

<https://impala.apache.org/>

impala的client: impala-shell

Cloudera公司的CDH集成了Impala.

***

# impala-shell/beeline

impala-shell

    $ impala-shell

beeline

    $ beeline --silent=true
    beeline> !connect jdbc:hive2://[ip]:21050[/database];auth=noSasl [username] [password]

    $ beeline -u "jdbc:hive2://[ip]:21050[/database];auth=noSasl" -n [username] -p [password] -e "USE [database]; ..."

***

# sql

normal table:

    > create table {table_name} (var type, var1 type1);

parquet table:

    > crate table {table_name} (var type, var1 type1) STORED AS PARQUET;

partition table:

    > create table {table_name} (var type, var1 type1) PARTITIONED BY (var2 type2);
    > insert into {table_name} PARTITION (var2 = val2) values (val, val1)

parquet partition table:

    > create table {table_name} (var type, var1 type1) PARTITION BY (var2 type2) STORED AS PARQUET;
    > insert into {table_name} PARTITION (var2 = val2) values (val, val1)
