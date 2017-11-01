Title: AMQP
Date: 2017-09-25 09:41:39
Tags: AMQP, Rabbitmq



# AMQP


AMQP: Advanced Message Queue Protocol.

AMQP是高级消息队列协议．是异步消息传递所使用的应用层协议规范．

***

# Rabbitmq

RabbitMQ是一个erlang开发的AMQP的开源项目．

<http://www.rabbitmq.com/>

rabbitmq-server也叫broker server

rabbitmq的三个组件：
* exchange,　交换器，发送消息的实体
* queue,　队列，接受消息的实体
* binding, 绑定器，连接交换器和队列，并且封装消息的路由信息

        producer => exchange -> routes -> queue => comsumer

安装

    $ sudo apt-get install rabbitmq-server

配置

    [
        {rabbit,
            [
                {heartbeat, 8000}
            ]
        }
    ].

# rabbitmqctl 命令

    $ sudo rabbitmqctl [-n node] [-t timeout] [-q] <commands> [command options]

添加用户并授权：

    $ add_user [username] [password]
    $ set_user_tags [username] administrator
    $ set_permissions sandbox ".*" ".*" ".*"

队列管理：

    $ stop_app
    $ reset
    $ start_app

# rabbitmq-plugins 插件管理

启动web-gui:

    $ rabbitmq-plugins enable rabbitmq_management
    # http://localhost:15672 guest/guest

***

# python

## pika

<https://github.com/pika/pika>

    $ pip install pika

    import pika
