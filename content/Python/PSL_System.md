Title: PSL_System
Date: 2016-08-15 11:04:12
Tags: Python, System



# Generic Operating System Services

## os

    import os

    os.pardir # 表示上一级路径

## time

    import time
    # 获取当前unix时间戳
    time.time()

    # 将时间2011-09-27 10:50:00转换成时间戳（从1970开始的秒数）
    time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))

    # 将时间戳转换成时间2011-09-27 10:50:00
    time.gmtime(1472540718.340721)

    time.sleep(seconds) # 延迟

## io

## logging

    import logging

## getopt

## argparse

    import argparse
    parser = argparse.ArgumentParser()
     |      - prog -- The name of the program (default: sys.argv[0])
     |      - usage -- A usage message (default: auto-generated from arguments)
     |      - description -- A description of what the program does
     |      - epilog -- Text following the argument descriptions
     |      - parents -- Parsers whose arguments should be copied into this one
     |      - formatter_class -- HelpFormatter class for printing help messages
     |      - prefix_chars -- Characters that prefix optional arguments
     |      - fromfile_prefix_chars -- Characters that prefix files  containing additional arguments
     |      - argument_default -- The default value for all arguments
     |      - conflict_handler -- String indicating how to handle conflicts
     |      - add_help -- Add a -h/-help option

    parser.add_argument_group
    parser.add_argument
    | - name or flags - Either a name or a list of option strings, e.g. foo or -f,
    --foo.
    action - The basic type of action to be taken when this argument is
    encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command
    line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals
    only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by
    parse_args().
    add_subparsers
    parse_args
    parse_known_args

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
