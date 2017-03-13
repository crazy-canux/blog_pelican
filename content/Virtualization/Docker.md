Title: Docker
Date: 2017-01-12 21:00:08
Tags: Container, Docker



# Docker

<https://github.com/docker/docker>

Docker是一个容器引擎，分为社区版CE,和企业版EE.

Docker包括三个基本概念：

* 仓库repository,集中存放镜像文件的场所，docker hub是最大的公开仓库．
* 镜像image,镜像是一个文件系统.
* 容器container,容器是镜像的运行的实例．

docker hub:

<https://hub.docker.com/>

docker store:

<https://store.docker.com/>

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
    $ sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    # Install docker from the stable repository
    $ sudo apt-get update
    $ sudo apt-get install docker-ce

下载deb安装包安装：

    $ sudo dpkg -i /path/to/package.deb

验证安装：

    # Verify the docker installed correctly
    $ sudo docker run hello-world
    $ docker ps -a # 查看所有的docker

# 使用docker

    $ docker run
