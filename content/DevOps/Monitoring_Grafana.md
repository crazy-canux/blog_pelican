Title: Monitoring Grafana
Date: 2017-01-12 21:05:48
Tags: Monitoring, Graphing, Grafana



# Grafana

The tool for beautiful monitoring and metric analytics & dashboards for Graphite, InfluxDB & Prometheus & More.

<https://github.com/grafana/grafana>

支持多种data source:

graphite/influxdb/opentsdb/premetheus/elasticsearch/mysql/postgresql

安装配置参考官方文档

***

# admin

organizational administrators.

grafana administrators.

***

# dashboard

## row

## panel

***

# templating

定义变量：

    show tag values with key='host'

在templating中定义变量, query中使用的两种方式:

    $varname
    select * from cpu where 'host' =~ /^$host$/
    [[varname]]
    select * from cpu where 'host' =~ /^[[host]]&/

***

# Annotations

***

# alerting

需要安装配置SMTP.

推荐使用sendmail.

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

# HTTP API
