Title: PSL_System
Date: 2016-08-15 11:04:12
Tags: Python, System



# Generic Operating System Services

## os

    import os

## time

    import time
    # 获取当前unix时间戳
    time.time()

    # 将时间2011-09-27 10:50:00转换成时间戳（从1970开始的秒数）
    time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))

    # 将时间戳转换成时间2011-09-27 10:50:00
    time.gmtime(1472540718.340721)

## io

## logging

    import logging

## getopt

## argparse

## errno

## getpass

## curses

## platform

## ctypes

    import ctypes

***

# Optional Operating System Services

## multiprocessing

## thread

## threading

## readline

## rlcompleter

## select

## dummy_threading

## dummy_thread

## mmap

***

# TPL

## Click

<https://github.com/pallets/click>

## Pexpect

<https://github.com/pexpect/pexpect>
