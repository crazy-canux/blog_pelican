Title: PSL_Data
Date: 2016-08-14 20:57:36
Tags: Python, Data



# Data Types

## datetime

    import datetime

classes:

    # datetime.date
    date(year, month, day)
    # methods:
    ctime(...)
    ...
    # data descriptors:
    day
    month
    year

    # datetime.datetime(datetime.date)
    datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    # methods:
    datetime.datetime.strptime(string, format)
    format_datetime = datetime.datetime.strptime('20160824161431', '%Y%m%d%H%M%S') # return: datetime.datetime(2016, 8, 24, 16, 14, 31)
    format_datetime = datetime.datetime.strptime('24 August 2016 16:14:31', '%Y%m%d%H%M%S') # return: datetime.datetime(2016, 8, 24, 16, 14, 31)

    datetime.datetime.strftime(format[, tuple])
    string_datetime = format_datetime.strftime("%d %B %Y %H:%M:%S") # return: '24 August 2016 16:14:31'
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # return: '2017-02-07 23:07:32'

    str(datetime.datetime.now())
    datetime.datetime.now().strftime('%Y%m%d%H%M%S') # 当前时间戳

    # datetime.time

    # datetime.timedelta

    # datetime.tzinfo

data:

    MAXYEAR = 9999
    MINYEAR = 1

## calendar

## collections

    import collections

classes:

    # collections.Callable

    # collections.Container

    # collections.Counter

    # collections.Hashable

    # collections.ItemsView

    # collections.Iterable

    # collections.Iterator

    # collections.deque
    # 返回一个deque类型的实例，也就是双端队列
    deque([iterable[, maxlen]])

    # collections.defaultdict
    # 返回一个defaultdict类型的实例，类似于dict.setdefault()
    defaultdict(default_factory[, ...])

functions:

    namedtuple(typename, field_names, verbose=False, rename=False)
    # 返回一个tuple的子类, 将只能通过index访问的tuple变为可以通过name来访问．
    NewTuple = namedtuple('NewTuple', ['elm1', 'elm2', 'elm3'])
    nt = NewTuple(1, 2, 3)
    nt.elm1 # 1

data:

## heapq

## bisect

## array

## sched

## Queue

队列数据结构．

    import Queue

classes:

    # Queue.Queue
    Queue(maxsize=0) # 创建一个大小为maxsize的queue对象
    # methods:
    empty(self) # 如果queue为空返回True
    full(self) # 如果queue达到maxsize返回True
    get(self, block=True, timeout=None) # 从队列中取出一个元素并返回,如果block=True,会一直阻塞,直到队列中有元素．
    get_nowait(self)
    join(self)
    put(self, item, block=True, timeout=None) # 把item放到队列中,如果block=true,会一直阻塞,直到队列有空间存放item.
    put_nowait(self, item)
    qsize(self) # 返回queue大小，近似值
    task_done(self)

## weakref

## UserDict

## UserList

## UserString

## types

## copy

copy和deepcopy都只拷贝对象的类型和数值，不拷贝对象的ID.也就是==运算为True, is(id())运算为False.

    import copy

functions:

    copy.copy(x) # 浅复制, 只拷贝父对象，不拷贝内部的子对象.
    copy.deepcopy(x, memo=None, _nil=[]) # 深复制, 拷贝父对象和内部的子对象

## pprint

## repr

***

# Data Persistence

pickle/cPickle/marshal提供对象的序列化操作．

gdb相关的模块anydbm/whichdb/dbm/gdbm/dumbdbm提供类似字典和文件的对象．

shelve集合了以上两者的功能．

## pickle

pickle不支持unicode,只支持ascii.

## cPickle

python3将cPickle和pickle统一合并为pickle.

cPickle是c开发的，速度比pickle快，但是不支持被继承．

    import cPickle

functions:

    Pickler(file, protocol=0)
    Unpickler(file)
    dump(obj, file, protocol=0) # 写入到一个文件
    dumps(obj, protocol=0) # 写入到一个字符串
    load(file) # 从文件读取
    loads(string) # 从字符串读取

data:

    HIGHEST_PROTOCOL = 2

## marshal

## shelve

## anydbm

## whichdb

## dbm

## gdbm

## dumbdbm

## cope_reg

## pickletools

## sqlite

python访问数据库两种方式：

1. ORM
2. DB-API

ORM是对象-关系管理器，相关模块有SQLAlchemy, SQLObject.

DB-API参考PEP248/249定义了Database的API。

<https://www.python.org/dev/peps/pep-0249/>

    import sqlite3

classes:

    # sqlite3.Connection
    # methods:
    close(...)
    commit(...)
    cursor(...)
    execute(...)
    ...

    # sqlite3.Cursor
    # methods:
    close(...)
    ...

functions:

    adapt(obj, protocol, alternate)
    connect(database[, timeout, isolation_level, detect_types, factory])
    ...

data:

***

# Data Compression and Archiving

## gzip

## bz2

## zlib

## zipfile

## tarfile

***
