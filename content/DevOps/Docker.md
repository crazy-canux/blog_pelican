Title: Docker
Date: 2017-01-12 21:00:08
Tags: Container, Docker



# Docker

<https://github.com/docker>

<https://github.com/moby/moby>

Docker是一个容器引擎，分为社区版CE,和企业版EE.

docker不是虚拟机，也不依赖虚拟化技术．

Docker包括三个基本概念：

* 仓库repository,集中存放镜像文件的场所，docker store是最大的公开仓库．
* 镜像image, 镜像是一个文件系统.
* 容器container, 容器是镜像的运行的实例．

docker store:

<https://store.docker.com/>

docker hub:

<https://hub.docker.com/>

修改默认register:

    # http://7bd09afa.m.daocloud.io
    # https://docker.mirrors.ustc.edu.cn
    # https://registry.docker-cn.com

    $ sudo vim /etc/docker/daemon.json
    {
        "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
    }

# Install

windows和mac的桌面版需要安装docker toolbox.

ubuntu14.04推荐安装的依赖:

    # Install dependency
    $ sudo apt-get update
    $ sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual

从repository安装：

    # Install dependency
    $ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

    # Add Docker’s official GPG key
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    $ sudo apt-key fingerprint 0EBFCD88

    # set up the stable repository
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    # Install docker from the stable repository
    $ sudo apt-get update
    $ sudo apt-get install docker-ce

下载deb安装包安装：

    $ sudo dpkg -i /path/to/package.deb

添加用户到docker组:

    $ sudo usermod -aG docker $USER

卸载：

    $ sudo apt-get purge docker-ce
    $ sudo rm -rf /var/lib/docker

验证安装：

    # Verify the docker installed correctly
    $ sudo docker run hello-world
    $ docker ps -a # 查看所有的docker

# docker命令

image管理：

    $ docker image COMMAND

    查看本地镜像:
    $ docker image ls
    REPOSITORY    TAG    IMAGE ID    CREATED    SIZE

    根据创建dockerfile，创建新的images:
    $ docker image build

    创建tag
    $ dicker image tag

    删除image
    $ docker image rm <IMAGE ID>

container管理:

    $ docker container COMMAND

    运行image,产生一个container:
    $ docker container run <IMAGE ID>/<REPOSITORY> [COMMAND] [ARGS]

    列出container:
    $ docker container ls
    CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES
    -a 查看所有containers, 默认只显示running状态的

    启动container:
    $ docker container start/restart <CONTAINER ID>

    停止container:
    $ docker container stop <CONTAINER ID>

    删除container：
    $ docker container rm <CONTAINER ID>

    在container中执行命令
    $ docker container exec [OPTIONS] <CONTAINER> COMMAND [ARG...]

docker hub使用:

    # 登陆到docker hub
    docker login

    # 从docker hub/store查找images:
    docker search [OPTIONS] TERM
    $ docker search

    # 从registry获取repository/images到/var/lib/docker：
    docker pull [OPTIONS] NAME[:TAG|@DIGEST]
    $ docker pull
    $ docker pull ubuntu # 默认下载所有tag
    $ docker pull ubuntu:14.04
    # 从中国站点下载
    $ docker pull registry.docker-cn.com/library/ubuntu:16.04

    # 推送到docker hub
    docker push

***

# Dockerfile

    FROM
    RUN
    ADD
    COPY
    CMD
    EXPOSE
    WORKDIR
    MAINTAINER
    ENV
    ENTRYPOINT
    USER
    VOLUME
