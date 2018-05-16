Title: Monitoring Logging
Date: 2016-06-08 09:46:47
Tags: Monitoring, Logging



# Monitoring Logging

Log monitor.

***

# logrotate

***

# grok

logstash和telegraf-logparser都是用grok来解析log

在线检测

<http://grokdebug.herokuapp.com/>

grok的正则表达式

<https://github.com/kkos/oniguruma/blob/master/doc/RE>

可用的grok(logstash & telegraf)

<https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/grok-patterns>

<https://github.com/influxdata/telegraf/blob/master/plugins/inputs/logparser/grok/patterns/influx-patterns>

***

# Elastic stack

beats/filebeats: 通过filebeats agent获取log．

logstash: 使用filebeats解析log并写入stash(elasticsearch).

***

# TICK stack

telegraf(agent): 通过logparser插件解析log并写入influxdb.

pattern:

    # 通过已经定义的变量来定义filter
    patterns = ['''${<capture_syntax>[:<semantic_name>][:<modifier>]}''']
    patterns = ['''%{TIMESTAMP_ISO8601:asctime:string} \[%{DATA:name:string}\] %{LOGLEVEL:levelname:string}: %{GREEDYDATA:message:string}''']

    semantic_name是field/tag的名字, 默认都是string类型的field
    modifier 是string/int/float/tag/drop/ts-"CUSTOM"/...类型

custom_patterns:

    # 通过正则表达式或已经定义的变量来定义新的变量
    # 一行一个
    custom_patterns = '''
        LOGLEVEL_PYTHON (?:WARNING|ERROR|CRITICAL)
    '''

***
