Title: PSL_Cryptographic
Date: 2016-08-14 21:15:14
Tags: Cryptographic



# Cryptographic Services

## hashlib

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

