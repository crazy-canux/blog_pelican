Title: GSL_golang
Date: 2018-01-01 10:49:21
Tags: Go, go, runtime, expvar, context, unsafe, errors



# runtime

## constants

    // 指定编译器
    const Compiler = "gc"/"gccgo"

    // 处理器架构: 386/amd64/arm
    const GOARCH string = theGoarch

    // 操作系统: linux/freebsd/darwin/win
    const GOOS string = theGoos

## variables

    var MemProfileRate int = 512 * 1024

## functions

    func GOROOT() string
    func Version() string

    // 返回本地机器的逻辑cpu个数
    func NumCPU() int

    // 设置同时执行的最大cpu数量
    func GOMAXPROCS(n int) int

***

# go

***

# expvar

***

# context

***

# unsafe

***

# errors

## function

    // 使用字符串创建一个错误, 返回一个error
    func New(text string) error
