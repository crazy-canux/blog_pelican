Title: PSL_Data
Date: 2016-08-14 20:57:36
Tags: Python, Data

# Data Types

## datetime

    import datetime

    datetime.datetime.strptime(string, format)
    format_datetime = datetime.datetime.strptime('20160824161431', '%Y%m%d%H%M%S') # return: datetime.datetime(2016, 8, 24, 16, 14, 31)
    format_datetime = datetime.datetime.strptime('24 August 2016 16:14:31', '%Y%m%d%H%M%S') # return: datetime.datetime(2016, 8, 24, 16, 14, 31)

    datetime.datetime.strftime(format[, tuple])
    string_datetime = format_datetime.strftime("%d %B %Y %H:%M:%S") # return: '24 August 2016 16:14:31'
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # return: '2017-02-07 23:07:32'

    str(datetime.datetime.now())

    datetime.datetime.now().strftime('%Y%m%d%H%M%S')

## calendar

## collections

    import collections

## heapq

## bisect

## array

## sched

## Queue

## weakref

## UserDict

## UserList

## UserString

## types

## copy

copy和deepcopy都只拷贝对象的类型和数值，不拷贝对象的ID.也就是==运算为True, is(id())运算为False.

    import copy
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
    dump(obj, file, protocol=0) # 写入到一个文件
    load(file) # 从文件读取
    dumps(obj, protocol=0) # 写入到一个字符串
    loads(string) # 从字符串读取

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

DB-API参考PEP249定义了Database的API。

<https://www.python.org/dev/peps/pep-0249/>

    import sqlite3
    cxn = sqlite3.connect(r'/path/to/file')
    cur = cxn.cursor()
    cur.execute(<sql>)
    ...
    cur.close()
    cxn.close()

***

# Data Compression and Archiving

## gzip

## bz2

## zlib

## zipfile

## tarfile

***

# TPL

相关的第三方库
