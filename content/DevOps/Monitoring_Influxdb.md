Title: Monitoring Influxdb
Date: 2018-01-18 19:23:25
Tags: TICK, Monitoring, Influxdb



# Influxdb

<https://github.com/influxdata/influxdb>

Scalable datastore for metrics, events, and real-time analytics.

支持从opentsdb, graphite, collectd等获取数据

默认数据库_internal 用于存储内部运行数据

安装配置参考官方文档

log

    $ sudo journalctl -u influxdb.service

config:

    # 开通kapacitor的subscription功能
    [[subscriber]]
    enable = true

***

# 数据结构

influxdb每条记录是一个point.

points包括下面部分：

    measurement: a measurement, like cpu_load, 相当于表名
    tags: zero or more tag, key=value, eg: host=ip
    fields: zero or more field, key=value, eg: value=0.18
    time: a timestamp

    <measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]

series: 在一个database中,相同的retention policy, measurement, tag set的数据集，叫一个序列．

RP: retention policy, autogen是默认的存储策略, 用于设置数据保留时间.

CQ: continuous query, 连续查询，自动定时启动一组语句，将结果放在指定数据表中．

IFQL: influx query language.

***

# CLI

    $ influx --help
    $ influx -username <username> -p <password> -h <hostname>
    $ influx -precision rfc3339 # 显示可读的时间戳

    $ influx -database 'test' -host '127.0.0.1'
    -execute 'select * from "test"."test"."test" where time > now() - 30d'
    -format 'csv' > test.csv

database

    $ CREATE DATABASE test
    $ DROP DATABASE test
    $ SHOW DATABASES
    $ USE test

measurement(table)

    $ DROP MEASUREMENT <measurement>
    $ SHOW MEASUREMENTS
    $ SHOW MEASUREMENTS WHERE <tagkey>=<tagvalue>

tags

    $ SHOW TAG KEYS
    $ SHOW TAG KEYS FROM <measurement>
    $ SHOW TAG VALUES FROM <measurement> WITH KEY=<tagkey>

fileds

    $ SHOW FIELD KEYS
    $ SHOW FIELD KEYS FROM <measurement>

subscription

    $ SHOW SUBSCRIPTIONS
    $ CREATE SUBSCIPTION <subs_name> ON <db>.<rp> DESTINATIONS ("ANY"|"ALL") host{",", host}
    $ DROP SUBSCRIPTION <subs_name> ON <db>.<rp>

series

    $ SHOW SERIES
    $ DROP SERIES FROM <measurement> WHERE <tagkey>='<tagvalue>'
    $ DROP SERIES WHERE <tagkey>='<tagvalue>' # 从所有measurement删除指定节点的所有数据

shared

    $ drop shard <shard_id>

***

# HTTP API

    port = 8086

## write

create:

    curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mydb"
    post /query
    data = {
        "q": "create database <database>"
    }

## query

show:

    curl -G 'http://localhost:8086/query' --data-urlencode "q=show databases"
    get /query
    params = {
        "pretty" : True,
        "q": "show databases"
    }

***

# influxQL

influxql语句按下列关键字顺序排列

tag_key, field_key, measurement都需要用双引号.

The SELECT clause specifies an InfluxQL function.

    select "<field_key/tag_key>" from "<measurement>"

The INTO clause writes query results to a user-specified measurement.

    select <> INTO "<measurement>" from <>

The FROM clause specifies a single measurement.

    select <> from "<measurement>"

