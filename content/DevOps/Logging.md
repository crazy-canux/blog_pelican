Title: Logging
Date: 2017-01-12 21:05:48
Tags: Logging, Operations, ElasticSeaarch, Logstash, Kibana



# Logging

运维中的日志管理．

# ELK

ELK是实时日志分析平台．

elasticsearch是分布式搜索引擎

<https://github.com/elastic/elasticsearch>

logstash收集，分析和存储日志．

<https://github.com/elastic/logstash>

kibana日志分析友好的界面．

<https://github.com/elastic/kibana>

# 安装和配置

安装elasticsearch:

    $ 下载.tar.gz
    $ tar -xvf elasticsearch-x.x.x.tar.gz
    $ cd elasticsearch-x.x.x

    # Running as a daemon
    $ ./bin/elasticsearch -d -p pid
    $ kill `cat pid`

    # configuring
    $ vim ./config/elasticsearch.yml

elasticsearch通过http://localhost:9200接收logstash的消息

安装logstash:

    # 下载.tar.gz
    $ tar xvf logstash-x.x.x.tar.gz
    $ cd logstash-x.x.x

    # Running
    $ ./bin/logstash -e 'input { stdin { } } output { stdout {} }'

    # configuring
    $ vim ./config/logstash.yml

    # 添加elasticsearch的配置到logstash
    $ vim ./bin/logstash-elasticsearch.conf
    $ ./bin/logstash agent -f logstash-elasticsearch.conf

安装kibana:

    # 下载deb包安装

    # 设置sysv init
    $ sudo update-rc.d kibana defaults 95 10
    $ sudo service kibana start

    # 配置
    $ vim /etc/kibana/kibana.yml
