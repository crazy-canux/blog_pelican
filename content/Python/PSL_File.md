Title: PSL_File
Date: 2016-08-14 20:51:28
Tags: Python, File, glob, tempfile, csv, json, yaml



# File and Directory Access

## os.path

windows的路径要写成：

    C:\\test\\sub\\

    import os

function:

    os.path.expanduser(path) # 把path中~或~user扩展成绝对路径 expanduser("~/src") -> /home/user/src
    os.path.expandvars(path) # 把path中的shell变量$var 或 ${var} 还原．
    os.path.dirname(filename) # 返回filename的路径 dirname("/home/user/file.py") -> /home/user
    os.path.join(a, *p) # 拼结一个完整的路径　
    os.path.join(a, os.pardir) # 返回上级目录的路径
    os.path.realpath(filename) # 返回filename的真实路径+文件名 realpath('__file__')
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

    copy(src, dst)
    copy2(src, dst)
    ...
    rmtree(path, ignore_errors=False, onerror=None) # 删除指定的目录,path不能是文件．
    unregister_archive_format(name)
    move(src, dst)
    ...

## tempfile

## macpath

## ConfigParser

一般用来处理*.ini文件，格式为：

    [section]
    option-key = option-value


导入：

    import ConfigParser

classes:

    ConfigParser.ConfigParser(defaults=None)
    # methods:
    read(filenames) # 读取ini文件
    sections() # 获取所有section
    options(section) # 获取section的所有option
    get(section, option, raw=False, vars=None) # 返回字符串
    getint(section, options)
    getfloat(section, options)
    getboolean(section, options) # 大小写都可以:0/1, false/true, no/yes, off/on
    set(section, option, value)
    has_section(section)
    has_option(section, option)
    remove_section(section)
    remove_option(section, option)
    write(fp)

issue:

    默认是全部小写写入.
    config = ConfigParser.ConfigParser(allow_no_value=True)
    config.optionxform =str # 原样写入

***

# File Formats

## csv

    import csv

classes:

    # csv.DictReader
    DictReader(self, f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
    # methods
    next()

    # csv.DictWriter
    DictWriter(self, f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwargs)
    # mthods
    writeheader()
    writerow(rowdict)
    writerows(rowdicts)

functions:

    // 返回DictReader对象
    reader(iterable, dialect='excel', **kwargs)

    // 返回DictWriter对象
    writer(fileobj, dialect='excel', **kwargs)

data:

## robotparser

## netrc

## xdrlib

## plistlib

## json

http api(restful)一般使用json格式的数据．

python和json数据类型对应关系参考WEB/JSON.

complex和class/def不能被编码.

    import json

classes:

functions:

    # 将转换后的json格式写入文件
    dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
    with open(file, 'w') as f:
        json.dump(dict_data, f)

    # 将dict类型转换成json格式
    dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
    json_data = json.dumps(dict_data)

    indent=4 # 写入自动缩进４个空格

    # 将读出的文件(json格式)转换成dict
    load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    with open(file, 'r') as f:
        dict_data = json.load(f)

    # json类型变成dict类型
    loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    response_dict = json.loads(response.content) # 使用requests获取的json数据,转化为dict类型

***

# yaml

<http://pyyaml.org/wiki/PyYAML>

***

# Internet Data Handling

## email

## mailcap

## mailbox

## mimetypes

## base64

    import base64

## binhex

## binascii

## quopri

## uu

