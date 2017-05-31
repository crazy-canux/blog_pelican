Title: DevOps
Date: 2016-04-03 10:49:21
Tags: Python, Vim, Pycharm



# python

python2的最后一个版本是python2.7, 2020年停止更新.

Windows安装：

    Python2.7.9之后的版本直接下载msi安装即可．
    选择自动设置PATH，默认安装pip和setuptools.
    可以使用IDLE或python命令行或cmd执行python命令

Linux安装：

    $sudo apt-get install python
    $sudo yum install python

    $sudo apt-get install python-dev
    $sudo yum install python-devel

    $sudo apt-get install python3-dev
    $sudo yum install python3-devel

    $sudo apt-get install libssl-dev
    $sudo yum install openssl-devel

标准库的路径：

    C:\Python27\Lib
    /usr/lib/python2.7/

命令：

    $ python/ipython     # 进入python解释器
    >>>exit()/Ctrl+d     # 退出python解释器
    >>>help()            # 进入help工具
    help>quit            # 退出help工具
    $ pydoc --help        # 文档工具

python的IDE：

1. Windows: IDLE
2. Linux: Vim
3. Pycharm/IntelliJ

python的可用接口

1. python内置函数，类和异常．

    C/C++实现的，不需要导入就可以使用的。

2. python标准库

    python实现的，需要导入才能使用的。

3. python外部库

    需要安装和导入才能使用的。外部库是对python代码的补充。

4. python框架

    需要安装和导入才能使用的。python代码是对外部库的补充。

***

# python的其它解释器

## cpython

python的默认解释器，安装python即可获得。

<https://github.com/python/cpython>

## stackless

cpython的增强版，支持多线程。

<https://bitbucket.org/stackless-dev/stackless>

## pypy

用python写的python解释器。

比cpython更快的python。

<https://bitbucket.org/pypy/pypy>

## jpython

java开发的可以运行在JVM平台的python解释器。

## ironpython

C#开发的可以运行在.net/mono平台的python解释器。

***

# python开发相关的工具

## ipython

python写的交互式解释器。

<https://github.com/ipython/ipython>

    $pip install ipython

## pyenv

python的版本管理工具.

<https://github.com/yyuu/pyenv>

***

# 第三方库

<https://pypi.python.org/pypi>

第三方库路径：

    C:\Python27\Lib\site-packages
    /usr/lib/python2.7/dist-packages
    /usr/lib/python2.7/site-packages
    /usr/local/lib/python2.7/dist-packages
    /usr/local/lib/python2.7/site-packages

* 二进制安装：

        $sudo apt-get install python-packagename

* 源码安装第三方库：

        $ cd package
        $ python setup.py install

* easy_install(setuptools)安装：

    <https://github.com/pypa/setuptools>

    easy_install安装egg包,不推荐使用．

    setuptools带的工具,从pypi的egg归档格式中安装。

    python2.7.9, python3.4, virtualenv自带setuptools.

    缺点是不支持卸载。

        $sudo apt-get install python-setuptools

        $pip install -U setuptools

        $sudo -E easy_install packagename[=version] # 安装
        $sudo -E easy_install -U packagename[=version] # 升级

* pip安装：

    <https://github.com/pypa/pip>

    python2.7.9和python3.4和virtualenv自带pip.

    直接从pypi安装wheel格式和sdist格式(也就是tarball)。

        $sudo apt-get install python-pip
        $sudo apt-get install python-wheel

        $pip install -U pip
        $pip install -U wheel

        $ pip install packagename[==version] # 安装
        $ pip install -U packagename[==version] # 升级
        $ pip uninstall packagename # 卸载
        $ pip install XXX.whl # 安装wheel包

        $pip list
        $pip search packagename
        $pip freeze > requirements.txt
        $pip install -r requirements.txt

***

# python代码检查

* flake8

    <https://github.com/PyCQA/flake8>

    Include: pyflakes, pep8/pycodestyle, McCabe

* pylama

    <https://github.com/klen/pylama>

    Include: pyflakes, pylint, pep8/pycodestyle, pep257/pydocstyle, mccabe, radon, ghslint(for js)

* pep8/pycodestyle

    Simple Python style checker in one Python file.

    <https://github.com/PyCQA/pycodestyle>

* pep257/pydocstyle

    docstring style checker

    <https://github.com/PyCQA/pydocstyle>

* jedi

    Awesome autocompletion and static analysis library for python.

    <https://github.com/davidhalter/jedi>

* mccabe

    McCabe complexity checker for Python

    <https://github.com/PyCQA/mccabe>

* pyflakes

    A simple program which checks Python source files for errors.

    Faster than pylint.

    <https://github.com/PyCQA/pyflakes>

* pylint

    A Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells

    <https://github.com/PyCQA/pylint>

        $pylint --list-msgs
        $pylint --help-msg=C6409

* rope

    A python refactoring library

    <https://github.com/python-rope/rope>

***

# python项目结构

    .
    |-- README.rst
    |-- LICENSE
    |-- AUTHORS.rst
    |-- CONTRIBUTING.rst

    |-- project    项目源代码目录
        |-- __init__.py 包文件
        ...
    |-- docs       用来存放文档
        |-- conf.py
        |-- index.rst
        ...

    |-- tests 用来存放测试相关的文件(不能有__init__.py)
    |-- examples 用来存放使用本包相关的例子(不能有__init__.py)

    |-- bin 用来存放将被setup.py安装的二进制脚本
    |-- data 用来存放其它类型文件
    |-- etc 用来存放配置文件
    |-- tools 用来存放与工具相关shell脚本
    |-- scripts 用来存放安装相关的脚本

    |-- setup.py 标准安装脚本
    |-- setup.cfg
    |-- MANIFEST.in

    |-- .gitignore
    |-- .gitattributes
    |-- requirements.txt 依赖的环境
    |-- Makefile
    |-- fabfile.py

***
