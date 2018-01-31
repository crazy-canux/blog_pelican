Title: Monitoring Influxdb
Date: 2018-01-18 19:23:25
Tags: TICK, Monitoring, Influxdb



# Influxdb

<https://github.com/influxdata/influxdb>

Scalable datastore for metrics, events, and real-time analytics.

支持从opentsdb, graphite, collectd等获取数据

默认数据库_internal 用于存储内部运行数据

安装配置参考官方文档

***

# 数据结构

influxdb每条记录是一个point.

points包括下面部分：

    measurement: a measurement, like cpu_load, 相当于表名
    tags: zero or more tag, key=value, eg: host=ip
    fields: zero or more field, key=value, eg: value=0.18
    time: a timestamp

    <measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]

***

# CLI

    $ influx --help
    $ influx -username <username> -p <password> -h <hostname>

创建数据库

    $ CREATE DATABASE test

查看数据库

    $ SHOW DATABASES

切换数据库

    $ USE test

查看measurement(指标／表)

    $ SHOW MEASUREMENT

查看fileds

    $ SHOW FIELD KEYS

查看tags

    $ SHOW TAG KEYS
    $ SHOW TAB VALUES FROM measurement WITH KEY='tag-key'

插入数据

    $ INSERT cpu,host=server,region=en value=1.2 1434067467100293230

查询数据

    $ SELECT "host", "region", "value" from cpu

# HTTP API

    curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mydb"

# LINE protocol

# Python API

***

# influxQL

The SELECT clause specifies an InfluxQL function.
The FROM clause specifies a single measurement.
The WHERE clause specifies the time range for the query.
The GROUP BY clause groups results by all tags (*) and into 12-minute intervals.
The ORDER BY time DESC clause returns results in descending timestamp order.
The LIMIT 2 clause limits the number of points returned to two.
The OFFSET 2 clause excludes the first two averages from the query results.
The SLIMIT 1 clause limits the number of series returned to one.
The SOFFSET 1 clause paginates the series returned.

