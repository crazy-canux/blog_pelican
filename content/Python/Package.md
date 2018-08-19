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

## virtualenv

python3.5开始并入了虚拟化标准库venv.

分离的虚拟的python环境,自动安装setuptools和pip和wheel

<https://github.com/pypa/virtualenv>

    $cd project

    # 默认python2.7
    $virtualenv .venv
    # 指定python3, 会安装pip/setuptools/wheel到当前环境.
    $virtualenv -p `which python3` .venv

    # 激活虚拟环境
    $source .venv/bin/activate

    # 先升级pip和setuptools
    $pip install pip
    $pip install setuptools
    $pip install wheel

    # 导出项目用的所有依赖库．
    $pip freeze > requirements.txt
    # 在其它环境需要安装依赖：
    $pip install -r requirements.txt

virtualenvwrapper

<https://bitbucket.org/virtualenvwrapper/virtualenvwrapper>

封装了virtualenv的工具:

    $ pip install virtualenvwrapper

    # 创建主目录
    $ mkdir -p $WORKON_HOME

    # 最好写入到.bashrc/.zshrc:
    $ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
    $ export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
    $ export WORKON_HOME=~/.virtualenvs
    $ source /usr/local/bin/virtualenvwrapper.sh

    # 为每个项目创建独立python环境：
    $ mkvirtualenv -r requirementx.txt [project-name]
    # 不安装setuotools/wheel/pip
    $ mkvirtualenv --no-setuptools --no-wheel --no-pip [name]
    # 指定查找pip/setuptools的路径
    --extra-search-dir=/usr/local/lib/python2.7/dist-packages
    --extra-search-dir=/usr/lib/python2.7/dist-packages
    $ workon [project-name] # 切换到针对该项目的virtualenv
    (pro)$ /path/to/pip install [package] # 安装第三方包
    (pro)$ ~/.virtualenvs/[project-name]/bin/python setupt.py install # 源码安装
    (pro)$ lssitepackages # 查看安装的第三方包
    $ deactivate # 退出virtualenv
    $ rmvirtualenv [project-name] # 删除环境

pipenv

<https://github.com/pypa/pipenv>

封装了virtualenv的工具，用于取代virtualenvwrapper.

## setuptools

<https://github.com/pypa/setuptools>

<https://github.com/pypa/wheel>

python2.7.9和python3.4以及virtualenv自带setuptools．

支持sdist打包成tar.gz包,和wheel打包成whl包．

    $pip install -U pip
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
        # metadata:
        name=project,
        version=project.__version__,
        url='',
        download_url='',
        author='',
        author_email='',
        maintainer='',
        maintainer_email='',
        description=''
        long_description=read('README.XXX'),
        license='',
        platforms='any',
        keywords='',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            ...
        ],

        # options

        # 指定源码的位置
        packages=find_packages(),
        package_dir={},

        # 需要和源码一起安装的非代码文件,写入MANIFEST.in
        # 比如文档和测试文件
        package_data={}, # 将指定的文件放入安装路径
        include_package_data=None, # True表示
        exclude_package_data=None,

        # 不需要和源码一起安装的非代码文件.
        # 比如配置文件
        data_files=[(dest, source),()],

        # 通过pip安装requirement
        install_requires=['a==1.0.0', 'b>=1.0.0'],
        # python版本的要求
        python_requires='>=3',
        setup_requires=[],
        extras_require=None,
        test_require=[]

        zip_safe=True,

        # 安装一个命令
        scripts=[],    # 会被添加到环境变量用于命令.

        entry_points={}

        # preinst/postinst
        cmdclass={
            "develop": PostInstDevelop,
            "install": PostInstInstall
        }
    )

怎样实现postinst功能：

    from setuptools.command.develop import develop
    from setuptools.command.install import install

    class InstDevelop(develop):
        def run(self):
            # your preinst code here for develop.
            develop.run(self)
            # your postinst code here for develop.

    class InstInstall(install):
        def run(self):
            # your preinst code here for install.
            install.run(self)
            # your postinst code here for install.

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

    [Deprecated] $ python setup.py register -r pypi

先打包, 在dist目录生成包:

    $ python setup.py sdist # 生成tarball
    $ python setup.py bdist_wheel # 安装wheel后，可以用setuptools生成wheel包

再上传到pypi(推荐):

    $ pip install twine
    $ twine upload dist/*

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
