Title: Go_Concurrency
Date: 2018-01-01 10:49:21
Tags: Go, Concurrency



# 并发/concurrency

coroutines: 协程

gocoroutines: go语言的协程，是并行的，通过channel来通信.

CSP: communicating sequential processes, 顺序通信处理

MPM: message pussing model, 消息传递

***

# goroutines

go关键字会启动一个新的goroutine并执行

    go FuncName(...)

主进程main结束了，goroutine也结束．

***

# channels

goroutine通过channel来通信.

chan通过make来创建，通过close来关闭．

chan是先进先出的.chan是引用传递．

如果chan指定了容量(有缓存), 就是异步，非阻塞模式．

默认是无缓存的，同步的,　阻塞模式.

申明一个变量:

    var chanName chan Type

定义一个chan:

    ch := make(chan Type, cap)
    ch <- v    # 将v发送至信道ch
    v := <- ch    # 从ch接收值并赋予v

遍历chan:

    for index, value := ch {...}

无缓冲的chan:

    ch := make(chan Type)

无缓冲的chan生产者会阻塞unbuffered，直到消费者接收数据, 也就是说是同步的synchronous.

只有消费者或者只有生产者的chan会导致死索，产生panic.

带缓冲的chan:

    ch := make(chan Type, cap)

    // 带缓冲的chan可以通过range遍历
    for i := range ch {...}

带缓冲的chan，在缓冲区满之前，都不会阻塞buffered，是异步的asynchronous.

chan的方向：

默认chan都是双向的，但是也可以指定方向

只接收的chan无法关闭

    var recv_only chan<- Type

只发送的chan

    var send_only <-chan Type

显示关闭chan:

    // 一般在生产者关闭chan
    close(ch)

    // 如果chan关闭ok=false
    v, ok := <-ch

***

## select

监听chan的数据流，类似于switch-case, 处理多个chan的情况

select默认是阻塞的，只有监听的chan中有数据才执行.

select类似switch, default是监听的chan都没有准备好的时候默认执行的．

***

