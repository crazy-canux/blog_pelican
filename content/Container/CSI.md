Title: CSI
Date: 2018-11-12 21:00:08
Tags: Container, CSI



# CSI

提供容器的数据持久化服务.

容器管理数据的两种方式：

* 数据卷 Volumes
* 挂载主机目录(bind mounts)
* tmpfs

原理:

* 如果host上目录不存在，docker会自动创建
* 如果container上目录不存在，docker会自动创建
* 如果container目录存在且有内容，会被host上的目录覆盖掉，但不会被删除.

## Volumes

数据卷 是被设计用来持久化数据的，它的生命周期独立于容器.

volumes是通过docker volume命令管理的，位于/var/lib/docker/volumes/下面.

Docker不会在容器被删除后自动删除 数据卷，并且也不存在垃圾回收这样的机制来处理没有任何容器引用的 数据卷。

创建:

    $ docker volume create myvolume
    $ docker volume rm myvolume

使用：

    $ docker run -v/--volume myvolume:/var/lib/app ...
    $ docker run --mount source=myvolume,target=/var/lib/app ...

## Bind

bind mount就是直接将host路径挂在到docker．

使用:

    $ docker run -v/--volume /opt/app:/var/lib/app:ro ...
    $ docker run --mount type=bind,source=/opt/app,target=/var/lib/app,readonly ...

***

# PV

persistent volume

# PVC

Persistent volumn claim

