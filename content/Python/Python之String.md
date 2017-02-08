---
layout: post
title: Python之String
comments: true
date: 2016-08-12 16:49:07
updated:
tags:
- string
categories:
- Python
permalink:
---

# String Services

## string

## re

## cStringIO

## StringIO

## codecs

python的编码解码器。

    import codecs

    # 使用注册名为encoding的编码器编码obj，encoding默认为ascii。
    # encode将某个unicode字符串按照encoding定义的编码方式编码成字节序列。
    codecs.encode(obj, [encoding[,errors]])

    # 使用注册名为encoding的解码器解码obj，encoding默认是ascii。
    # decode将一个字节序列按照encoding定义的编码方式解码成unicode字符串。
    codecs.decode(obj, [encoding[,errors]])

    # encoding取下面值:
    # ascii默认值,gb2312, gbk, gb18030, utf-8

    # errors取下面值：
    # strict, 默认值，抛出UnicodeError异常。
    # ignore
    # replace
    # xmlcharrefreplace
    # backslashreplace

    codecs.open(filename, mode='rb', encoding=None, errors='strict', buffering=1)


## struct

## difflib

## textwrap

## unicodedata

## stringprep
