Title: HAWQ
Date: 2017-04-24 22:57:37
Tags: Hadoop, HAWQ




# HAWQ

<http://hawq.incubator.apache.org/>

<https://github.com/apache/incubator-hawq>

HAWQ是在Pivotal Greenplum和PostgreSQL基础上开发而来．

HAWQ也就是Pivotal HDB.

HAWQ和Pivotal　HDB是一个项目．

Hortonworks公司的HDP集成了HAWQ.

HAWQ可以通过HDFS在本机快速，交互查询hadoop数据．

hawq的交互式命令行接口, 类似于postgresql, 参考postgresql.

hawq的client: psql (参考postgresql)

***

# psql

    $ psql
    $ PGPASSWORD='password';psql -h <host> -p <port> -U <username> -d [database] -c "[psql command]"
    $ psql -l # 查看所有database

    # jdbc
    $ jdbc:pivotal:greenplum://hdm1:5432;DatabaseName=getstartdb;User=hdbuser;Password=hdbpass

***

# sql

AO(append only) table:

    > create table {table_name} (var type, var1 type1);

parquet table:

    > create table {table_name} (var type, var1 type2) WITH (appendonly=true, orientation=parquet);

AO table distributed by specified column and partitioned by range:

    > create table {table_name} (var type, var1 type1) distributed by range(var) partition by range(var1) (start val end val1 every val2);

AO table distributed by randomly and partitioned by range:

    > create table {table_name} (var type, var1 type1) distributed randomly partition by range (var) (start(val) end (val1) every(val2));

parquet table distributed by specified column and partitoned by list:

    > create table {table_name} (var type, var1 type1) WITH (appendonly=true, orientation=parquet) distributed by (var) partition by list (var1) (partition name values (val), partition name1 values (val1));

parquet table distributed by randomly and partitioned by list:

    > create table {table_name} (var type, var1 type1) WITH (appendonly=true, orientation=parquet) distributed randomly partiton by list (var1) (partition name values (val), partition name1 values (val));

