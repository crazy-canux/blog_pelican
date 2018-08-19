Title: Beego
Date: 2018-07-20 23:14:07
Tags: Go, Beego



# Beego

Beego是golang的web框架.

beego 是基于八大独立的模块构建的，是一个高度解耦的框架。

bee 工具是一个为了协助快速开发 beego 项目而创建的项目，通过bee您可以很容易的进行 beego 项目的创建、热编译、开发、测试、和部署

<https://github.com/astaxie/beego>

<https://beego.me/>

beego遵守MVC设计模式.

M: model,数据存取

V: view，展现哪些数据

C: controller，如何展现数据

执行顺序：

    main ->
    -> router ->  input filter ->
    -> controller (Model/Session/Log/Cache/Tools...) ->
    -> output filter -> views ->
    -> main

# 安装

安装beego和工具bee:

    $ go get -u github.com/astaxie/beego
    $ go get -u github.com/beego/bee

验证安装:

    $ bee new hello
    $ cd hello
    $ bee run hello

# 命令

bee:

    bee new 创建web项目
    bee api 创建api应用
    bee run 自动编译运行
    bee pack 项目打包
    bee bale
    bee generate 自动生成代码
    bee migrate 数据库迁移

beego

***

# project

创建一个名为hello的项目

    $ cd $GOPATH/src/beegolang
    $ bee new hello

    hello
    |-- conf
        |- app.conf
    |-- main.go
    |-- models
        |-- models.go
    |-- views
        |-- index.tpl
    |-- controllers
        |-- default.go
    |-- routers
    |-- tests
    |-- static

验证开发服务器：

    $ bee run beegolang/hello
    # OR
    $ cd beegolang/hello; bee run

浏览器输入：

    http://127.0.0.1:8080

***
