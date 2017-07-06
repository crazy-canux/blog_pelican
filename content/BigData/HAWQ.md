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

    # jdbc for hawq
    $ jdbc:pivotal:greenplum://hdm1:5432;DatabaseName=getstartdb;User=hdbuser;Password=hdbpass
