Title: Redis
Date: 2017-05-03 14:46:14
Tags: Database, NoSQL, Redis



# Redis

redis在key-value存储上性能比memcached更好．

安装：

    $ sudo apt-get install redis-server

redis监听端口6379.

redis gui:

<https://github.com/uglide/RedisDesktopManager>

***

# redis的命令

server:

    redis-server

client:

    redis-client

test:

    redis-benchmark

***

# CLI

redis-cli 进入命令行模式

    > command    # 查看所有可用命令

    > info    # 查看redis服务器信息

    > monitor

***

# 数据类型

string

    > set <key> <value>
    > get <key>

list

    > lset <key> <index> <value>
    > lindex <key> <index>
    > rpop
    > lpop <key>
    > rpush
    > lpush

hash

    > hset <key> <field> <value>
    > hget <key> <field>

set

    > sadd <key> <member>
    > spop <key>
    > srem <key> <memeber>

sorted set

    > zadd <key> <score> <member>
    > zrem <key> <member>

***


