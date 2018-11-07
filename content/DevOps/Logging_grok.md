Title: Logging Grok
Date: 2018-06-08 09:46:47
Tags: Logging, Grok



# grok

logstash和telegraf都是用grok来解析log

在线检测

<http://grokdebug.herokuapp.com/>

grok的正则表达式

<https://github.com/kkos/oniguruma/blob/master/doc/RE>

可用的pattern(logstash & telegraf-logparser/tail)

<https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/grok-patterns>

<https://github.com/influxdata/telegraf/blob/master/plugins/inputs/logparser/grok/patterns/influx-patterns>

***

# Elastic stack

beats/filebeats: 通过filebeats agent获取log．

logstash: 使用filebeats解析log并写入stash(elasticsearch).

***

# TICK stack

telegraf(agent): 通过logparser/tail插件解析log并写入influxdb.

pattern:

    # 通过已经定义的变量来定义filter
    patterns = ['''${<capture_syntax>[:<semantic_name>][:<modifier>]}''']
    patterns = ['''%{TIMESTAMP_ISO8601:asctime:string} \[%{DATA:name:string}\] %{LOGLEVEL:levelname:string}: %{GREEDYDATA:message:string}''']

    capture_syntax是已经定义好的pattern.
    semantic_name是field/tag的名字, 默认都是string类型的field
    modifier 是string/int/float/tag/drop/ts-"CUSTOM"/...类型

    timestamp有特殊的modifier:
    timestamp 有特殊的modifier：
    Timestamp modifiers:ts (This will auto-learn the timestamp format)
    ts-ansic ("Mon Jan _2 15:04:05 2006")
    ts-unix ("Mon Jan _2 15:04:05 MST 2006")
    ts-ruby ("Mon Jan 02 15:04:05 -0700 2006")
    ts-rfc822 ("02 Jan 06 15:04 MST")
    ts-rfc822z ("02 Jan 06 15:04 -0700")
    ts-rfc850 ("Monday, 02-Jan-06 15:04:05 MST")
    ts-rfc1123 ("Mon, 02 Jan 2006 15:04:05 MST")
    ts-rfc1123z ("Mon, 02 Jan 2006 15:04:05 -0700")
    ts-rfc3339 ("2006-01-02T15:04:05Z07:00")
    ts-rfc3339nano ("2006-01-02T15:04:05.999999999Z07:00")
    ts-httpd ("02/Jan/2006:15:04:05 -0700")
    ts-epoch (seconds since unix epoch, may contain decimal)
    ts-epochnano (nanoseconds since unix epoch)
    ts-syslog ("Jan 02 15:04:05", parsed time is set to the current year)
    ts-"CUSTOM"

custom_patterns:

    # 通过正则表达式或已经定义的变量来定义新的变量
    # 一行一个
    custom_patterns = '''
        LOGLEVEL_PYTHON (?:WARNING|ERROR|CRITICAL)
    '''

logparser:

    [[inputs.logparser]]
    files = ["/opt/sandbox/logs/appliance.log"]
    from_beginning = false
    watch_method = "inotify"
    [inputs.logparser.grok]
      patterns = ['''
        %{TIMESTAMP_ISO8601:timestamp:ts-"2006-01-02 15:04:05.000"}
        \[%{DATA:name:string}\]
        %{LOGLEVEL_PYTHON:levelname:tag}:
        %{GREEDYDATA:message:string}''']
      measurement = "log_test"
      custom_pattern_files = []
      custom_patterns = '''LOGLEVEL_PYTHON (?:WARNING|ERROR|CRITICAL)'''
      timezone = "Local"

tail:

    [[inputs.tail]]
    files = ["/opt/sandbox/logs/appliance.log"]
    from_beginning = false
    pipe = false
    watch_method = "inotify"
    data_format = "grok"

    grok_patterns = ['''%{TIMESTAMP_ISO8601:timestamp:ts-"2006-01-02 15:04:05.000"}
      \[%{DATA:name:string}\] %{LOGLEVEL_PYTHON:levelname:tag}:
      %{GREEDYDATA:message:string}''']
    grok_custom_patterns = ''LOGLEVEL_PYTHON (?:WARNING|ERROR|CRITICAL)'''
    grok_timezone = "Local"

***
