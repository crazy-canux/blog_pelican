Title: RabbitMQ
Date: 2017-09-25 09:41:39
Tags: Network, Rabbitmq



# Rabbitmq

<https://github.com/rabbitmq>

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

queue:　生产者和消费者都应该创建queue.(只能通过exchange接收message)

exchanges类型:

* fanout: 所有绑定到此exchange的queue都可以接收消息
* direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
* topic：所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息

message类型:

* messages: 生产者产生的总消息数．
* messages_ready: 等待deliver给消费者的消息．
* messages_unack: 已经被consumer处理，但是没有被ack的消息．

virtual hosts: 本质就是一个rabbitmq server,拥有独立的exchange,queue.默认是/(%2F).

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

    # 默认的guest/guest只能用于localhost.
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

# HAProxy

rabbitmq-cluster部署：

1. 在所有node上安装rabbitmq-server.
2. 修改所有node的/etc/hosts，配置ip和hostname.
3. 同步所有node的cookie(/var/lib/rabbitmq/.erlang.cookie).
4. 启动所有node上的rabbitmq-server.
5. 在所有slave node运行

        # rabbitmqctl stop_app
        # rabbitmqctl reset
        # rabbitmqctl start_app

6. 在master node 添加slave node到cluster.

        # rabbitmqctl stop_app
        # rabbitmqctl reset
        # rabbitmqctl join_cluster rabbit@<slaveN-host>
        ...
        # rabbitmqctl start_app

7. 检查cluster状态

        # rabbitmqctl cluster_status

8. 设置policy

        # rabbitmqctl set_policy ha-all "" '{"ha-mode":"all","ha-sync-mode":"automatic"}'

haproxy-server部署:

1. 在haproxy servwer安装haproxy
2. 配置haproxy

        # sudo vim /etc/haproxy/haproxy.cfg
        global
            log /dev/log    local0
            log /dev/log    local1 notice
            chroot /var/lib/haproxy
            user haproxy
            group haproxy
            daemon
        defaults
            log     global
            mode    tcp
            maxconn 10000
            timeout connect 3000
            timeout client 1000s
            timeout server 1000s
        frontend rabbitmq_front
            bind <haproxy-ip>:5672
            reqadd X-Forwarded-Proto:\ amqp
            default_backend rabbitmq_backend
        backend rabbitmq_backend
            balance roundrobin
            server rabbitmq-master <master-ip>:5672 check
            server rabbitmq-slave <slave-ip>:5672 check
        bind 0.0.0.0:15672
            server <master-hostname> <master-ip>:15672 check
            server <slave-hostname> <slave-ip>:15672 check

3. 重启haproxy service.
