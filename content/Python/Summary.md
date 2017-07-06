Title: Summary
Date: 2016-06-21 21:18:20
Tags: Python



# python难点总结

* abstractmethod

    抽象方法是定义在基类中，可能有或没有任何实现的方法．
    可以用abc标准库的修饰器@abstractmethod实现．

# 多线程

* GIL

    GIL: Global Interpretror Lock. 全局解释器锁．

    python不建议使用多线程，用多进程代替．

* coroutine

    协程就是同时开启两个任务，但一次只顺序执行一个．
    如果执行的任务阻塞，就切换到下一个继续执行．节省时间．

***

