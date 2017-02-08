---
layout: post
title: Python之DevelopmentTest
comments: true
date: 2016-04-11 22:58:13
updated:
tags:
- development
- test
categories:
- Python
permalink:
---

# 2to3

    $2to3 --help

# pydoc

    $pydoc --help

***

# test

    import test

# doctest

    import doctest

# unittest

    import unittest

***

# unittest2

<https://pypi.python.org/pypi/unittest2>

unittest的向后兼容版本。

    pip install unittest2

# nose2

<https://github.com/nose-devs/nose2>

nose2是unittest2的下一代测试环境.

    pip install nose

***

# tox

virtualenv的管理和测试命令行工具.

<https://github.com/tox-dev/tox>

***

# fixture

<https://github.com/testing-cabal/fixtures>

    pip install fixture

# mock

python2:

<https://github.com/testing-cabal/mock>

    pip install mock

python3:

合并到了unittest.

    import unittest.mock

# testscenarios

<https://github.com/testing-cabal/testscenarios>

# subunit

<https://github.com/testing-cabal/subunit>

