Title: Etcd
Date: 2018-01-12 21:00:08
Tags: Container, Etcd



# Etcd

<https://github.com/etcd-io/etcd>

其它类似应用:

* consul
* zookeeper

安装:

    # 下载安装包并解压到/opt/etcd
    $ sudo mv /opt/etcd/etcd /opt/etcd/etcdctl /usr/local/bin/

    # for ubuntu16
    $ sudo vim /etc/systemd/system/etcd.service

    [Unit]
    Description=Etcd Server
    After=network.target
    After=network-online.target
    Wants=network-online.target
    Documentation=https://github.com/coreos
    [Service]
    Type=notify
    WorkingDirectory=/var/lib/etcd/
    ExecStart=/opt/kube/bin/etcd \
    --name=etcd \
    --cert-file=/etc/etcd/ssl/etcd.pem \
    --key-file=/etc/etcd/ssl/etcd-key.pem \
    --peer-cert-file=/etc/etcd/ssl/etcd.pem \
    --peer-key-file=/etc/etcd/ssl/etcd-key.pem \
    --trusted-ca-file=/etc/kubernetes/ssl/ca.pem \
    --peer-trusted-ca-file=/etc/kubernetes/ssl/ca.pem \
    --initial-advertise-peer-urls=https://10.103.239.90:2380 \
    --listen-peer-urls=https://10.103.239.90:2380 \
    --listen-client-urls=https://10.103.239.90:2379,http://127.0.0.1:2379 \
    --advertise-client-urls=https://10.103.239.90:2379 \
    --initial-cluster-token=etcd-cluster-0 \
    --initial-cluster=etcd=https://10.103.239.90:2380 \
    --initial-cluster-state=new \
    --data-dir=/var/lib/etcd
    Restart=on-failure
    RestartSec=5
    LimitNOFILE=65536
    [Install]
    WantedBy=multi-user.target

***

