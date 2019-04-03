Title: Monitoring Telegraf
Date: 2018-01-18 19:23:25
Tags: TICK, Monitoring, Telegraf



# Telegraf

<https://github.com/influxdata/telegraf>

The plugin-driven server agent for collecting & reporting metrics.

***

# Configuartion

agent configuration:

    interval    所有inputs的默认运行间隔
    round_interval
    collection_jitter
    precision    ns/us/ms/s
    flush_interval
    flush_jitter

input configuration:

    interval
    name_override # 默认measurements是插件名,修改默认measurements.
    name_prefix
    name_suffix
    tags

***

# Go API

<https://godoc.org/github.com/influxdata/telegraf#Input>

测试插件：

    # 需要配置文件
    $ telegraf --input-filter <plugin-name> --test

***

# Build

安装依赖：

    sudo apt-get install ruby-dev
    sudo gem install fpm
    sudo apt-get install rpm

编译telegraf:

    make telegraf

生成配置文件：

    ./telegraf config > ./etc/telegraf.conf

构建deb:

    make package

***

# Development

修改默认enable的plugin:

    # plugin中相应的sampleConfig中的字段不要用#注释．
    internal/config/config.go -> 可以修改默认enable的plugin.
    inputDefaults
    outputDefaults

调试：

    ./telegraf --config ./etc/telegraf.conf --input-filter process --test

添加debugxinxi

    import "log"
    log.Printf("D! key: %v", value)
    # "D!" 开头的信息当debug=true才会打印.

***
