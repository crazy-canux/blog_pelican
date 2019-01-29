Title: Monitoring Kapacitor
Date: 2018-01-18 19:23:25
Tags: TICK, Monitoring, Kapacitor



# Kapacitor

<https://github.com/influxdata/Kapacitor>

Open source framework for processing, monitoring, and alerting on time series data

可以通过chrongraf创建tickscript/task, 然后通过api/cli导入到kapacitor.

配置:

    hostname = "10.103.1.1"

    # 如果从influxdb读取数据需要配置该选项．
    [[influxdb]]
    enabled = true

    # 如果从该路径加载tickscript
    [[load]]
    enabled = true
    dir="/etc/kapacitor/load"
    # tasks, 放到/etc/kapacitor/load/tasks/*.tick,重启kapacitor会自动加载task,并默认enable.
    ## 要求，ID和tick文件同名，tickscript开头需要指定dbrp, tickscript里面需要指定batch/stream.
    # templates...
    # handlers...

***

# CLI

    $ kapacitor help

    # 创建/更新 task, 创建的默认是disable状态.
    $ kapacitor define [task id/name] -tick [*.tick] -type [stream|batch] -dbrp [database.retentionPolicy]
    # 删除task
    $ kapacitor delete [task id/name]

    $ kapacitor list tasks
    $ kapacitor reload [task id/name] # 相当于disable & enable.
    $ kapacitor enable [task id/name]
    $ kapaciror disable [task id/name]
    $ kapacitor show [task id/name]
    $ kapacitor watch [task id/name]

    $ kapacitor list topics
    $ kapacitor delete topics [topic id]

***

# Http API

    port = 9092

## configuration

获取所有可以overwrite的参数

    GET /kapacitor/v1/config

获取section/option参数

    GET /kapacitor/v1/config/smtp
    GET /kapacitor/v1/config/smtp/
    GET /kapacitor/v1/config/influxdb
    GET /kapacitor/v1/config/influxdb/localhost

    POST /kapacitor/v1/config/smtp/
    {
        "set":{
            "enabled": true
        }
    }

***

# TICKscript

tickscript字符串用单引号和三单引号表示.

    var a = 'test'
    var b = '''test1
    test2'''

Keywords:

    TRUE
    FALSE
    AND
    OR
    lambda
    var
    dbrp

operator:

    + - * /    算数运算
    == != < <= > >=    比较运算
    =~ !~    正则表达式匹配和不匹配
    ! AND OR    逻辑运算

chaining operators:

    |    chaining method (constructor)
    .    property method (property methods & event handlers)
    @    User Define Function

status:

    0 -> OK
    1 -> INFO
    2 -> WARN
    3 -> CRIT

***

# node

node是tickscript中的复杂数据结构．

两个顶级node类型是stream和batch

batch是定时查询influxdb.

stream是通过订阅influxdb,写入到influxdb的数据也会写入kapacitor.

constructor调用相应的property methods.

## stream

    var data = stream
        |from()...

property methods:

    quiet()

chaining methods:

    Deadman
    From
    Stats

## batch

    var data = batch
        |query()...

property methods:

    quiet()

chaining methods:

    Deadman
    Query
    Stats

## alert

alert有三种类型: threshold, relative, deadman.

    var alert = data
        |eval()...
        |alert()
          .id('{{ index .Tags "<tag-key>" }}')
          .message('{{ .ID }} {{ .Level }} {{ index .Fields "<field-key>" }} {{ .Time }}')
          .details(...)
          ...

constructor:

    alert()

property methods:

    id()    # 定义alert的ID
    message()    # 相当于email的subject.
    details()    # html格式的警告信息，相当于email的body.
    info()
    infoReset()
    warn()
    warnReset()
    crit()
    critReset()
    email()
    log()    # 将json格式的alert存放到文件．
    idTag
    idField
    levelTag()
    levelField()
    durationField()
    messageField()
    post()
    tcp()
    all()    # period里面所有值都满足条件才alert
    topic()
    flapping()
    history()
    inhibit(<category>, <tags>) // 忽略一类告警
    quiet()
    noRecoveries() # 不要发恢复(OK)的警告
    stateChangesOnly() # 状态改变才发警告,OK/INFO/WARNING/CRITICAL
    category()

message/details event data:

    # 通过property methods定义一些变量
    ID -> {{ .ID }}
    Name -> measurement
    TaskName -> task name
    Group -> groupBy
    Tags -> {{.Tags}} {{index .Tags "<tag_key>"}}
    Fields -> {{.Fields}} {{index .Fields "<field_key>"}}
    Message
    Details
    Time -> {{ .Time }}
    Duration -> {{ .Duration }}
    Level -> {{ .Level }}
    Data
    Recoverable

## query

constructor:

    query(q string)

property methods:

    fill()
    align()
    alignGroup()
    groupBy()
    cron()
    every()
    period()
    quiet()

## from

constructor:

    from()

property methods:

    database()
    retentionPolicy()
    measurement()
    where()
    groupBy()
    round()
    truncate()
    quiet()

## window

constructor:

    window()

property methods:

    every()
    period()
    align()
    quiet()

## Log

constructor:

    log()

property methods:

    level()
    prefix()
    quiet()

## influxDBOut

constructor:

    influxDBOut()

property methods:

    create()
    ...

***

# handler

handler是用来处理alert的工具, 最常用的是email

handler可以调用相应的options.

## email

options:

    to("<email_address>")

需要配置smtp

    [smtp]
        enabled = true
        host = "localhost"  # 一般postfix/mailutils和kapacitor安装到同一台server
        port = 25

        from = "canuxcheng@gmail.com"  # 必须配置
        to = [""]  # 可以在tickscript中指定, tickscript不指定，就用该配置.

        global = true # 开启后,tickscript中不用指定handler,默认都是发邮件.

## log

options:

    path
    mode

写入到log.

## post

## tcp
