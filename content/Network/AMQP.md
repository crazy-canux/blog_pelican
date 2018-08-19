Title: AMQP
Date: 2017-09-25 09:41:39
Tags: AMQP, Rabbitmq



# AMQP


AMQP: Advanced Message Queue Protocol.

AMQP是高级消息队列协议．是异步消息传递所使用的应用层协议规范．

常用的开源AMQP框架：

<https://github.com/rabbitmq>

<https://github.com/apache/kafka>

<https://github.com/apache/activemq>

***

# Rabbitmq

RabbitMQ是一个erlang开发的AMQP的开源项目．

rabbitmq-server也叫broker server

rabbitmq的三个组件：

* exchange,　交换器，发送消息的实体
* binding, 绑定器，连接交换器和队列，并且封装消息的路由信息
* queue,　队列，接受消息的实体

workflow:

    producer(publish-message) =>

    rabbitmq-server => exchange -> binding -> queue =>

    => comsumer

producer: 生产message并且publish到rabbitmq-server.

consumer: 连接到rabbitmq-server并且subscribe一些queue.

connection: producer和consumer都是通过tcp连接到rabbitmq-server.

channels: 建立在tcp连接中的虚拟连接，用于处理数据流动.

queue:　生产者和消费者都应该创建queue.

exchanges类型:

* direct
* fanout
* topic

message类型:

* messages: 生产者产生的总消息数．
* messages_ready: 等待deliver给消费者的消息．
* messages_unack: 已经被consumer处理，但是没有被ack的消息．

virtual hosts: 本质就是一个rabbitmq server, 拥有独立的exchange,queue.

round-robin dispatch: 循环分发，按顺序分发message到consumer,如果message被consumer正确接收，就会从queue中移除．

no-ack: 每次consumer接收数据后，不管是否处理完成，就标记为ack,然后从queue中删除．但是如果处理过程异常，数据就会丢失．

ack: ack方式就是数据处理完成后发送ack,保证数据被处理再从queue删除，如果异常，会dispatch到别的consumer.

durable: 消息持久化，如果rabbitmq-server异常退出或服务器重启，为了保证数据还在，需要做数据持久化.

消息的状态信息：

* deliver: 消息投递给消费着．
  redeliver:　消息重新投递给消费者．
* publish/subscribe: 将同一个消息deliver到多个consumer叫publish或subscribe.
* ack: 已经处理完成的消息

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

## rabbitmqctl 命令

    $ sudo rabbitmqctl [-n node] [-t timeout] [-q] <commands> [command options]

添加用户并授权：

    $ add_user [username] [password]
    $ delete_user <username>
    $ change_password <username> <newpassword>
    $ clear_password <username>
    $ set_user_tags [username] administrator
    $ list_users

权限管理:

    add_vhost <vhostpath>
    delete_vhost <vhostpath>
    list_vhosts [<vhostinfoitem> ...]
    set_permissions [-p <vhostpath>] <user> <conf> <write> <read>
    clear_permissions [-p <vhostpath>] <username>
    list_permissions [-p <vhostpath>]
    list_user_permissions <username>

    list_queues [-p <vhostpath>] [<queueinfoitem> ...]
    list_exchanges [-p <vhostpath>] [<exchangeinfoitem> ...]
    list_bindings [-p <vhostpath>] [<bindinginfoitem> ...]
    list_connections [<connectioninfoitem> ...]
    list_channels [<channelinfoitem> ...]
    list_consumers [-p <vhostpath>]
    status
    environment
    report
    eval <expr>

## rabbitmq-plugins 插件管理

启动web-gui:

    $ rabbitmq-plugins enable rabbitmq_management
    # http://localhost:15672 guest/guest

***


