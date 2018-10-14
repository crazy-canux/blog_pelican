Title: Jenkins
Date: 2016-04-15 09:41:39
Tags: DevOps, Jenkins



# Jenkins

Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks such as building, testing, and deploying software.

<https://github.com/jenkinsci/jenkins>

安装好Jenkins后安装需要的插件．

安装jenkins:

    # download jenkins.war and install java8.
    $ java -jar jenkins.war --httpPort=8080
    $ firefox http://localhost:8080

设置开机自动启动，不用每次从终端启动:

    $ vim /etc/systemd/system/jenkins.service
    $ systemctl daemon-reload
    $ systemctl enable jenkins.service
    $ systemctl start jenkins

jinkens主目录:

    # 默认主目录在/home/canux/.jenkins

***

# 系统管理

管理插件，管理用户等.

# 添加credentials

首先添加源代码的credential.比如github/gitlab/p4v/bitbucket.

# nodes

添加节点需要安装和master版本一样的java.

# blueocean

blueocean是jenkins的一个差劲，提供更好的用户界面.

***

# plugins

## thinbackup

备份插件，主要备份jenkins主目录.

***

# pipeline

使用pipeline需要先安装pipeline插件.

pipeline是groovy语法的jenkins的DSL.

***

