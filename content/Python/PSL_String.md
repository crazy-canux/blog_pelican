Title: PSL_String
Date: 2016-08-12 16:49:07
Tags: Python, String



# String Services

## string

    import string

classes:

functions:

data:

    ascii_letters
    ascii_lowercase
    ascii_uppercase
    digits
    ...

## re

    import re

classes:

functions:

    compile(pattern, flags=0)
    escape(pattern)
    findall(pattern, string, flags=0)
    finditer(pattern, string, flags=0)
    match(pattern, string, flags=0) # if not match, return None, else return object.
    search(pattern, string, flags=0)
    purge()
    split(pattern, string, maxsplit=0, flags=0) # 根据pattern分割string,返回分割后的列表．
    sub(pattern, repl, string, count=0, flags=0)
    subn(pattern, repl, string, count=0, flags=0)
    template(pattern, flags=0)

data:

    # flags:
    IGNORECASE # 大小写不敏感
    LOCALE
    MULTILINE
    DOTALL
    VERBOSE
    UNICODE

modules:

    # sre_parse module
    # functions:
    sre_parse.parse(str, flags=0, pattern=None)
    sre_parse.expand_template(template, match)
    sre_parse.parse_template(source, pattern)

    # sre_compile module
    # functions:
    sre_compile.compile(p, flags=0)
    sre_compile.isstring(obj)

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

functions:

    open(filename, mode='rb', encoding=None, errors='strict', buffering=1)

data:

## struct

## difflib

    import difflib

classes:

functions:

    get_close_matches(word, possibilities, n=3, cutoff=0.6)

## textwrap

## unicodedata

## stringprep

## readline

## rlcompleter

***
