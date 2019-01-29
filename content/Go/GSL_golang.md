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

    //更改调度器可以使用的逻辑cpu数量.
    func GOMAXPROCS(n int) int

    // 使当前goroutine让出绑定的cpu,其它goroutine可以继续执行.
    // 当前goroutine放回队列等待继续执行.
    func Gosched()

    // 终止当前goroutine,终止前执行所有defer.
    func Goexit()

***

# runtime/debug

## function

    // 设置最大线程数，默认1000.
    func SetMaxThreads(threads int) int

***

# runtime/cgo

***

# runtime/pprof

***

# runtime/race

***

# runtime/trace

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
