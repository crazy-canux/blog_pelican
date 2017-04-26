Title: PSL_String
Date: 2016-08-12 16:49:07
Tags: Python, String



# String Services

## string

## re

    import re


## cStringIO

## StringIO

## codecs

python的编码解码器coder/decoder。

    import codecs

    # 使用注册名为encoding的编码器编码obj，encoding默认为ascii。
    # encode将unicode编码的obj编码成encoding编码对应的字节序列．
    codecs.encode(obj, [encoding[,errors]])
    codecs.encode(u'hello world', 'utf-8') # 编码成utf-8字节序．

    # 使用注册名为encoding的解码器解码obj，encoding默认是ascii。
    # decode将原来按照encoding编码的obj解码成unicode字符串.
    codecs.decode(obj, [encoding[,errors]])
    codecs.decode(obj, 'utf-8') # 将utf-8编码的obj解码成unicode.

    # encoding取下面值:
    # ascii是默认值,gb2312, gbk, gb18030, utf-8, utf-16
    # ascii利用一个字节把字符转换成数字．
    # unicode利用多字节转换，支持多种编码方式，utf-8, uft-16.

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

***

# TPL

相关的第三方库
