Title: PSL_File
Date: 2016-08-14 20:51:28
Tags: Python, File



# File and Directory Access

## os.path

windows的路径要写成：

    C:\\test\\sub\\

    import os
    os.path.expanduser(path) # 把path中~或~user扩展成绝对绝对路径

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