The WHERE clause specifies the time range for the query.

    select <> from <> where <condition1> OR/AND <condition2>

    # string类型的 value必须用单引号．
    select <> from <> where "<tag_key/field_key>" <operation> '<tag_value/field_value>'

    now() : time > now(() - 10m

    = != < >

    RE:
    =~ !~
    =~  : /.*ERROR.*|.*CRITICAL.*/  /ERROR|CRITICAL/

The GROUP BY clause groups results by all tags (*) and into 12-minute intervals.

    select <> from <> where <> group by "<tag_key>"

    fill()
    time()/time(1ns/u/ms/s/m/h/d/w)

The ORDER BY time DESC clause returns results in descending timestamp order.

    select <> from <> where <> group by <> order by <time/field_key>
    select <> from <> where <> group by <> order by <time/field_key> desc

The LIMIT 2 clause limits the number of points returned to two.

    select <> from <> where <> group by <> order by <> limit <number>
    select <> from <> where <> group by <> order by <> desc limit <number>

The OFFSET 2 clause excludes the first two averages from the query results.

    select <> from <> where <> group by <> order by <> limit <number> offset <>
    select <> from <> where <> group by <> order by <> desc limit <number> offset <>

The SLIMIT 1 clause limits the number of series returned to one.

    select <> from <> where <> group by <> order by <> limit <> offset <> slimit <>
    select <> from <> where <> group by <> order by <> desc limit <> offset <> slimit <>

The SOFFSET 1 clause paginates the series returned.

    select <> from <> where <> group by <> order by <> limit <> offset <> slimit <> soffzet <>
    select <> from <> where <> group by <> order by <> desc limit <> offset <> slimit <> soffset<>

The tz() clause returns the UTC offset for the specified timezone.

    select <> from <> where <> group by <> order by <> limit <> offset <> slimit <> soffzet <> tz(<time_zone>)
    select <> from <> where <> group by <> order by <> desc limit <> offset <> slimit <> soffset<> tz(<time_zone>)

***

# flux

influxql的升级版，支持多表查询.

***

# function

## aggregations

    count(<fieldkey>) # 统计fieldvalues行数
    distinct(<fieldkey>) # 返回fieldvalues不重复的值的列表
    integral(<fieldkey>) # 积分
    mean(<fieldkey>) # 返回fieldvalues的算数平均值
    median(<fieldkey>) # 返回fieldvalues的排序后的中间值
    mode(<fieldkey>) # 返回fieldvalues出现频率最高的值
    spread(<fieldkey>) # 返回fieldvalues最值之间的差异
    stddev(<fiekdkey>) # 返回fieldvalues的标准偏差
    sum(<fieldkey>) # 返回fieldvalues的和

## selectors

    bottom(<fieldkey>, N) # 返回最小的N个fieldvalues
    first(<fieldkey>) # 返回timestamp最小的fieldvalue
    last(<fieldkey>) # 返回timestamp最大的fieldvalue
    max(<fieldkey>) # 返回最大的fieldvalue
    min(<fieldkey>) # 返回最小的fieldvalue
    percentile(<fieldkey>, N) # 百分数
    sample(<fieldkey>, N) # 返回N个fieldvalue的随即样本
    top(<fieldkey>, N) # 返回最大的N个fieldvalue

## transformations

transformations函数的field_key可以是aggregations和selectors函数的返回值

    cumulative_sum(<field_key>)
    derivative(<field_key>, [<unit>]) # 求单位时间的变化率, (cur-last)/(interval/unit)
    difference(<field_key>) # 返回连续时间值之间的差异 -> 值的差异
    elapsed(<field_key>) # 返回连续时间间隔的差异 -> 时间间隔差异
    moving_average()
    non_negative_derivative()
    non_negative_difference()

## predictors

    holt_winters(function(<field_key>), N, S)

***

# RP

数据保存策略.

autogen是默认RP，duration=infinite

duration: 存储的数据时间间隔

replication: 存储的数据副本数量

    show retention policies on "<database>"

    create retention policy "<rp_name>" on "<database>" duration 30d replication 1 default

    drop retention policy "<rp_name>" on "<database>"

***

# CQ

对超过保存策略指定时间的数据，可以做统计采样.(类似于store procedure).

CQ不能更新，只能删除重建．

    show continuous queries

    create continuous query <CQ_name> on <database>
    begin
        SELECT <function[s]> INTO <destination_measurement> FROM <measurement> [WHERE <stuff>] GROUP BY time(<interval>)[,<tag_key[s]>]
    end

    DROP CONTINUOUS QUERY <cq_name> ON <database_name>

***
