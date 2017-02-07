Title: Pelican
Date: 2013-04-01 12:49:49
Modified: 2017-02-01 12:49:49
Tags:
Slug:
Authors:
Summary:



# Pelican

python开发的静态站点生成器.

<http://blog.getpelican.com/>

<https://github.com/getpelican/pelican>

<http://pelican-docs-zh-cn.readthedocs.io/en/latest/getting_started.html>

<http://pelican-zh.readthedocs.io/en/latest/zh-cn/>

# 搭建博客

创建环境:

    $mkdir blog_pelican
    $cd blog_pelican
    $virtualenv venv
    $source venv/bin/activate
    $pip install pelican
    $pip install markdown

创建pelican项目:

    $pelican-quickstart

生成下列文件和目录:

    publishconf.py # 主配置文件
    pelicanconf.py # 发布的配置文件
    fabfile.py # fabric配置文件
    Makefile   # make配置文件
    develop_server.sh # 用于开启测试服务器
    content # 用于存放所有文章
    output # 静态生成文件

生成博客站点:

    $pelican content

预览站点:

    $cd output
    $python -m pelican.server
    $firefox http://localhost:8000/

# 发布站点

pelican部署博客:

    # 将rst或md格式转换成html.
    $pelican content

    # 浏览生成的文件
    $firefox output/index.html
    # 启动web服务器预览
    $python2.7 -m SimpleHTTPServer
    $python3 -m http.server
    $firefox http://localhost:8000/

    # 部署站点
    $pelican content -s publishconf.py

fabric部署博客:

    $fab build # 生成页面
    $fab regenerate # 自动重新生成页面
    $fab serve # 启动测试服务器
    $fab publish

make部署博客:

    $make html # 生成页面
    $make regenerate # 自动重新生成页面
    $make serve # 启动测试服务器
    $make devserver # 同时生成页面并启动测试服务器
    $./develop_server.sh stop # 停止测试服务器
    $make rsync_upload

***

# 配置

pelicanconf.py

publishconf.py

参考pelican和hexo的配置：

<https://github.com/crazy-canux/blog_hexo>

<https://github.com/crazy-canux/blog_pelican>

***

# Theme

添加主题

    $cd blog_pelican
    $git submodule add https://github.com/getpelican/pelican-themes.git themes

安装主题：

    $cd pelican-themes
    $pelican-themes -i bootstrap2

在pelicanconf.py添加主题：

    THEME = 'bootstrap2'

***

# Plugin

添加插件：

    $cd blog_pelican
    $git submodule add https://github.com/getpelican/pelican-plugins.git plugins
