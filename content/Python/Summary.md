Title: Summary
Date: 2016-06-21 21:18:20
Tags: Python



# python难点总结

* abstractmethod

    抽象方法是定义在基类中，可能有或没有任何实现的方法．
    可以用abc标准库的修饰器@abstractmethod实现．

* magicmethod

    魔法方法就是在类中用双下划线包围的方法．
    最基本的魔法方法是__init__方法．
    实例化一个类第一个被执行的魔法方法是__new__，最后一个被执行的是__del__．

# 多线程

* GIL

    GIL: Global Interpretror Lock. 全局解释器锁．

    python不建议使用多线程，用多进程代替．

* coroutine

    协程就是同时开启两个任务，但一次只顺序执行一个．
    如果执行的任务阻塞，就切换到下一个继续执行．节省时间．

***

# python的垃圾回收机制

GC: Garbage Collector.垃圾回收．

python的垃圾回收以引用计数为主，标记清除和分代收集为辅．

当对象被引用，包括对象在被创建,对象被作为参数传递给函数，对象成为容器对象的一个元素时，引用值增加．

当对象的引用被销毁，包括一个本地引用离开其作用范围，对象的别名被del显示销毁，对象的别名被赋值给其它对象，对象被从一个窗口对象中移除，窗口对象本身被del显示销毁，引用值会减少．

引用计数最大的问题是循环引用．

***

# 编码

## python2

python2中的str和unicode是两种不同的类.

str存储的是已经编码的字节序列，输出时看到的每个字节用16进制表示，以\x开头，每个汉字占用三个字节长度。

unicode存储的是编码前的字符，输出时看到的以\u开头，每个汉字占用一个长度。

str类型可以通过decode()方法转化为unicode对象。

unicode可以通过encode()方法转化为str对象。

    S.encode([encoding[,errors]])
    S.decode([encoding[,errors]])

encode把str类型的S编码成encoding,S必须是unicode，如果不是,python2默认先S.decode('ascii'),用ascii编码把S解码成unicode，如果S原来不是ascii而是utf-8就会报错，需要显示调用S.decode('utf-8')先把S按照utf-8解码成unicode再编码。

decode把str类型的S解码成unicode，S原来的编码用encoding指定,如果S原来是utf-8,S.decode('utf-8')按照utf-8把S解码成unicode。

    unicode(string[, encoding[, errors]])

unicode把str类型的string按照encoding解码成unicode。

如果文件中出现中文需要指定utf-8,默认是ascii：

    # -*- coding: utf-8 -*-

获取默认的encoding，python2系统默认是ascii:

    import sys
    print sys.getdefaultencoding()

## python3

python3的str和bytes是两种不同的类。

    S.encode(encoding='utf-8', errors='strict')
    B.decode(encoding='utf-8', errors='strict')

获取默认的encoding，python3系统默认是utf-8:

    import sys
    print(sys.getdefaultencoding())

