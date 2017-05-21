Title: PSL_File
Date: 2016-08-14 20:51:28
Tags: Python, File



# File and Directory Access

## os.path

windows的路径要写成：

    C:\\test\\sub\\

    import os
    os.path.expanduser(path) # 把path中~或~user扩展成绝对路径 expanduser("~/src") -> /home/user/src
    os.path.realpath(filename) # 返回filename的真实路径+文件名 realpath("/home/user/file.py") -> /home/user/file.py
    os.path.dirname(filename) # 返回filename的路径 dirname("/home/user/file.py") -> /home/user
    os.path.join(a, *p) # 拼结一个完整的路径　
    os.path.join(a, os.pardir) # 返回上级目录的路径
    os.path.abspath(path) # 返回绝对路径

## stat

## fileinput

## filecmp

## fnmatch

## linecache

## glob

## shutil

## tempfile

## macpath

## ConfigParser

***

# File Formats

## csv

    import csv
    DictReader(self, f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

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
