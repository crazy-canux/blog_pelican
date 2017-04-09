Title: Package
Date: 2016-06-22 05:17:19
Tags: Python, Package



# Package

PEP426是python最新的打包标准，定义了wheel为最新的python包。

<https://www.python.org/dev/peps/pep-0426/>

## ensurepip

内置模块.提供使用pip从pypi安装模块。

## distutils

内置的模块.处理简单的包安装,一般使用setuptools代替该模块。

## venv

python3新增了虚拟环境的包．python2中使用virtualenv.

## zipapp

python3新增管理可执行的python的zip包．

***

# TPL

相关的第三方库

# virtualenv

python3.4之后并入了虚拟化标准库venv.

分离的虚拟的python环境,自动安装setuptools和pip

<https://github.com/pypa/virtualenv>

    $cd project

    # 默认python2.7
    $virtualenv .venv
    # 指定python3
    $virtualenv -p `which python3` .venv

    # 激活虚拟环境
    $source .venv/bin/activate

    # 先升级pip和setuptools
    $pip install pip
    $pip install setuptools

    # 导出项目用的所有依赖库．
    $pip freeze > requirements.txt
    # 在其它环境需要安装依赖：
    $pip install -r
    requirements.txt

## setuptools

<https://github.com/pypa/setuptools>

<https://bitbucket.org/pypa/wheel>

python2.7.9和python3.4以及virtualenv自带setuptools．

支持sdist打包成tar.gz包,和wheel打包成whl包．

    $pip install -U setuotools
    $pip install -U wheel

创建setup.py文件：

<https://pypi.python.org/pypi?%3Aaction=list_classifiers>

    import os

    from setuptools import setup, find_packages

    import project

    def read(readme):
        extend = os.path.splitext(readme)[1]
        # pypi只识别reST格式
        if (extend == ".rst"):
            import codecs
            return codecs.open(readme, 'r', 'utf-8').read()
        # pypandoc可以将markdown格式转换成reST格式
        elif (extend == ".md"):
            import pypandoc
            return pypandoc.convert(readme, 'rst')

    setup(
        name=project,
        version=project.__version__,
        author='',
        author_email='',
        maintainer='',
        maintainer_email='',
        description=''
        long_description=read('README.XXX'),
        license='',
        platforms='any',
        keywords='',
        url='',
        download_url='',
        # find_packages会自动查找包含__init__.py的包．
        packages=find_packages(),
        package_dir={"": ""},
        install_requires=['a==1.0.0', 'b>=1.0.0'],
        extras_require='',
        cmdclass='',
        entry_points={},
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            ...
        ],
        test_suite='',
        test_require='',
    )

创建setup.cfg文件：

    [wheel]
    universal = 1

创建README.rst文件：

可以是rst格式也可是是md格式。

如果是md格式不要使用类似于***的分割线。

    参考rst和md的文档

创建MAINFEST.in文件：

默认只有python模块和包会被打包，如果需要其它文件需要添加到这个文件中。

    include LICENSE README.rst AUTHORS.rst CONTRIBUTING.rst
    recursive-include docs *
    graft examples
    graft tests
    global-exclude *.py[co]
    prune docs/_build
    prune docs/_themes

创建\_\_init\_\_.py文件：

位于project/project/\_\_init\_\_.py，安装后用import导入，help(project)看到的信息。

    NAME: 自动获取的项目名字 - 该文件注释的总结部分
    FILE: /install_path/project/project/__init__.py
    DESCRIPTION: 该文件的注释，除总结部分
    PACKAGE CONTENTS: 在project/project/自动获取的py文件名
    DATA: __开头和结尾的变量
    VERSION: __version__变量的值
    AUTHOR: __author__变量的值

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    SUMMARY

    Descriptions
    """

    __version__ = ''
    __author__ = ''

    ...

发布到pypi主服务器pypi：

去pypi注册帐号

<https://pypi.python.org/pypi>

创建~/.pypirc文件

    [distutils]
    index-servers = pypi

    [pypi]
    username = <username>
    password = <password>

在索引中注册项目(不再支持，直接upload)：

    $python setup.py register -r pypi

打包:

    $python setup.py sdist # 生成tarball
    $python setup.py bdist_wheel # 安装wheel后，可以用setuptools生成wheel包

打包并上传到pypi：

    $python setup.py sdist upload -r pypi
    $python setup.py bdist_wheel upload -r pypi

## pbr

<https://github.com/openstack-dev/pbr>

## 扩展点（Entry Points）

* pkg_resources

* entry_point_inspector

<https://github.com/dhellmann/entry_point_inspector>

* stevedore

<http://docs.openstack.org/developer/stevedore/>
