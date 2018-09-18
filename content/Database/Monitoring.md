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

通过redis-cli info查看

    Redis_mode: cluster/standalone
     
    >>> client
    Connected_clients  已连接的客户端数量
    Blocked_clients 正在等待阻塞命令的客户端数量
     
    >>>memory
    Used_memory 由redis内存分配器分配的内存总量
    Used_memory_rss  和top看到一样
     
    >>> cpu
    Used_cpu_sys
    Used_cpu_user
     
    >>>keyspace
    Keys :  db0的key的数量
    Expires: db0的过期的key
    Avg_ttl:  db0平均存活时间
     
    >>> stats
    Total_commands_processed   redis处理的命令数
    Instantaneous_ops_per_sec    redis内部每秒执行命令数（QPS）
    Total_net_input_bytes    redis网络入口流量
    Total_net_output_bytes  redis网络出口流量
    Instantaneous_input_kbps：   每秒读字节数
    Instantaneous_output_kbps:  每秒写字节数
    Rejected_connections:  拒绝连接的个数
    Expired_keys:  总共过期的key的数量
    Evicted_keys: 总共剔除的key的数量
    Keyspace_hits: 命中个数
    Keyspace_misses: 没命中个数
     
    >>> replication (master/slave)
    Connected_slaves:    连接的slave实例个数
     
    >>> persistence  （rdb和aof的持久化信息）

***

# Mongo

