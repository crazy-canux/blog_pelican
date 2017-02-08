---
layout: post
title: Monitoring之Addons
comments: true
date: 2016-06-08 09:46:47
updated:
tags:
- addons
- monitoring
categories:
- Operation
- Monitor
permalink:
---

# OMD

> OMD implements a completely new concept of how to install, maintain and update a monitoring system built on Nagios.

<http://omdistro.org/>

<http://git.mathias-kettner.de/git/?p=omd.git;a=tree>

The Open Monitoring Distribution

用于快速部署基于nagios的分布式监控，包括：
1. Icinga/Shinken/check_MK
2. Monitoring-Plugins和其它插件
3. mod-gearman/MK Livestatus/thruk/multisite
4. nsca/check_nrpe。
5. NagVis/Pnp4nagios/rrdtool/dokuwiki

# Gearman

> Gearman provides a generic application framework to farm out work to other machines or processes that are better suited to do the work.

Gearman用来做任务分发的.

一个C++实现的Gearman Job Server:

<http://gearman.org/>

<https://github.com/gearman/gearmand>

一个C实现的Gearman worker:

<http://www.mod-gearman.org/>

<https://github.com/sni/mod_gearman>

# rrdtools

>RRDtool is a little program for easily maintaining a database of time-series data. It comes with a charting program for drawing pretty graphs based on the data stored.

存储性能数据。

<http://oss.oetiker.ch/rrdtool/>

<https://github.com/oetiker/rrdtool-1.x>

# pnp4nagios

> PNP is an addon to Nagios which analyzes performance data provided by plugins and stores them automatically into RRD-databases.

基于RRD，绘制nagios的性能图。

<http://docs.pnp4nagios.org/>

<https://github.com/lingej/pnp4nagios>

可以在nagios的service配置中添加“ostpl_enable-graph"启用图形。

templates.dist是自带模板

templates是用户自定义模板

XXX.php需要和nagios的service的command_name同名，默认查找这个同名的模板.

测试就是scp XXX.php nagios-server:/usr/share/pnp4nagios/html/templates/然后去nagios查看结果

pnp4nagios查找顺序：
1. templates/check_XXX.php
2. templates.dist/check_XXX.php
3. templates/default.php
4. templates.dist/default.php

# Nagvis

>NagVis is a program for visualizing the data the monitoring core of your choice, for example Nagios, Naemon, Icinga or Shinken, in a human friendly way.

绘制监控地图。

<http://www.nagvis.org/>

<https://github.com/NagVis/nagvis>

***

# dokuwiki

> DokuWiki is a simple to use and highly versatile Open Source wiki software that doesn't require a database.

创建监控的procedure。

<https://www.dokuwiki.org/dokuwiki/>

<https://github.com/splitbrain/dokuwiki>

***

# graphite

<https://github.com/graphite-project>

<http://graphite.readthedocs.io/en/latest/index.html>

Zabbix,Sensu,Ganglia,Nagios/Naemon/Icinga/Shinken都可以配合使用。

绘制性能图。

graphite-web

> A highly scalable real-time graphing system

carbon

> Carbon is responsible for receiving metrics over the network, caching them in memory for "hot queries" from the Graphite-Web application, and persisting them to disk using the Whisper time-series library.

whisper/ceres

ceres会替代whisper。

> Whisper is a fixed-size database, similar in design and purpose to RRD (round-robin-database). It provides fast, reliable storage of numeric data over time. Whisper allows for higher resolution (seconds per point) of recent data to degrade into lower resolutions for long-term retention of historical data.

# grafana

> Grafana is an open source, feature rich metrics dashboard and graph editor for Graphite, Elasticsearch, OpenTSDB, Prometheus and InfluxDB.

为graphite提供更好的可视化图形。

<https://github.com/grafana/grafana>

<http://grafana.org/>

# graphios

> A program to send nagios perf data to graphite(carbon)/statsd/librato/influxdb

发送nagios性能数据到Graphite。

<https://github.com/shawn-sterling/graphios>

# Ledbetter

> A simple script for gathering Nagios problem statistics and submitting them to Graphite. It focuses on summary (overall, servicegroup and hostgroup) statistics and writes them to the nagios.problems metrics namespace within Graphite.

发送nagios性能数据到Graphite。

<https://github.com/github/ledbetter>

***

# NSCP

> NSClient is an agent designed originally to work with Nagios but has since evolved into a fully fledged monitoring agent which can be used with numerous monitoring tools (like Icinga, Naemon, OP5, NetEye Opsview etc).

又叫NSClient++,现在同时支持windows和linux,主要用来安装到windows服务器,用于监控windows系统.

<https://nsclient.org/>

<https://github.com/mickem/nscp>
