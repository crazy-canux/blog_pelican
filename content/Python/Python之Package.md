---
layout: post
title: Python之Package
comments: true
date: 2016-06-22 05:17:19
updated:
tags:
- python
categories:
- Python
permalink:
---

# PEP426

python最新的打包标准，定义了wheel为最新的python包。

# ensurepip/pip

内置模块,提供使用pip从pypi安装模块。

# distutils

内置的模块。处理简单的包安装。

# distutils2

distutils的升级版，已经废弃。

# distlib

取代distutils和distutils2.

<https://bitbucket.org/pypa/distlib>

# distribute

已经并入setuptools。

# setuptools

<https://github.com/pypa/setuptools>

<https://bitbucket.org/pypa/wheel>

setuotppls是第三方模块, 高级包管理工具，需要安装：

最新的setuptools是合并了原来的setuptools和distribute。

自动处理依赖，egg分发格式，包含了easy_install 来安装egg格式的包。

安装wheel包，可以支持打包wheel包。

    sudo apt-get install python-setuptools

创建setup.py文件：

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
        packages=find_packages(),
        package_dir={"": ""},
        install_requires=INSTALL_REQUIRES,
        extras_require='',
        cmdclass='',
        entry_points={},
        # classifiers 参考 <https://pypi.python.org/pypi?%3Aaction=list_classifiers>
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
    recursive-include docs * OR graft docs
    graft examples
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
    $python setup.py bdist_wheel # 安装wheel包后，可以用setuptools生成wheel包

打包并上传到pypi：

    $python setup.py sdist upload -r pypi
    $python setup.py bdist_wheel upload -r pypi

# pbr

<https://github.com/openstack-dev/pbr>

# 扩展点（Entry Points）

## pkg_resources

## entry_point_inspector

<https://github.com/dhellmann/entry_point_inspector>

## stevedore

<http://docs.openstack.org/developer/stevedore/>
