Title: PSL_Cryptographic
Date: 2016-08-14 21:15:14
Tags: Python, Cryptographic



# Cryptographic Services

## hashlib

哈希算法和摘要算法标准库，就是把任意长度的数据转换为一个长度固定的数据串．

MD5: Message Digest Algorithm 5.

SHA1: Secure Hash Algorithm.

    import hashlib

classes:

    # methods:
    # 哈希对象有下列方法：
    update(arg) # 更新字符串
    md5.update('string or read from a file') # 放入需要转换的内容

    digest() # 字符串
    hexdigest() # 十六进制字符串
    md5.hexdigest() # 获取md5十六进制字符串

    copy() # 复制哈希对象

functions:

    # 下类函数都返回哈希对象
    new(name, string='')
    md5()
    md5 = hashlib.md5() # 创建一个md5的hash对象
    sha1()
    sha224()
    sha256()
    sha384()
    sha512()

## hmac

***

# TPL

相关的第三方库

## pycrypto

<https://github.com/dlitz/pycrypto>

windows需要MS Visual C++ compiler for python2.7.

    $ pip install pycrypto

## ecdsa

pure-python ECDSA signature/verification

<https://github.com/warner/python-ecdsa>

    $ pip install ecdsa

## pygpgme

<https://pypi.python.org/pypi/pygpgme>

A Python wrapper for the GPGME library.

Windows安装失败？

    # 需要先安装gpgme的开发库
    $ sudo apt-get install libgpgme11-dev
    $ pip install pygpgme

