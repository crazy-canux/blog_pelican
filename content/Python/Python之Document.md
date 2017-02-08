---
layout: post
title: Python之Document
comments: true
date: 2016-08-03 21:57:26
updated:
tags:
- reST
- Sphinx
- readthedoc
categories:
- Python
permalink:
---

# Sphinx

<https://github.com/sphinx-doc/sphinx>

<https://zh-sphinx-doc.readthedocs.io/en/latest/contents.html>

Sphinx就是python处理reStructuredText格式的工具。

安装：

    pip install -U Sphinx

使用sphinx：

    $cd your-project/docs

    $sphinx-quickstart
    # 以下选项需要手动设定，其它都可以用默认值：
    > Project name: pydeveloper
    > Author name(s): Canux CHENG
    > Project version: 1.0.0.0
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y

配置文件conf.py包含刚才的所有配置，可以在这里手动修改。

<http://www.sphinx-doc.org/en/1.4.8/config.html#confval-locale_dirs>

添加包的版本：

    sys.path.insert(0, os.path.abspath(".."))
    from <project> import __version__

修改自己的配置：

    copyright = u'2016, <a href="http://canuxcheng.com">Canux CHENG</a>'

# sphinx-docs

<https://zh-sphinx-doc.readthedocs.io/en/latest/markup/index.html#sphinxmarkup>

sphinx的标记把reST格式的文档关联起来。

index.rst这是文档的首页。

# sphinx-build

生成web可读的文档。

简单方法生成文档：

    # 生成html格式的文档
    $make html
    $make latexpdf

# sphinx-apidoc

自动生成API文档。

    $sphinx-apidoc

# Debug

浏览器打开docs/_build/html/index.html即可。

# ReadTheDocs

<https://readthedocs.org/>

<http://readthedocs.readthedocs.io/zh_CN/latest/>

将项目文档部署到readthedocs站点。

直接注册帐号，同步github项目，然后导入你的项目即可。

# alabaster

<https://github.com/bitprophet/alabaster/>

这个主题是sphinx的默认主题，基于requests和flask的文档的主题而来。

主题设置：

    html_theme_options = {
        'github_user': 'crazy-canux',
        'github_repo': '<your-project>',
        'github_banner': True,
        'show_powered_by': False,
        'show_related': True,
    }

***

# pypandoc

<https://github.com/bebraw/pypandoc>

文档转换工具pandoc的python包。

安装：

    pip install pypandoc

