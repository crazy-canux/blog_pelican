Title: Database Monitoring
Date: 2016-04-03 14:46:14
Tags: Database, Monitoring



# Monitoring

# MSSQL

<https://github.com/Microsoft/mssql-monitoring>

<https://blogs.msdn.microsoft.com/sqlcat/2017/07/03/how-the-sqlcat-customer-lab-is-monitoring-sql-on-linux/>

<https://docs.microsoft.com/zh-cn/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-2017>

<https://docs.microsoft.com/zh-cn/sql/relational-databases/system-dynamic-management-views/sql-server-operating-system-related-dynamic-management-views-transact-sql?view=sql-server-2017>

参考telegraf/inputs/sqlserver.

# Mysql

# Oracle

# Postgresql

***

# Redis

通过redis-cli> info查看

    其它指标参考grafana dashboard.

    Redis_mode: cluster/standalone

    >>> replication (master/slave)
    Connected_slaves:    连接的slave实例个数
     
    >>> persistence  （rdb和aof的持久化信息）

***

# Mongo

通过mongo> serverStatus()查看

    其它指标参考grafana dashboard.
