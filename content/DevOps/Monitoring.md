Title: Monitoring
Date: 2016-06-08 09:46:47
Tags: Monitoring



# Monitoring

Tranditional monitoring is for Datacenter, like nagios, zabbix.

Modern monitoring is for service, like Elastic stack for log monitoring.

Modern monitoring based on TSDB, like TICK stack for metrics monitoring.

# Elastic stack

kibana: 数据可视化

elasticsearch: 搜索，分析，存储数据

x-pack: 具有监控和报警功能的工具包.

logstash: 动态数据收集管道，支持可扩展的插件．

beats(agent): 轻量型数据采集平台，从边缘机器向logstash/elasticsearch发送数据．

# TICK stack

influxdb: tsdb.

kapacitor: alerting.

chronograf: GUI.

telegraf(agent): metrics collector.

***

# Graphing

最流行的监控绘图软件是grafana, 支持influxdb和elasticsearch.

使用grafana替代chronograf.
