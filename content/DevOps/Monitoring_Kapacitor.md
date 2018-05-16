Title: Monitoring Kapacitor
Date: 2018-01-18 19:23:25
Tags: TICK, Monitoring, Kapacitor



# Kapacitor

<https://github.com/influxdata/Kapacitor>

Open source framework for processing, monitoring, and alerting on time series data

***

# CLI

    $ kapacitor help

    $ kapacitor define [task id] -tick [*.tick]
    $ kapacitor delete [task id]

    $ kapacitor list tasks
    $ kapacitor show [task id]
    $ kapacitor reload [task id]
    $ kapacitor enable [task id]
    $ kapaciror disable [task id]

    $ kapacitor record stream -task cpu_alert -duration 60s
    $ kapacitor replay -recording $rid -task cpu_alert

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
            "enabled": false
        }
    }

***

# TICKscript



