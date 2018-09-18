Title: GSL_concurrency
Date: 2018-01-01 10:49:21
Tags: Go, GSL, sync



# sync

sync用于线程同步

    import "sync"

## constants

## variables

## functions

## Locker

## Once

## Mutex

## RWMutex

## Cond

## WaitGroup

用于等待一组线程结束，父线程用Add方法来设定应等待的线程数量;
每个被等待的线程在结束时应调用Done方法;
同时，主线程应调用Wait方法阻塞至所有线程结束．

struct:

    type WaitGroup sttruct {}

functions:

methods:

    func (*WaitGroup) Add(delta int)
    # 增加计数

    func (*WaitGroup) Done()
    # 减少计数

    func (*WaitGroup) Wait()
    # 阻塞直到计数器为0

## Pool

***

# sync/atomic
