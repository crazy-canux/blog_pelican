Title: PSL_Test
Date: 2016-04-11 22:58:13
Tags: Python, Test, TDD

# Test

python的单元测试库．

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

也叫pyunit，类似于Junit(java)都是基于Kent Beck和Erich
Gamma的XUnit框架．

测试结果：

OK 表示测试通过

FAIL 表示测试没有通过，并引发一个AssertionError异常．

ERROR 表示测试过程引发一个不是AssertionError的异常．

    import unittest
    import MyClass

    unittest.TestCase: 每个实例就是一个test case. 使用TestCase.assert* 系列方法进行测试．
    unittest.TestSuite: 每个实例就是一个test suite. 多个test case放在一起就是一个test suite.
    unittest.TestLoader/unittest.defaultTestLoader: 用来加载TestCase到TestSuite.
    unittest.TextTestRunner: 用来执行测试用例．
    unittest.TextTestResult: 用来保存测试的结果．
    unittest.TestResult: 用来保存测试的结果．
    unittest.main()/unittest.TestProgram: 搜索该模块下所有test开头的测试用例方法并执行．
    fixtures对一个测试用例的环境的搭建和销毁，通过重载TestCase的setUp()和teaeDown()方法．

    # unittest.TestCase
    defaultTestResult() # return unittest.TestResult()

    class MyClassTest(unittest.TestCase):

        def setUp(self):
            """重载setUp和tearDown."""
            pass

        def tearDown(self):
            pass

        def test_func(self):
            """具体的测试用例，需要用test开头"""
            self.assertEqual(MyClass.method(args), value, "message")

    if __name__ == "__main__":
        unittest.main()

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

分析单元测试的代码覆盖率

<https://github.com/nedbat/coveragepy>

    $ pip install coverage

    # 通过命令进行测试，可以集成到其它工具．
    $ coverage run --source=<package-name> setup.py test

***

## tox

virtualenv management and test command line tool.

<https://github.com/tox-dev/tox>

    $ pip install tox

    # 通过命令进行测试，可以集成unittest, nose2, pytest等工具．
    $ tox

***

## buildbot

Python-based continuous integration testing framework

<https://github.com/buildbot/buildbot>

## pybuilder

Continuous build tool for Python.

<https://github.com/pybuilder/pybuilder>
