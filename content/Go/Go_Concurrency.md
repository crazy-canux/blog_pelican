Title: Go_Concurrency
Date: 2018-01-01 10:49:21
Tags: Go, Concurrency



# 并发/concurrency

go的并发同步模型来自CSP泛型。CSP是一种消息传递模型，用于在goroutine之间同步和传递数据的类型是channel.

concurrency:并发,同时管理很多事情，可以执行到一半就暂停去做其他事情.有同时执行的能力，但不一定要同时执行.

所以如果是单个cpu，每次只能运行一个goroutine,如果是多cpu,就是并行,每个cpu都可以跑goroutine.

parallelism: 并行,让不同的代码在不同的物理处理器上同时执行.

process: 进程, 是系统资源和调度的基本单位，包括内存，句柄，线程等。

thread: 线程,是cpu调度和分配的基本单位,每个进程至少包含一个线程，初始线程就是主线程，每个线程绑定到一个逻辑cpu上运行。

coroutines: 协程

goroutines: go语言的协程，是并行的，通过channel来通信.

CSP: communicating sequential processes, 顺序通信进程

MPM: message pussing model, 消息传递模型

# goroutines

go关键字会启动一个新的goroutine并执行.

每个goroutine会绑定到一个逻辑处理器上运行，每个逻辑处理器会绑定到单个操作系统线程。

当goroutine阻塞，就会把goroutine和线程从逻辑处理器上分离，然后创建一个新的线程绑定到该逻辑处理器，并继续运行队列中的其它goroutine.

当阻塞的goroutine恢复，会再次进入队列，和该goroutine绑定的线程也会保存下来.

    go FuncName(...)

主进程main结束了，goroutine也结束．

***

# 竟态

race condition: 竞争状态，多个goroutine同时操作同一资源.

    # 检测竞争状态
    $ go build -race

所以要解决goroutine间的消息传递和同步的问题.

# 同步

通过对资源上锁来保持同步.

golang的同步通过sync和sync/atomic两个包实现.

# 消息传递

goroutine通过channel来传递消息.

channels是引用类型.

channel可以共享内置类型，命名类型，结构类型，引用类型的值或指针.

chan通过make来创建，通过close来关闭．

chan是先进先出的.

如果chan指定了容量(有缓存), 就是异步，非阻塞模式．

默认是无缓存的，同步的,　阻塞模式.

申明一个变量:

    var ChanName chan Type

定义一个chan:

    var ch = make(chan Type, cap)
    ch := make(chan Type, cap)

操作chan:

    ch <- v    # 发送值到ch

    <- ch    # 从ch接收值
    v := <- ch    # 从ch接收值并赋予Type类型变量v

    v, ok = <- ch # 从ch接收值，如果ch关闭或没有数据，ok就为false.

无缓冲的chan:

    ch := make(chan Type)

无缓冲的chan生产者会阻塞unbuffered，直到消费者接收数据, 也就是说是同步的synchronous.

只有消费者或者只有生产者的chan会导致死锁，产生panic.

带缓冲的chan:

带缓冲的chan，在缓冲区满之前，都不会阻塞buffered，是异步的asynchronous.

只有通道中没有要接收的值，接收动作才会阻塞.

只有在通道没有可用缓冲区容纳被发送的值，发送动作才会阻塞．

    ch := make(chan Type, cap)

    // 带缓冲的chan可以通过range遍历
    for i := range ch {...}

chan的方向：

默认chan都是双向的，但是也可以指定方向

只接收的chan无法关闭

    var recv_only chan<- Type

只发送的chan

    var send_only <-chan Type

显示关闭chan:

通道关闭后，不能再向通道发送值，但是已经发送的值可以被接收.

    // 一般在生产者(发送动作)关闭chan
    close(ch)

    // 如果chan关闭ok=false, v为零值.
    v, ok := <-ch

***

## select

监听chan的数据流，类似于switch-case, 处理多个chan的情况

select默认是阻塞的，只有监听的chan中有数据才执行.

select类似switch, default是监听的chan都没有准备好的时候默认执行的．

***

