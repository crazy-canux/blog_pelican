Title: CNI
Date: 2018-11-12 21:00:08
Tags: Container, CNI, Flannel



# CNI

一台host：

    none
    host
    bridge

多台host:

    overlay
    macvlan

提供overlay/macvlan的网络服务.

* flannel
* cilium
* kube-router
* calico

## bridge

创建:

    $ docker network create -d bridge ...

使用:

    $ docker network connect [OPTIONS] NETWORK CONTAINER
    $ docker network disconnect [OPTIONS] NETWORK CONTAINER
    $ docker run --network ...

参数:

    com.docker.network.bridge.name # bridge名字
    com.docker.network.bridge.enable_ip_masquerade # iptables:nat, 容器访问外网.
    com.docker.network.bridge.enable_icc # iptables:filter, 同一网段容器相互访问.
    com.docker.network.bridge.host_binding_ipv4
    com.docker.network.driver.mtu

## overlay

创建:

    $ docker network create -d overlay

***

# Flannel

<https://github.com/coreos/flannel>

