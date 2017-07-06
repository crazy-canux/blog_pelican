Title: DevOps
Date: 2016-04-11 22:58:06
Tags: Java



# Java的IDE

VIM + Plugins

IBM -> eclipse

Oracle -> NetBeans

Jetbrains -> InteLLiJ IDEA

# Java安装

JRE: Java Runtime Environment. Java的运行环境。

JDK: Java Develop Kit. Java的开发工具包。包括JRE和其它开发工具。

1. OpenJDK(/usr/lib/jvm/)

        $ sudo add-apt-repository ppa:openjdk-r/ppa
        $ sudo apt-get update
        $ sudo apt-get install openjdk-8-jdk

        $ sudo yum install java-1.8.0-openjdk*

2. Oracle JDK(C:\Program Files\Java\)

        $ sudo add-apt-repository ppa:webupd8team/java
        $ sudo apt-get update
        $ sudo apt-get install oracle-java8-installer

3. IBM JRE

    一些IBM的程序需要安装IBM的JRE。

# Java配置

配置java和java工具：

    $sudo update-alternatives --config java
    $sudo update-alternatives --config javac
    $sudo update-alternatives --config jdb
    $sudo update-alternatives --config jar
    $sudo update-alternatives --config javadoc
    $sudo update-alternatives --config javap
    $sudo update-alternatives --config javah

Windows添加环境变量到path：

    JAVA_HOME: C:\Program Files\Java\jdk1.8.0_92
    PATH: %JAVA_HOME%\bin

Linux添加环境变量到~/.bash_profile或~/.bashrc:

    export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-.../jre
    export PATH=$JAVA_HOME/bin:$PATH

# 获取java源代码

解压安装目录里的src.zip，在安装目录src即可访问源码。

# 获取java文档

下载官方文档。

在安装路径新建docs目录，解压到docs目录,用file协议访问。

file:\\\C:\Program Files\Java\jdk_version\docs\index.html

***

# java

/usr/lib/jvm/<java-version>/jre/bin/java

    $ java -version

***

# javac

/usr/lib/jvm/<java-version>/bin/javac

    $ javac -version

***

# jdb

/usr/lib/jvm/<java-version>/bin/jdb

    $ jdb -version

***
# Java项目结构

    .
    |-- README.md
    |-- LICENSE
    |-- AUTHORS.md
    |-- CONTRIBUTING.rst

    |-- src
