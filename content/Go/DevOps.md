Title: DevOps
Date: 2018-01-01 10:49:21
Tags: Go, DevOps



# Go

go有三种安装方式：

1. 源码安装
2. 标准包安装
3. 第三方工具安装

GOROOT:

    GOROOT 就是go的安装目录

windows标准包安装go:

    下载zip包解压到C:\go
    %GOROOT%=C:\go

linux标准包安装go:

    下载.tar.gz包解压到/usr/local/go
    export GOROOT=/usr/local/go
    export PATH=$PATH:$GOROOT/bin

验证安装：

    $ go --help
    $ go version

第三方工具gvm安装go:

<http://github.com/moovweb/gvm>

    $ gvm install go1.9.2
    $ gvm use go1.9.2

***

# GOPATH

gopath用来存放go源码，go的可运行文件，以及相应的编译之后的包文件．

GOPATH 从go1.1到1.7都需要设置，而且不能是go的安装目录, go1.8开始有默认值:

    GOPATH=$USERPROFILE%go
    GOPATH=$HOME/go

gopath结构：

    src    存放源码
    pkg    编译后的库文件
    bin    编译后生成的可执行文件

bin目录一般加入环境变量:

    $GOPATH/bin

gopath有多个值时用冒号分开即可.

***

# go命令

    $ go help [command]

get

下载并安装包和依赖, 也就是安装第三方的库．

    $ go get [...] [packages]

    > go get安装第三方包如果出现依赖无法安装，可以通过github下载．
    $ cd golang.org/x
    $ git clone https://github.com/golang/crypto.git crypto
    $ go install golang.org/x/crypto/ssh

build

编译包和依赖

    $ go build [-o output] [-i] [build flags] [packages]

install

编译并安装包和依赖

    $ go install [build flags] [packages]

run

编译并运行程序

    $ go run [...] gofiles... [...]

fmt

格式化代码和文档：

    $ go fmt [...] [packages]

test

测试包:

    $ go test [...] [packages] [...]

doc

查看文档：

    $ go doc [package/symbol]

***

# 包管理

go get的功能很有限．

godep和golide都会被官方的dep取代．

## dep

<https://github.com/golang/dep>

无法解决GFW的问题.

安装：

    $ go get -u github.com/golang/dep/cmd/dep

go官方包管理器

    # 初始化一个使用dep管理包的项目，
    # 创建Gopkg.toml, Gopkg.lock, vendor/
    $ dep init

    $ dep status

    $ dep prune

    $ dep ensure
    $ dep ensure -update
