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

unittest也叫pyunit，类似于Junit(java)都是基于Kent Beck和Erich Gamma的XUnit框架．

测试结果：

OK 表示测试通过

FAIL 表示测试没有通过，并引发一个AssertionError异常．

ERROR 表示测试过程引发一个不是AssertionError的异常．

    # Python2.7 此处用的是标准库的unittest.
    import unittest
    import MyClass

classes:

    unittest.TestCase: 每个实例就是一个test case. 使用TestCase.assert* 系列方法进行测试．
    unittest.TestSuite: 每个实例就是一个test suite. 多个test case放在一起就是一个test suite.
    unittest.TestLoader/unittest.defaultTestLoader: 用来加载TestCase到TestSuite.
    unittest.TestResult: 用来保存测试的结果．

    unittest.TestProgram/unittest.main(): 搜索该模块下所有test开头的测试用例方法并执行．
    fixtures对一个测试用例的环境的搭建和销毁，通过重载TestCase的setUp()和teaeDown()方法．

    unittest.TextTestRunner: 用来执行测试用例．
    unittest.TextTestResult: 用来打印格式化的测试结果．

    # unittest.TestCase
    # methods:
    assertXXX　系列方法．
    failXXX 系列方法
    fail(self, msg=None) # test立即失败
    addCleanup(self, function, *args, **kwargs)
    addTypeEqualityFunc(self, typeobj, function)
    countTestCases(self)
    debug(self)
    defaultTestResult() # return unittest.TestResult()
    doCleanups(self)
    id(self)
    run(self, result=None) # 可以在子类覆盖该方法．
    shortDescription(self)
    skipTest(self, reason)
    setUp(self) # 重写之后，每个case运行之前都会调用一次．
    tearDown(self) # 同上

    # classmethods:
    setUpClass(cls) # 通过@classmethod重写，这样所有的case运行之前只调用一次，而不是每个case运行之前都调用．
    tearDownClass(cls) # 同上

    # data:
    failureException = AssertionError
    longMessage = False
    maxDiff = 640

functions:

    findTestCases(module, prefix='test', sortUsing=<built-in function cmp>, suiteClass=<class 'unittest.suite.TestSuite'>)
    getTestCaseNames(testCaseClass, prefix, sortUsing=<built-in function cmp>)
    installHandler()
    makeSuite(testCaseClass, prefix='test', sortUsing=<built-in function cmp>, suiteClass=<class 'unittest.suite.TestSuite'>)
    registerResult(result)
    removeHandler(method=None)
    removeResult(result)

    # unittest.case实现了几个函数用来增强unittest.TestCase的方法, 一般当装饰器用．
    expectedFailure(func) # 如果这个case失败了，不计入失败的数目．
    # @unittest.expectedFailure
    skip(reason) # 无条件跳过一个test case.
    skipIf(condition, reason) # condition为true就跳过一个test case.
    skipUnless(condition, reason) # 和上面相反

examples:

    class MyClassTestCase(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            print 'Just execute before the first test case start.'

        @classmethod
        def tearDownClass(cls):
            print 'Just execute after all test case end.'

        def setUp(self):
            """重载setUp进行测试之前的初始化工作.运行每个test_func之前都会运行该方法"""
            print "start"

        def tearDown(self):
            """重载tearDown进行测试结束后的清理工作.结束运行每个test_func之后都会运行该方法"""
            print "end"

        def test_func(self):
            """具体的测试用例，需要用test开头,多个test_func会根据func名字中的数字或字母的顺序来执行，和位置无关.
            不是用test开头的方法默认不会被执行"""
            self.assertEqual(MyClass.method(args), value, "message")

    if __name__ == "__main__":
        unittest.main()

    # 自动发现和批量执行testcase/testsuite:
    def discover_test_case():
        test_cases = []
        _module = ...
        tests.append(unittest.defaultTestLoader.loadTestsFromModule(_module))
        unittest.defaultTestLoader.discover()
        return tests

    def get_test_suite():
        """打包一个testsuite."""
        return unittest.TestSuite(discover_test_case())

    unittest.TextTestRunner
    if __name__ == "__main__":
        runner = unittest.TextTestRunner()
        result = runner.run(get_test_suite())

## mock

<https://github.com/testing-cabal/mock>

python3集成了mock到unittest模块，导入unittest.mock即可．

    # Python2.7
    $pip install mock
    import mock

    # Python3
    import unittest.mock

mock就是在测试中对于不容易构造或获取的对象，用一个虚拟的对象来代替以便测试的方法．

    # Python2.7 此处用的是第三方库mock
    from mock import Mock, patch, PropertyMock, MagicMock

## nose2

<https://github.com/nose-devs/nose2>

nose是unittest/unittest2的升级版．

nose2是nose的升级版．

nose2用于单元测试．

    $ pip install nose

    import nose

## pytest

<https://github.com/pytest-dev/pytest/>

pytest用于单元测试．推荐使用．

    $ pip install -U pytest

    import pytest

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
