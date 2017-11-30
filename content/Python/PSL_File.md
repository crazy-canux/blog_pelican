Title: PSL_File
Date: 2016-08-14 20:51:28
Tags: Python, File



# File and Directory Access

## os.path

windows的路径要写成：

    C:\\test\\sub\\

    import os

function:

    os.path.expanduser(path) # 把path中~或~user扩展成绝对路径 expanduser("~/src") -> /home/user/src
    os.path.expandvars(path) # 把path中的shell变量$var 或 ${var} 还原．
    os.path.realpath(filename) # 返回filename的真实路径+文件名 realpath("/home/user/file.py") -> /home/user/file.py
    os.path.dirname(filename) # 返回filename的路径 dirname("/home/user/file.py") -> /home/user
    os.path.join(a, *p) # 拼结一个完整的路径　
    os.path.join(a, os.pardir) # 返回上级目录的路径
    os.path.abspath(path) # 返回绝对路径, os.path.abspath('__file__')
    os.path.splitext(p) # 分解路径和扩展名返回组成的元组，/home/user/test.py -> ("/home/user/test", ".py")
    os.path.basename(p) # 返回最后一个组件名，也就是文件名 /home/user/test.py -> test.py
    os.path.getsize(filename) # 返回文件大小
    os.path.exists(path) # 判断path(文件或目录)是否存在
    os.path.isfile(path) # 判断path是否是常规文件

## stat

## fileinput

## filecmp

## fnmatch

## linecache

## glob

functions:

    glob(pathname) # 返回匹配pathname路径下正则表达式的所有文件组成的列表
    iglob(pathname) # 同上，返回generator.

## shutil

Utility functions for copying and archiving files and directory trees.

    import shutil

functions:

    rmtree(path, ignore_errors=False, onerror=None) # 删除指定的目录,path不能是文件．
    unregister_archive_format(name)
    ...

## tempfile

## macpath

## ConfigParser

***

# File Formats

## csv

    import csv

classes:

    # csv.DictReader
    DictReader(self, f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

functions:

data:

## robotparser

## netrc

## xdrlib

## plistlib

***

# TPL

相关的第三方库

## pyyaml

YAML parser and emitter for Python

<http://pyyaml.org/wiki/PyYAML>

    $ pip install pyyaml

    import yaml

classes:

    # yaml.YAMLObject

    # methods:
    from_yaml(cls, loader, node)
    to_yaml(cls, dumper, data)

    # yaml.YAMLError

functions:

    add_constructor(tag, constructor, Loader=<class 'yaml.loader.Loader'>)

    dump(data, stream=None, Dumper=<class 'yaml.dumper.Dumper'>, **kwds)
    # dump(data, open(file, 'w')),　序列化python对象data到stream,一般是一个文件，如果stream=None, 返回生成的字符串．
    safe_dump(data, stream=None, **kwds) # 序列化最基本的tag
    dump_all(documents, stream=None, Dumper=<class 'yaml.dumper.Dumper'>, default_style=None, default_flow_style=None, canonical=None, indent=None, width=None, allow_unicode=None, line_break=None, encoding='utf-8', explicit_start=None, explicit_end=None, version=None, tags=None)

    load(stream, Loader=<class 'yaml.loader.Loader'>)
    # data = load(open(file, 'r')), 从stream中解析第一个yaml文档．
    safe_load(stream) # 解析最基本的tag
    load_all(stream, Loader=<class 'yaml.loader.Loader'>)
