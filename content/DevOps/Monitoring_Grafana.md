Title: Monitoring Grafana
Date: 2017-01-12 21:05:48
Tags: Monitoring, Graphing, Grafana



# Grafana

The tool for beautiful monitoring and metric analytics & dashboards for Graphite, InfluxDB & Prometheus & More.

<https://github.com/grafana/grafana>

支持多种data source:

graphite/influxdb/opentsdb/premetheus/elasticsearch/mysql/postgresql

安装配置参考官方文档

grafana配置文件是grafana.ini.

***

# HTTP API

    port = 3000

## dashboard

create/update dashboard:

将datasource设置成变量，然后导出的json文件就可以直接导入了．

dashboard.id=null才能创建新dashboard.

    post /api/dashboards/db
    data = json.dumps({
        "dashboard": {
            "id": null,
            ...
        },
        "folderId": 0,
        "overwrite": True, # True for python, true for go.
        "message": "commit message"
    })

## datasource

create datasource:

    post /api/datasources
    data = json.dumps({
        "name":
        "type":
        "url":
        "database":
        "access": "proxy"
    })

## alert

create alert notification/channel:

    post /api/alert-notifications
    data = json.dumps({
        "name":
        "type": "email",
        "isDefault": true,
        "settings": {
            "addresses": "a.com; b.com",
            "uploadImage": true
        }
    })

***

# Dashboard

graph

singlestat

table

text

heatmap

alertlist

## templating

定义变量：

    show tag values with key='host'
    # 设置在dashboard加载时更新

在templating中定义变量, query中使用的两种方式:

    $varname
    select * from cpu where 'host' =~ /^$host$/
    [[varname]]
    select * from cpu where 'host' =~ /^[[host]]&/

内置变量：

    $_interval  # 相当于influxdb里面的$interval，表示group by的时间间隔
    $timeFilter/$_timeFilter    # time > now() - <time range>

panel里的变量：

    $col         给select出来的field取别名
    $tag_host

## Annotations

***

# Alerting

email需要安装配置SMTP,推荐使用sendmail.

alert发出去的图片或连接打不开：

    $ vim /etc/grafana/grafana.ini
      [server]
      domain=
      root_url=

grafana4.6.2只有graph panel支持alert, singlestat 和 table暂不支持．

conditions暂不支持template variables.

***

# plugins

默认安装路径：

    /var/lib/grafana/plugins

命令：

    # 查看已经安装的plugin
    $ sudo grafana-cli plugins list-remote
    $ sudo grafana-cli plugins install <plugin-id> <version>

    # 查看安装的plugin
    $ sudo grafana-cli plugins ls

    # 删除plugin
    $ sudo grafana-cli plugins remove <plugin-id>

***
