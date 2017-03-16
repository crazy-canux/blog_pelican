Title: PSL_Test
Date: 2016-04-11 22:58:13
Tags: Python, Test

# Test

python的测试工具．

## 2to3

    $2to3

## pydoc

    import pydoc

## test

    import test

## doctest

python内置的文档测试库．

    import doctest

## unittest

python内置的单元测试库．

    import unittest

***

# TPL

相关的第三方库

## unittest2

unittest2是unittest的升级版．

python3集成了unittest2到unittest,像使用unittest一样使用即可．

    # python2.7
    $pip install unittest2
    import unittest2

    # python3
    import unittest

## mock

<https://github.com/testing-cabal/mock>

python3集成了mock到unittest模块，导入unittest.mock即可．

    # Python2.7
    $pip install mock
    import mock

    # Python3
    import unittest.mock

## nose2

<https://github.com/nose-devs/nose2>

nose是unittest/unittest2的升级版．

nose2是nose的升级版．

nose2用于单元测试．

    $ pip install nose

    import nose2

## pytest

<https://github.com/pytest-dev/pytest/>

pytest用于单元测试．推荐使用．

    $ pip install -U pytest

    import pytest

     def test_main():
         ...

    if __name__ == "__main__":
        pytest.main("/path/to/test_script.py")

    $ py.test

***

## coverage

测试代码覆盖率

<https://github.com/nedbat/coveragepy>

    $ pip install coverage

    # 通过命令进行测试，可以集成到其它工具．
    $ coverage run --source=<package-name> setup.py test

## tox

virtualenv management and test command line tool.

<https://github.com/tox-dev/tox>

    $ pip install tox

    # 通过命令进行测试，可以集成nose2, pytest, coverage等工具．
    $ tox

## buildbot

Python-based continuous integration testing framework

<https://github.com/buildbot/buildbot>

## pybuilder

Continuous build tool for Python.

<https://github.com/pybuilder/pybuilder>
